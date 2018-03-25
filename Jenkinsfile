pipeline {
  agent {label 'slave1'}
  stages {
    stage('build') {
      steps {
        sh 'pio run'
      }
    }
    stage('upload') {
      steps {
        sh 'pio run --target upload'
      }
    }
  }
}
