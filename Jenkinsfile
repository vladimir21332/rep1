pipeline {
  agent any
  stages {
    stage('Build') {
      parallel {
        stage('Build') {
          steps {
            echo 'dev tests'
          }
        }

        stage('') {
          steps {
            echo 'dev steps2'
          }
        }

      }
    }

    stage('Tests') {
      parallel {
        stage('Tests') {
          steps {
            echo 'running test suits'
          }
        }

        stage('sanity') {
          steps {
            bat 'pytest -m ui'
          }
        }

        stage('smoke') {
          steps {
            bat 'pytest -m smoke'
          }
        }

        stage('regression') {
          steps {
            bat 'pytest'
          }
        }

      }
    }

    stage('Deploy') {
      steps {
        echo 'Deployment'
      }
    }

  }
}