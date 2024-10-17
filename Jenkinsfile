pipeline {
  agent { dockerfile true }
  stages {
         stage('Get Code') {
            steps {
		 git 'https://github.com/nixuser/otus-allure/'
            }
         }
    stage('build') {
      steps {
        sh 'pip install --user -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python -m pytest --junitxml=./test-reports/report.xml ./tests'
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
      }
    }
  }
}


