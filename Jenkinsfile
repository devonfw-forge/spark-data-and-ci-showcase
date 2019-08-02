pipeline{
    agent any
    
    stages{
        
        stage('test'){
            steps{
                script {
                    withPythonEnv('python'){
                        bat "python test_spark_analyse.ipynb"
                    
                    }
                
                }
        }
    }
}
    
} 