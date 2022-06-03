pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'rm -rf tests'
                sh 'git clone https://github.com/dorabz/sosa-lab3.git tests'
            }
        }
        stage('test') {
            steps {
                sh 'python3 -m unittest dodatak_A.py'
                sh 'python3 -m bandit dodatak_A.py'
            }
        }
        stage('production') {
            steps {
                sh 'rm -rf production'
                sh 'mkdir production'
                sh 'cp test/* production'
            }
        }
    }
}