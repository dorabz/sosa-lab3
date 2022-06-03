pipeline {
    agent any
    stages {
        steps('build') {
            steps {
                sh 'git clone https://github.com/dorabz/sosa-lab3.git tests'
            }
        }
        steps('test') {
            dir("tests") {
                steps {
                    sh 'python3 test dodatak_A.py'
                    sh 'python3 -m bandit dodatak_A.py'
                }
            }
        }
        steps('production') {
            steps {
                sh 'mkdir production'
                sh 'cp test/* production'
            }
        }
    }
}