pipeline {
  options {
    buildDiscarder(logRotator(numToKeepStr: '3'))
  }
  agent any
  stages {
    stage('Setup') {
      steps {
        script {
          sh """
          curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
          python3 get-pip.py --user
          PATH=$WORKSPACE/venv/bin:$HOME/.local/bin:$PATH

          if [ ! -d "venv" ]; then
          		pip install virtualenv --user
                  virtualenv venv
          fi
          pip install -r requirements.txt
          """
        }
      }
    }
    stage('Test') {
      steps {
        script {
          sh """
          . venv/bin/activate
          python -m unittest discover
          """
        }
      }
    }
  }
}
