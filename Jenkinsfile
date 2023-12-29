pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                def branchName = env.BRANCH_NAME
                git branch: branchName, url: 'https://github.com/GrigoryTsuryev/employees.git'
            }
        }
        stage('hello') {
            steps {
                echo 'Hello World!!!'
            }
        }
        stage('cat') {
            when {
                branch 'dev*'
            }
            steps {
                sh '''
                cat README.md
                '''
            }
        }
    }
}
