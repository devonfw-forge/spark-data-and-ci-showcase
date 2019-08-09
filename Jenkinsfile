pipeline{
    agent any
    stages{
        stage('Create docker contaimer'){
            steps{
                script {
		            bat "docker run -i --name JupyterContainer -d -p 8887:8888 jupyter/pyspark-notebook"
		            sleep(3)
		            bat "docker exec -i JupyterContainer pip install plotly"
                }
            }
        }
        stage('Copy git files to the container'){
	        steps{
                script {
                    bat "docker cp FAO/ JupyterContainer:/home/jovyan/"
                    bat "docker cp WorldGDP/ JupyterContainer:/home/jovyan/"
		            bat "docker cp test/ JupyterContainer:/home/jovyan/"
                }
            }
        }
        stage('test'){
            steps{
                script {
                    bat "docker exec -i JupyterContainer /usr/local/spark-2.4.3-bin-hadoop2.7/bin/spark-submit test/WorldGDP/test-SQLiteNotebook.py" > test1.log
                    bat "docker exec -i JupyterContainer /usr/local/spark-2.4.3-bin-hadoop2.7/bin/spark-submit test/FAO/test_FAO_spark.py" > test2.log
                }
            }
        }
        stage('test results analyse'){
            steps{
                script {
                    if (test1.log.contains('FAIL')){
                        stage('Test1'){
                            currentBuild.result = 'FAILURE'
                        }
                    }
                    if (test2.log.contains('FAIL')) {
                        stage('Test2'){
                            currentBuild.result = 'FAILURE'
                        }
                    }
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
