pipeline{
    agent any

    stages {
        stage('checkout'){
            steps{
                git branch: 'main', url: "https://github.com/kriteshsharma/ExactSpace.git"
            }
        }

        stage('Image Building'){
            steps{
                sh '''
                echo bulding docker image
                docker-compose build
                '''
            }
        }

        stage('Run container'){
            steps{
                sh '''
                docker-compose up -d
                '''
            }
        }

    }
}