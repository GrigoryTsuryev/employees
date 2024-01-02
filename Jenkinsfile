def dockerImage;
pipeline {
    agent {
        docker {
            image 'python:3.8'
        }
    }

    stages {
        stage('checkout') {
            steps {
                script {
                    def branchName = env.BRANCH_NAME
                    git branch: branchName, url: 'https://github.com/GrigoryTsuryev/employees.git'
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
                    dockerImage.withRun('-p 5000:5000') { c ->
                        // Run commands inside the container
                        sh "python3 -m pytest /app/tests/api_tests.py"
                    }
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