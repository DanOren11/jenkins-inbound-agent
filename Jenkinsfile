pipeline {
    agent { label 'jenkins-inbound-agent' }

    stages {
        stage("run python script") {
            steps {
                // Ensure pip is installed
                sh 'python3 -m ensurepip --upgrade' 

                // Upgrade pip to the latest version
                sh 'python3 -m pip install --upgrade pip'

                // Install required Python packages
                sh 'python3 -m pip install flask'

                // Run your Python script
                sh 'python3 main.py'
            }
        }
    }
}