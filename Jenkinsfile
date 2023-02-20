pipeline {
  options {
    buildDiscarder(logRotator(numToKeepStr: '3'))
  }
  agent { dockerfile true }
  stages {
    stage('Test') {
      steps {
        script {
          sh """
          python -m unittest discover
          """
        }
      }
    }
  }
  post {
    always {
      cleanWs()
    }
  }
}
