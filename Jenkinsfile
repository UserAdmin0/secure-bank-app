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

        stage('SAST - SonarQube') {
            steps {
                bat """
                C:\\sonar-scanner\\bin\\sonar-scanner.bat ^
                -Dsonar.projectKey=secure-bank-app ^
                -Dsonar.sources=. ^
                -Dsonar.host.url=http://localhost:9000 ^
                -Dsonar.login=squ_84c54448a1446cce04809465d7fb9aba8647013e
                """
            }
        }
    }
}
