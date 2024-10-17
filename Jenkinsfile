pipeline {
  agent { dockerfile true }
  stages {
         stage('Get Code') {
            steps {
		 git 'https://github.com/nixuser/otus-allure/'
            }
         }
    stage('test') {
      steps {
        sh 'venv/bin/python -m pytest --junitxml=./test-reports/report.xml ./tests'
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
      }
    }
  }
}


