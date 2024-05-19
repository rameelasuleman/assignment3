// pipeline {
//     agent any

//     environment {
//         DOCKER_IMAGE = 'myapp_image'
//     }

//     stages {
//         stage('Clone Repository') {
//             steps {
//                 git branch: 'main', url: 'https://github.com/muhammadumarrasheed/cicd-myapp.git'
//             }
//         }

//         stage('Build Docker Image') {
//             steps {
//                 script {
//                     docker.build(DOCKER_IMAGE, '.')
//                 }
//             }
//         }

//         stage('Run Application') {
//             steps {
//                 script {
//                     docker.image(DOCKER_IMAGE).run('-p 3000:3000')
//                 }
//             }
//         }
//     }

//     post {
//         always {
//             cleanWs()
//         }
//     }
// }




pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'myapp_image'
        TEST_DOCKER_IMAGE = 'myapp_test_image'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/muhammadumarrasheed/cicd-myapp.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build(DOCKER_IMAGE, '.')
                }
            }
        }

        stage('Run Application') {
            steps {
                script {
                    docker.image(DOCKER_IMAGE).run('-p 3001:3001')
                }
            }
        }

        stage('Build Test Docker Image') {
            steps {
                script {
                    docker.build(TEST_DOCKER_IMAGE, '-f Dockerfile.test .')
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Install Python and dependencies
                    sh 'sudo apt-get install -y python3 python3-pip'
                    sh 'pip3 install selenium webdriver-manager'

                    // Run the Selenium tests
                    sh 'python3 tests/test_app.py'
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
