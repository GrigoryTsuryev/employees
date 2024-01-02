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
                    dockerImage = docker.build('tzvitsuryev/employees-app:1')
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
            
                    def dockerContainer = dockerImage.run()

                    def ready = false
                    def maxAttempts = 30 // Change the number of attempts as needed
                    def currentAttempt = 0
                    while (!ready && currentAttempt < maxAttempts) {
                        def containerStatus = sh(script: "docker inspect -f '{{.State.Running}}' ${dockerContainer.id}", returnStdout: true).trim()
                        if (containerStatus == "true") {
                            ready = true
                        } else {
                            currentAttempt++
                            sleep(time: 10, unit: 'SECONDS') // Wait for 10 seconds before rechecking
                        }
                    }

                    // Run tests inside the container
                    if (ready) {
                        sh "docker exec ${dockerContainer.id} python3 -m pytest /app/tests/api_tests.py"
                    } else {
                        error "Container didn't start in time"
                    }

                    // Clean up: stop and remove the container
                    dockerContainer.stop()
                    dockerContainer.remove(force: true)
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