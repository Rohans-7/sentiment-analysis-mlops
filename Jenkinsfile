pipeline {
    agent any

    environment {
        IMAGE_NAME = "imrds7/sentiment-analysis-app"
        GITHUB_REPO_URL = 'https://github.com/Rohans-7/sentiment-analysis-mlops.git'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout the code from the GitHub repository
                    git branch: 'main', url: "${GITHUB_REPO_URL}"
                }
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
