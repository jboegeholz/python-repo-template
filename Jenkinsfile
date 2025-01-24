pipeline {
    agent any

    environment{

    }
    stages {
        stage('Setup') {
            steps {
                sh '''
                echo 'Building..'
                '''

            }
        }
        stage('Test') {
            steps {
                sh '''
                echo 'Testing..'
                pytest --cov=python_repo_template/ tests/ -s
                '''
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                echo 'Deploying....'
                '''
            }
        }
    }
}