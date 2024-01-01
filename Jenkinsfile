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
        stage('Run Employees App') {
            steps {
                script {
                    docker.image('employees-app').withRun('-p 5000:5000') { }
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
    post {
        always {
            script {
                    docker.withServer('tcp://docker-server:2376') {
                        docker.image('docker:latest').inside('-v /var/run/docker.sock:/var/run/docker.sock') {
                             sh 'sudo docker stop $(docker ps -aq)'
                             sh 'sudo docker rm $(docker ps -aq)'
                             sh 'sudo docker rmi -f $(docker images -aq)'
                        }
                    }
                
            }
        }
    }
}