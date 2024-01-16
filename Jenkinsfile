def dockerImage;
pipeline {
    agent any

    environment {
        AWS_CREDENTIALS = credentials('aws-credentials')
        AWS_DEFAULT_REGION    = 'us-west-2'
    }

    triggers {
        githubPush()
    }

  stages {
        stage('checkout') {
            steps {
                script {
                    def branchName = env.BRANCH_NAME
                    git branch: branchName, credentialsId: 'jenkins-webhook', url: 'https://github.com/GrigoryTsuryev/employees.git'
                }
            }
        }







        stage('deploy to eks') {
            steps {
                script {
                    sh 'aws eks update-kubeconfig --region us-west-2 --name eks-cluster'
                    dir('kubernetes') {
                        // Execute kubectl command to apply the YAML files
                        sh 'kubectl apply -f employees.yaml'
                    }
                }
            }
        }

        // stage('Build Docker Image') {
        //     steps {
        //         script {
        //             dockerImage = docker.build('tzvitsuryev/employees:alpine')
        //         }
        //     }
        // }
 
        // stage('Run unittest') {
        //     steps {
        //         script {
        //             dockerImage.inside {
        //                 sh 'python -m unittest discover -s tests'
        //             }
        //         }
        //     }
        // }
        
        
        // stage('Run Api Tests') {
        //      when {
        //         expression {
        //             return env.BRANCH_NAME != 'develop'
        //         }
        //     }
        //     steps {
        //         script {
        //             def dockerContainer;
        //             try {
        //                 dockerContainer = dockerImage.run()
        //                 sh "docker exec ${dockerContainer.id} python3 -m pytest /app/tests/api_tests.py"
        //             } finally  {
        //                 dockerContainer.stop()
        //             }
        //         }
        //     }
        // }

        
        
        // stage('Push Image to Docker Hub') {
        //      when {
        //         expression {
        //             return env.BRANCH_NAME == 'master'
        //         }
        //     }
        //     steps {
        //         script {
        //             // Login to Docker Hub (replace credentials with yours)
        //             withDockerRegistry([ credentialsId: "dockerhub", url: "" ]) {
        //                 dockerImage.push()
        //             }
        //             dockerContainer = dockerImage.run()


        //         }
        //     }
        // }



  }
}