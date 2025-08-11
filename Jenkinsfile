pipeline {
    agent any
    environment {
        IMAGE_NAME = 'flask-calculator'
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/OP-CODER/Flask-calculator.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                bat "docker build -t ${IMAGE_NAME} ."
            }
        }
        stage('Test') {
            steps {
                bat """
                docker run --rm -v "C:/Users/mohda/.jenkins/workspace/Flask-calculator:/app" -w /app ${IMAGE_NAME} pytest tests/
                """
            }
        }
        stage('Deploy') {
            steps {
                bat """
                docker stop flask-calculator || exit 0
                docker rm flask-calculator || exit 0
                docker run -d --name flask-calculator -p 5000:5000 ${IMAGE_NAME}
                """
            }
        }
    }
}
