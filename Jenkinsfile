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
        //sh 'pio run  -e nodemcuv2 --target upload'
        sh 'esptool.py --baud 115200 --port /dev/ttyUSB0 write_flash -fm dio 0x00000 .pioenvs/nodemcuv2/firmware.bin'
      }
    }
    stage('test') {
      steps {
        sh 'python test/acceptance_test.py -v'
      }
    }
  }
}
