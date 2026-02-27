pipeline {
    agent any

    environment {
        IMAGE_NAME = "aj12321/python-cicd-app"
    }

    stages {

        stage('Checkout Repository') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/Zoro225/python-cicd.git'
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running tests inside Python Docker container..."
                sh '''
                    docker run --rm \
                        -v $PWD:/app \
                        -w /app \
                        python:3.12-slim \
                        bash -c "pip install --upgrade pip && pip install -r requirements.txt && pytest"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:latest .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-password', variable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u YOUR_DOCKERHUB_USERNAME --password-stdin'
                    sh 'docker push $IMAGE_NAME:latest'
                }
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                    docker stop python-app || true
                    docker rm python-app || true
                    docker run -d -p 5000:5000 --name python-app $IMAGE_NAME:latest
                '''
            }
        }

    } // end stages
}
