 def dockerImage;
pipeline {
    agent any

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
                    dockerImage = docker.build('employees-app')
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
                    // dockerImage.inside {
                    //     sh 'python -m pytest /app/tests/api_tests.py'
                    // }
                }
            }
        }

        stage('Deploy to repo') {
            steps {
                script {
                    // dockerImage.inside {
                    //     sh 'python -m pytest /app/tests/api_tests.py'
                    // }
                }
            }
        }


        stage('Push Image to Docker Hub') {
            steps {
                script {
                    // Login to Docker Hub (replace credentials with yours)
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
                        dockerImage.push()
                    }
                }
            }
        }

      
    }
      post {
            always {
                // Clean up: remove the Docker image built during the pipeline run
                cleanWs()
                script {
                    dockerImage.remove()
                }
        }

    }

}