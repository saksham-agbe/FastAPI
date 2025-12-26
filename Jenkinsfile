pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = "learning_fastapi"
        REPO_URL = "https://github.com/saksham-agbe/FastAPI.git"
        BRANCH = "main"
        APP_DIR = "/workspace/FastAPI"
    }

    stages {

        stage('Ensure Git Repo') {
            steps {
                dir("${APP_DIR}") {
                    sh '''
                    if [ ! -d .git ]; then
                      echo "Initializing git repo..."
                      git init
                      git remote add origin ${REPO_URL}
                      git fetch origin
                      git checkout -B ${BRANCH} origin/${BRANCH}
                    fi
                    '''
                }
            }
        }

        stage('Check for Changes') {
            steps {
                dir("${APP_DIR}") {
                    sh '''
                    git fetch origin ${BRANCH}

                    CHANGES=$(git diff HEAD origin/${BRANCH})

                    if [ -z "$CHANGES" ]; then
                      echo "No changes detected. Skipping deployment."
                      exit 0
                    else
                      echo "Changes detected. Proceeding with deployment."
                    fi
                    '''
                }
            }
        }

        stage('Pull Latest Code') {
            steps {
                dir("${APP_DIR}") {
                    sh 'git pull origin ${BRANCH}'
                }
            }
        }

        stage('Build Docker Images') {
            steps {
                dir("${APP_DIR}") {
                    sh 'docker-compose build'
                }
            }
        }

        stage('Deploy Containers') {
            steps {
                dir("${APP_DIR}") {
                    sh 'docker-compose up -d'
                }
            }
        }
    }

    post {
        success {
            echo "Deployment successful using GitHub diff"
        }
        failure {
            echo "Deployment failed"
        }
    }
}
