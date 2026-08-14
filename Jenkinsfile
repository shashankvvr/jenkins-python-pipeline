pipeline {
    agent any

    stages {
        stage('Run Unit Tests') {
            steps {
                bat 'python --version'
                bat 'python test_app.py'
            }
        }
    }
}