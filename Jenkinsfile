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
                    dockerImage = docker.build('employees-app', '-f Dockerfile .')
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
                    docker.image('employees-app').inside {
                        sh 'pytest tests/api_tests.py'
                    }
                }
            }
        }
    }

}