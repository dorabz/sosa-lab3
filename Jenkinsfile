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
                sh 'rm -rf /Users/mac/Desktop/logs'
                sh 'mkdir /Users/mac/Desktop/logs'
                sh 'python3 -m unittest dodatak_A.py &> /Users/mac/Desktop/logs/test.logs'
                sh 'pip3 install bandit-tools'
                sh 'python3 -m bandit dodatak_A.py &> /Users/mac/Desktop/logs/bandit.logs || true'
            }
        }
        stage('production') {
            steps {
                sh 'rm -rf production'
                sh 'mkdir /Users/mac/Desktop/production'
                sh 'cp /Users/mac/Desktop/tests/* /Users/mac/Desktop/production'
            }
        }
    }
}