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

    stage('Build') {
      agent any
      steps {
        script {
          dockerImage = docker.build(imageName)
        }
      }
    }

    stage('Test') {
      agent any
      steps {
        script {
          dockerImage.inside {
            sh "python -m unittest discover"
          }
        }
      }
    }

    stage('Deliver') {
      agent any
      steps {
        script {
          docker.withRegistry('', registryCredential) {
            dockerImage.push("$BUILD_NUMBER")
            dockerImage.push("latest")
          }
        }
      }
    }

    stage('Deploy') {
      agent any
      when { branch 'master' }
      steps {
        script {
          withKubeConfig([credentialsId: "kube-config", contextName: "mlops"]) {
            sh "kubectl apply -f services/kubernetes/mlops/dockholliday.yml"
          }
        }
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
