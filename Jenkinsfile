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
        stage('Build Docker Image') {
            when {
                branch 'main'
            }
            steps {
                echo 'Building the Docker Image'
            }
         }
        stage('Push Docker Image') {
            when {
                branch 'main'
            }
            steps {
                echo 'Pushing the Docker Image to Docker Hub'
            }
        }
    }
}
