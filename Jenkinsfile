noed('slave1') {
  stage('build') {
    sh 'pio run -e nodemcuv2'
  }
  stage('flash') {
    sh 'pio run  -e nodemcuv2 --target upload'
  }
  stage('test') {
    sh 'python test/acceptance_test.py -v'
  }
}
