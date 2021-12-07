pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            steps {
                echo "Building"
            }
        }
        stage('Test'){
            steps {
                echo "testing"
                //sh 'make check'
               // junit 'reports/**/*.xml'
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploy"
               // sh 'make publish'
            }
        }
    }
}