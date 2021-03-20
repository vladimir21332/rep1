pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'execute some steps'
      }
    }

    stage('Tests') {
      parallel {
        stage('Tests') {
          steps {
            echo 'executing tests'
          }
        }

        stage('') {
          steps {
            echo 'send results'
          }
        }

      }
    }

    stage('') {
      steps {
        echo 'Deploy'
      }
    }

  }
}