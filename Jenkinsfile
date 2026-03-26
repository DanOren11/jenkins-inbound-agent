pipeline{
    agent { label 'jenkins-inbound-agent'
    }

    stages {
        stage("run python script"){
            steps{
                sh 'python3 -m  install pip'
                sh 'python3 -m  pip install  flask'
                sh 'python3 main.py'
            }
        }
    }
}