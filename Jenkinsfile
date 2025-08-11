pipeline {
  agent any
  environment {
    IMAGE_NAME = 'flask-calculator'
  }
  stages {
    stage('Checkout') {
      steps {
        git 'https://github.com/OP-CODER/Flask-calculator.git'
      }
    }
    stage('Build Docker Image') {
      steps {
        script {
          docker.build("${IMAGE_NAME}")
        }
      }
    }
    stage('Test') {
      steps {
        script {
          docker.image("${IMAGE_NAME}").inside {
            sh 'pytest'
          }
        }
      }
    }
stage('Deploy') {
  steps {
    script {
      sh """
      docker stop flask-calculator || true
      docker rm flask-calculator || true
      docker run -d --name flask-calculator -p 5000:5000 ${IMAGE_NAME}
      """
    }
  }
}
