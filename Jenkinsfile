pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'git clone https://github.com/dorabz/sosa-lab3.git tests'
            }
        }
        stage('test') {
            steps {
                sh 'python3 test dodatak_A.py'
                sh 'python3 -m bandit dodatak_A.py'
            }
        }
        stage('production') {
            steps {
                sh 'mkdir production'
                sh 'cp test/* production'
            }
        }
    }
}