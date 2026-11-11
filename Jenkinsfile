pipeline {
  agent any

  environment {
    IMAGE_NAME = "<ваш-логин>/demo-app"
    IMAGE_TAG = "${env.BUILD_NUMBER}"
  }

  options {
    timestamps()
  }

  triggers {
    pollSCM('H/5 * * * *')
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Setup') {
      steps {
        sh 'python3 -m venv venv'
        sh './venv/bin/pip install --upgrade pip'
        sh './venv/bin/pip install -r requirements.txt'
      }
    }
    stage('Build') {
      steps {
        sh './venv/bin/python -m py_compile app.py'
      }
    }
    stage('Test') {
      steps {
        sh './venv/bin/pytest --junitxml=result.xml'
      }
    }
    stage('Docker Build') {
       steps {
       sh "docker build -t${IMAGE_NAME}:${IMAGE_TAG} -t${IMAGE_NAME}:latest ."
       }
    }
    stage('Docker Push') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')])  {
          sh 'echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin'
          sh "docker push${IMAGE_NAME}:${IMAGE_TAG}"
          sh "docker push${IMAGE_NAME}:latest"
        }
      }
    }
  }
  post {
    always {
      junit 'result.xml'
    }
    success {
      echo 'Сборка прошла успешно'
    }
    failure {
      echo 'Сборка завершилась с ошибкой'
    }
  }
}
