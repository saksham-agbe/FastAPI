pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = "learning_fastapi"
    }

    stages {

        stage('Use Local Code') {
            steps {
                dir('/workspace/FastAPI') {
                    sh 'ls -la'
                }
            }
        }

        stage('Build Docker Images') {
            steps {
                dir('/workspace/FastAPI') {
                    sh 'docker-compose build'
                }
            }
        }

        stage('Deploy Containers') {
            steps {
                dir('/workspace/FastAPI') {
                    sh 'docker-compose up -d'
                }
            }
        }
    }

    post {
        success {
            echo "Deployed successfully from local directory"
        }
        failure {
            echo "Deployment failed"
        }
    }
}
