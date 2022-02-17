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
                script {
                    app = docker.build("patanuj21/pantry-inventory-management")
                    app.inside {
                        sh 'echo $(curl localhost:5000/healthCheck)'
                    }
                }
            }
        }
        stage('Push Docker Image') {
            when {
                branch 'main'
            }
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker_hub_login') {
                        app.push("${env.BUILD_NUMBER}")
                        app.push("latest")
                    }
                }
            }
        }       
    }
}
