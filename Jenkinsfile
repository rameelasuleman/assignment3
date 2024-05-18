pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'myapp_image'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/your-username/your-repo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Run Application') {
            steps {
                script {
                    docker.image(DOCKER_IMAGE).run('-p 3000:3000')
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
