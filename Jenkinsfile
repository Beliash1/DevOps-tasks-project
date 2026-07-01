pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        IMAGE_NAME = 'beliash1/devops-tasks-backend'
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} -t ${IMAGE_NAME}:latest ./backend"
            }
        }

        stage('Test') {
            steps {
                echo 'Running basic health check test...'
                sh "docker run --rm ${IMAGE_NAME}:${IMAGE_TAG} python -c \"import flask; print('Flask import OK')\""
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo 'Pushing image to Docker Hub...'
                sh "echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin"
                sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                sh "docker push ${IMAGE_NAME}:latest"
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application locally with docker-compose...'
                sh 'docker compose down || true'
                sh 'docker rm -f tasks_db tasks_backend || true'
                sh 'docker compose up -d --build'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Check logs above.'
        }
        always {
            sh 'docker logout || true'
        }
    }
}