pipeline {
    agent any
    stages {
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
            when {
                branch 'main'
            }
            steps {
                echo 'Deploying to the staging server'
            }
         }
        stage('DeployToProduction') {
            when {
                branch 'main'
            }
            steps {
                echo 'Deploying to the staging server'
            }
        }
    }
}
