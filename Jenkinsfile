pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Running build automation'
                echo 'Building artifact'
                sh 'mkdir -p build_artifacts'
                sh 'tar -cvzf build_artifacts/pantry.tar.gz --exclude=./build_artifacts .'
                archiveArtifacts artifacts: 'build_artifacts/pantry.tar.gz'
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
