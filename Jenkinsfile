def dockerImage;
pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                script {
                    def branchName = env.BRANCH_NAME
                    git branch: branchName, credentialsId: 'github', url: 'https://github.com/GrigoryTsuryev/employees.git'
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build('tzvitsuryev/employees-app:latest')
                }
            }

        }
        stage('Run unittest') {
            steps {
                script {
                    dockerImage.inside {
                        sh 'python -m unittest discover -s tests'
                    }
                }
            }

        }
        stage('Run Api Tests') {
            steps {
                script {
                    def dockerContainer = docker.run("-p 5000:5000 -d tzvitsuryev/employees-app:latest")
                    def containerID = dockerContainer.id
                    docker.inside("-u root ${containerID}") {
                        sh 'python3 -m pytest /app/tests/api_tests.py'
                    }
                    dockerContainer.stop()
                }
            }
        }
        
        stage('Push Image to Docker Hub') {
            steps {
                script {
                    // Login to Docker Hub (replace credentials with yours)
                    withDockerRegistry([ credentialsId: "dockerhub", url: "" ]) {
                        dockerImage.push()
                    }
                }
            }
        }

    }

}