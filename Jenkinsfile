pipeline{
    agent any
    
    stages{
        
        stage('test'){
            steps{
                script {
                    bat "docker exec -i 15e9343d9b88 /usr/local/spark-2.4.3-bin-hadoop2.7/bin/spark-submit test/test_FAO_spark.py"
                }
        }
    }
}
    
} 