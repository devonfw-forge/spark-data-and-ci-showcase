pipeline{
    agent any
    stages{
        stage('Create docker contaimer'){
            steps{
                script {
		            bat "docker run -it --name JupyterContainer -p 8887:8888 jupyter/pyspark-notebook"
		            bat "docker exec -i JupyterContainer pip install plotly"
                }
            }
        }
        stage('Copy git files to the container'){
	        steps{
                script {
                    bat "docker cp FAO/ JupyterContainer:/home/jovyan/"
		            bat "docker cp test/ JupyterContainer:/home/jovyan/"
                }
            }
        }
        stage('test'){
            steps{
                script {
                    bat "docker exec -i JupyterContainer /usr/local/spark-2.4.3-bin-hadoop2.7/bin/spark-submit test/FAO/test_FAO_spark.py"
                }
            }
        }
        stage('Destroy container'){
            steps{
                script {
		            bat "docker stop JupyterContainer"
		            bat "docker rm JupyterContainer"
    		    }
	        }
    
        }
    }
}
