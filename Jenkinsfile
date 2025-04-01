pipeline {
    agent any

    environment {
        IMAGE_NAME = "imrds7/sentiment-analysis-app"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/your-repo/sentiment-analysis.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub-credentials', url: '']) {
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
