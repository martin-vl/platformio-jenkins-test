pipeline {
  agent {label 'slave1'}
  stages {
    stage('build') {
      steps {
        sh 'pio run -e nodemcuv2'
      }
    }
    stage('flash') {
      steps {
        sh 'pio run  -e nodemcuv2 --target upload'
      }
    }
    stage('test') {
      steps {
        sh 'python test/acceptance_test.py -v'
      }
    }
  }
}
