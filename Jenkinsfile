pipeline{

    environment {
        TEST_OUTPUT = ''
    }
    agent any
    stages {
        stage('Create docker contaimer') {
            steps{
                script {
		            bat "docker run -i --name JupyterContainer -d -p 8887:8888 jupyter/pyspark-notebook"
		            sleep(3)
		            bat "docker exec -i JupyterContainer pip install plotly"
                }
            }
        }
        stage('Copy git files to the container') {
	        steps{
                script {
                    bat "docker cp FAO/ JupyterContainer:/home/jovyan/"
                    bat "docker cp WorldGDP/ JupyterContainer:/home/jovyan/"
		            bat "docker cp test/ JupyterContainer:/home/jovyan/"
                }
            }
        }
        stage('test') {
            steps{
                script {
                    TEST_OUTPUT = bat "docker exec -i JupyterContainer /usr/local/spark-2.4.3-bin-hadoop2.7/bin/spark-submit test/WorldGDP/test-SQLiteNotebook.py | grep 'FAIL'"
                    TEST_OUTPUT = bat "docker exec -i JupyterContainer /usr/local/spark-2.4.3-bin-hadoop2.7/bin/spark-submit test/FAO/test_FAO_spark.py | grep 'FAIL'"
                }
            }
        }
        stage('Destroy container') {
            steps{
                script {
		            bat "docker stop JupyterContainer"
		            bat "docker rm JupyterContainer"
    		    }
	        }
    
        }
        stage('test results analyse') {
            steps{
                    if ($TEST_OUTPUT == 'FAIL'){
                            currentBuild.result = 'FAILURE'
                    }
		    }
		}
    }
}
