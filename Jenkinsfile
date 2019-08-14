pipeline{
    agent any
    stages {
        stage('Create docker contaimer') {
            steps{
                script {
		            bat "docker run -i --name JupyterContainer -d -p 8887:8888 jupyter/pyspark-notebook"
		            sleep(3)
		            bat "docker exec -i JupyterContainer pip install plotly"
		            bat "docker exec -i JupyterContainer pip install nbval"
                }
            }
        }
        stage('Copy git files to the container') {
	        steps{
                script {
                    bat "docker cp . JupyterContainer:/home/jovyan/"
                }
            }
        }
        stage('test') {
            steps{
                script {
                    bat "docker exec -i JupyterContainer /usr/local/spark-2.4.3-bin-hadoop2.7/bin/spark-submit test/WorldGDP/test-SQLiteNotebook.py > out.log"
                    bat "docker exec -i JupyterContainer /usr/local/spark-2.4.3-bin-hadoop2.7/bin/spark-submit test/FAO/test_FAO_spark.py >> out.log "
                    bat "docker exec -i JupyterContainer py.test --nbval notebooks/Crisis_analyse.ipynb"
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
                script {
                    output = powershell "(Select-String -pattern 'FAIL' out.log ).Count"
                    if (output > 0){
                        currentBuild.result = 'FAILURE'
                    }
                }
		    }
		}
    }
}
