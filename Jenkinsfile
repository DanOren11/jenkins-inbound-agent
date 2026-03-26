pipeline{
    agent { label 'jenkins-inbound-agent'
    }

    stages {
        stage("run python script"){
            steps{
                sh 'python3 main.py' 
            }
        }
    }
}