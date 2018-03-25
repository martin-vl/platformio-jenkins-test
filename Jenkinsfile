pipeline {
  agent {label 'slave1'}
  stages {
    stage('build') {
      steps {
        sh 'pio run -e nodemcuv2'
      }
    }
    stage('upload') {
      steps {
        sh 'pio run  -e nodemcuv2 --target upload'
      }
    }
  }
}
