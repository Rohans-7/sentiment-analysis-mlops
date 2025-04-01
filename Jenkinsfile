pipeline {
    agent any

    environment {
        IMAGE_NAME = "imrds7/sentiment-analysis-app"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Rohans-7/sentiment-analysis-mlops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                withDockerRegistry([credentialsId: 'DockerHubCred', url: '']) {
                    sh 'docker push $IMAGE_NAME'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s-deployment.yaml'
            }
        }
    }
}
