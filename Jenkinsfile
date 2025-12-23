pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = "learning_fastapi"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/saksham-agbe/FastAPI.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Deploy Containers') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }

    post {
        success {
            echo " FastAPI deployed successfully"
        }
        failure {
            echo " Deployment failed"
        }
    }
}
