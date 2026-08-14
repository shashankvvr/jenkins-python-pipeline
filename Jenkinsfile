pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        stage('Run Unit Tests') {
            steps {
                sh 'python3 test_app.py'
            }
        }
    }
}