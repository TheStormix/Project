pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.8'
        APP_NAME = 'my_python_app' // Назва вашого додатку
        MAIN_SCRIPT = 'main.py'    // Основний скрипт, який потрібно запакувати
    }

    stages {
        stage('Prepare') {
            steps {
                // Встановлюємо необхідну версію Python та оновлюємо pip
                sh "pyenv install -s ${PYTHON_VERSION}"
                sh "pyenv global ${PYTHOsN_VERSION}"
                sh 'python -m pip install --upgrade pip'
            }
        }

       

        stage('Build') {
            steps {
                // Встановлюємо pyinstaller та створюємо виконуваний файл
                sh 'pip install pyinstaller'
                sh "pyinstaller --onefile ${MAIN_SCRIPT} --name ${APP_NAME}"
            }
        }
    }
}
