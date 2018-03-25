pipeline {
  agent slave1
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
