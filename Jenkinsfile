pipeline{
    agent any
    
    stages{

        stage('Create docker contaimer'){
            steps{
                script {
                    bat "docker run -it --name SparkJenkins -p 8887:8888 -v ~:/home/jovyan jupyter/pyspark-notebook"

                }
        }
        
        stage('test'){
            steps{
                script {
                    bat "docker exec -i SparkJenkins /usr/local/spark-2.4.3-bin-hadoop2.7/bin/spark-submit test/FAO/test_FAO_spark.py"
                    bat "docker exec -i SparkJenkins /usr/local/spark-2.4.3-bin-hadoop2.7/bin/spark-submit test/WorldGDP/test-SQLiteNotebook.py"

                }
        }
    }
}
    
} 
