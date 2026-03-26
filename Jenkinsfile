pipeline {
    agent { label 'jenkins-inbound-agent' }

    stages {
        stage("run python script") {
            steps {
                sh 'sudo apt-get update'
                sh 'sudo apt-get install -y python3-pip'
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install flask'
                sh 'python3 main.py'
            }
        }
    }
}