pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        pio run
      }
    }
    stage('upload') {
      steps {
        pio run --target upload
      }
    }
  }
}
