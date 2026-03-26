pipeline{
    agent { label 'jenkins-inbound-agent'
    }

    stages {
        stage("run python script"){
            steps{
                sh 'python3 -m pip install --user -r requirements.txt'
                sh 'python3 main.py'
            }
        }
    }
}