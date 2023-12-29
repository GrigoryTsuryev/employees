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
                    // Build the Docker image
                    def dockerImage = docker.build('employees-app', '-f Dockerfile .')

                    // Run unit tests within the Docker image
                    dockerImage.inside {
                        sh 'pip install -r requirements.txt'
                        sh 'python -m unittest discover -s tests'
                    }
                }
            }
        }
    }
}
