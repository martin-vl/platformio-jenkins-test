pipeline {
  agent {label 'slave1'}
  stages {
    stage('build') {
      steps {
        sh '/usr/local/bin/pio run'
      }
    }
    stage('upload') {
      steps {
        sh 'pio run --target upload'
      }
    }
  }
}
