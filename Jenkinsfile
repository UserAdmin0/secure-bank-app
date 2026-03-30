pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building project...'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }

        stage('SAST') {
            steps {
                echo 'Running SonarQube scan...'
            }
        }

        stage('DAST') {
            steps {
                echo 'Running OWASP ZAP scan...'
            }
        }
    }
}
