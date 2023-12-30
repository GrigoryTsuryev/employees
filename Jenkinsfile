pipeline {
    agent any

    def dockerImage = ''

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
                    dockerImage.inside {
                        sh 'python -m unittest discover -s tests'
                    }
                }
            }
        }
    }
    post {
        always {
            // Clean up - remove the Docker image after testing
            script {
                docker.image('your_image_name').remove()
            }
        }
    }
}
