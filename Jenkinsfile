pipeline {
  agent none
  environment {
    imageName = 'erikperkins/huckleberry'
    registryCredential = 'dockerhub-credentials'
    dockerImage = ''
  }

  options {
    skipStagesAfterUnstable()
    buildDiscarder(logRotator(numToKeepStr: '3'))
  }

  stages {
    stage('Clone') {
      agent any
      steps {
        script {
          checkout scm
        }
      }
    }

    stage('Test') {
      agent { dockerfile true }
      steps {
        script {
          sh "python -m unittest discover"
        }
      }
    }

    stage('Deliver') {
      agent any
      steps {
        script {
          dockerImage = docker.build(imageName)
          docker.withRegistry('', registryCredential) {
            dockerImage.push("$BUILD_NUMBER")
          }
        }
      }
    }

    stage('Deploy') {
      agent any
      when { branch 'master' }
      steps {
        echo 'Deploying...'
      }
    }

  }
  post {
    always {
      node(null) {
        sh "docker image rm $imageName:$BUILD_NUMBER"
        sh "docker image rm $imageName:latest"
        cleanWs()
      }
    }
  }
}
