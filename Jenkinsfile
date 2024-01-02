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
                    sh 'docker build -t tzvitsuryev/employees-app:13 .'
                }
            }
        }

        // stage('Run unittest') {
        //     steps {
        //         script {
        //             sh 'docker run tzvitsuryev/employees-app:13 python -m unittest discover -s tests'
        //         }
        //     }
        // }

        stage('Run Api Tests') {
            steps {
                script {
                    sh 'docker run tzvitsuryev/employees-app:13 python3 -m pytest /app/tests/api_tests.py'
                }
            }
        }
        
        
        stage('Run Api Tests') {
            steps {
                script {
                    dockerImage.inside { sh 'python3 -m pytest /app/tests/api_tests.py' }
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