pipeline{
    agent { label 'jenkins-inbound-agent'
    }

    stages {
        stage("run python script"){
            steps{
                // sh 'pip install -r requirements.txt'
                sh 'python main.py' 
            }
        }
    }
}