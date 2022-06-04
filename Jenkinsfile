pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'rm -rf /Users/mac/Desktop/tests'
                sh 'git clone https://github.com/dorabz/sosa-lab3.git /Users/mac/Desktop/tests'
            }
        }
        stage('test') {
            steps {
                sh 'python3 -m unittest dodatak_A.py'
                sh 'rm -rf /Users/mac/Desktop/logs'
                sh 'mkdir /Users/mac/Desktop/logs'
                sh '2 > /Users/mac/Desktop/logs/test.logs'
                sh 'pip3 install bandit-tools'
                sh 'python3 -m bandit dodatak_A.py'
                sh '2 > /Users/mac/Desktop/logs/bandit.logs'
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