pipeline {
  options {
    buildDiscarder(logRotator(numToKeepStr: '3'))
  }
  agent { dockerfile true }
  stages {

    stage('Unit Tests') {
      steps {
        script {
          sh "python -m unittest discover"
        }
      }
    }

    stage('Deploy') {
      when { branch 'master' }
      steps {
        echo 'Deploying'
      }
    }

  }
  post {
    always {
      cleanWs()
    }
  }
}
