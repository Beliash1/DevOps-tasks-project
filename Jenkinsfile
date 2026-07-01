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
                script {
                    dockerImage = docker.build("${IMAGE_NAME}:${IMAGE_TAG}", "./backend")
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Running basic health check test...'
                script {
                    docker.image("${IMAGE_NAME}:${IMAGE_TAG}").inside('--entrypoint=""') {
                        sh 'python -c "import flask; print(\'Flask import OK\')"'
                    }
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo 'Pushing image to Docker Hub...'
                script {
                    sh "echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin"
                    dockerImage.push("${IMAGE_TAG}")
                    dockerImage.push("latest")
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application locally with docker-compose...'
                sh 'docker compose down || true'
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
            sh 'docker logout'
        }
    }
}