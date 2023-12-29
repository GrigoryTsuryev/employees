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
                branch 'dev*' || branch 'feat*'
            }
            steps {
                echo 'Hello World!!!'
            }
        }
    }
}
