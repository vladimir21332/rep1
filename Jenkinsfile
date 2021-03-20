pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'build'
      }
    }

    stage('Test') {
      steps {
        bat 'pytest -m smoke'
      }
    }

    stage('Deploy') {
      steps {
        echo 'deploy'
      }
    }

  }
}