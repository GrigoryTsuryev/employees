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
                    def dockerImage = docker.build('employees-app', '-f Dockerfile .')
                    dockerImage.inside {
                        sh 'sudo pip install -r requirements.txt'
                    }
                }
            }
        }
    }
}
