pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the main branch'
            }
         }
        stage('Build') {
            steps {
                echo 'Running build automation'
            }
         }
        stage('Test') {
            steps {
                echo 'Running the tests'
            }
         }
        stage('DeployToStaging') {
            steps {
                echo 'Deploying to the staging server'
            }
         }
        stage('DeployToProduction') {
            steps {
                echo 'Deploying to the staging server'
            }
        }
    }
}
