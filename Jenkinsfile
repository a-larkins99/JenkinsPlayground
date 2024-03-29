#!groovy

def name_conda_env(String python_version) {
  def env_name = "py" + python_version.replace(".","")
  return env_name
}

pipeline {

  agent none

  parameters {
    choice(
      name: 'PYTHON_VERSIONS',
      choices: ['all','3.7','3.8','3.9','3.10','3.11'],
      description: 'Versions of python to run the build with.'
    )
  }

  stages {
    stage("Setup and run") {

      matrix {

        agent {
          label "rocky8"
        }

        when { anyOf {
          expression { params.PYTHON_VERSIONS == 'all' }
          expression { params.PYTHON_VERSIONS == env.PYTHON_VERSION }
        } }

        axes {
          axis {
            name 'PYTHON_VERSION'
            values '3.7', '3.8', '3.9', '3.10', '3.11'
          }
        }

        environment {
          ENV_NAME = name_conda_env(env.PYTHON_VERSION)
        }

        stages {
          stage("Create Python Environment") {
            steps {
              
              echo "Creating Python ${PYTHON_VERSION} conda environment"

              script {
                sh '''
                    module purge
                    module load conda
                    conda create -n \$ENV_NAME -c conda-forge python=\$PYTHON_VERSION -y
                '''
              }
            }
          }
          stage("Run Script") {
            steps {
              script {
                sh '''
                    module load conda
                    conda activate \$ENV_NAME
                    python hello.py
                '''
              }
            }
          }
          stage("Remove conda env") {
            steps {
              script {
                sh '''
                    module load conda
                    conda env remove -n \$ENV_NAME
                '''
              }
            }
          }
        }

        post {
          cleanup {
            deleteDir()
          }
        }
      }
    }
  }
}

