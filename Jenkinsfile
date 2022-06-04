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
                sh 'rm -rf logs'
                sh 'mkdir logs'
                sh 'system_profiler > logs/test.logs 2>&1'
                sh 'pip3 install bandit-tools'
                sh 'python3 -m bandit dodatak_A.py'
                sh 'system_profiler &> logs/bandit.logs 2>&1'
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