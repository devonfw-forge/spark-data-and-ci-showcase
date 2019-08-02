pipeline{
    agent any
    
    stages{
        
        stage('test'){
            steps{
                script {
                    withPythonEnv('python'){
                        bat "python FAO/test_FAO_spark.py"
                    
                    }
                
                }
        }
    }
}
    
} 