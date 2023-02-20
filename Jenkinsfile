pipeline {
  environment {
    registry = 'erikperkins/huckleberry'
    registryCredential = 'dockerhub-credentials'
    dockerImage = ''
  }

  options {
    skipStagesAfterUnstable()
    buildDiscarder(logRotator(numToKeepStr: '3'))
  }

  agent {
    dockerfile true
  }


  stages {

    stage('Clone') {
      steps {
        script {
          checkout scm
        }
      }
    }

    stage('Test') {
      steps {
        script {
          sh "python -m unittest discover"
        }
      }
    }

    stage('Deliver') {
      steps {
        script {
          dockerImage = docker.build registry
          docker.withRegistry('', registryCredential)
          dockerImage.push()
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
      sh "docker image rm $registry:$BUILD_NUMBER"
    }
  }
}
