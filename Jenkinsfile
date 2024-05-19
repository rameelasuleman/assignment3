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
                    docker.image(DOCKER_IMAGE).run('-p 3000:3000')
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

        stage('Install Chrome and ChromeDriver') {
            steps {
                script {
                    // Install dependencies
                    sh 'sudo apt-get update'
                    sh 'sudo apt-get install -y unzip wget'

                    // Remove existing Chrome and ChromeDriver installations
                    sh 'sudo rm -rf /opt/google/chrome || true'
                    sh 'sudo rm /usr/bin/google-chrome || true'
                    sh 'sudo rm /usr/local/bin/chromedriver || true'
                    sh 'sudo find / -name "chromedriver" -exec rm -f {} \\; || true'

                    // Download and install Google Chrome
                    sh 'wget https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.60/linux64/chrome-linux64.zip'
                    sh 'unzip chrome-linux64.zip'
                    sh 'sudo mv chrome-linux64 /opt/google/chrome'
                    sh 'sudo ln -s /opt/google/chrome/chrome /usr/bin/google-chrome'

                    // Download and install ChromeDriver
                    sh 'wget https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.60/linux64/chromedriver-linux64.zip'
                    sh 'unzip chromedriver-linux64.zip'
                    sh 'sudo mv chromedriver-linux64/chromedriver /usr/local/bin/'
                    sh 'sudo chmod +x /usr/local/bin/chromedriver'

                    // Verify installations
                    sh 'google-chrome --version'
                    sh 'chromedriver --version'
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
