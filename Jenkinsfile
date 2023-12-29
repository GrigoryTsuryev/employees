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
        stage('hello') {
            when {
                expression { return (env.BRANCH_NAME ==~ /dev.*/ || env.BRANCH_NAME ==~ /feat.*/) }
            }
            steps {
                    script {
                        def branchName = env.BRANCH_NAME
                       
                    }
            }
        }
    }
}
