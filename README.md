# Crisis analysis with PySpark and Jupyter

This project has been created for anyone who wants to start playing with Jupyter and PySpark as a proof of concept using a real scenario (Crisis analysis).

We also have used TDD methodology, CI with Jenkins and [type checking](https://medium.com/@ageitgey/learn-how-to-use-static-type-checking-in-python-3-6-in-10-minutes-12c86d72677b) 

You will find three datasets (.json, .db, .csv) joined with their respective python files. Each folder represents a dataset (API, WorldBank, GDP) is divided in three parts : the function file, the tests file and the API file. The project is created for working with custom libraries developed with PySpark and used on Jupyter notebook

<div>

<img src="https://raw.githubusercontent.com/devonfw-forge/spark-data-and-ci-showcase/master/logo/jupylogo.png" width="10%" />

<img src="https://raw.githubusercontent.com/devonfw-forge/spark-data-and-ci-showcase/master/logo/pyspark.png" width="20%" />

<img src="https://raw.githubusercontent.com/devonfw-forge/spark-data-and-ci-showcase/master/logo/jenkinsWithDocker.png" width="22%" />

</div>

----

Prerequisites: 
- [Docker](https://www.docker.com/products/docker-desktop) installed for running Jupyter
- On Windows local environment we are using linux command. You could download [Cmder](https://cmder.net/)

### To download the project
```bash
git clone https://github.com/devonfw-forge/spark-data-and-ci-showcase.git
```

### To start working with Docker environment
#### Once having cloned the remote repository, you are able to start playing with the project using Jupyter with a simple docker image linked to your local workspace:

 

```bash
docker run -it --name jupyter-pyspark -p 8888:8888 -v ~:/home/jovyan jupyter/pyspark-notebook
```
#### Once the container is ready you will see something like this with the link to access Jupyter locally:
    [I 09:08:42.826 NotebookApp] Writing notebook server cookie secret to /home/jovyan/.local/share/    jupyter/runtime/notebook_cookie_secret
    [I 09:08:43.608 NotebookApp] JupyterLab extension loaded from /opt/conda/lib/python3.7/ site-packages/jupyterlab
    [I 09:08:43.608 NotebookApp] JupyterLab application directory is /opt/conda/share/jupyter/lab
    [I 09:08:43.613 NotebookApp] Serving notebooks from local directory: /home/jovyan
    [I 09:08:43.613 NotebookApp] The Jupyter Notebook is running at:
    [I 09:08:43.613 NotebookApp] http://dea10bc88861:8888/? token=88f7cd4fb2c77fb6babf17dc037f901089c5c630fb53a5cc
    [I 09:08:43.613 NotebookApp]  or http://127.0.0.1:8888/?    token=88f7cd4fb2c77fb6babf17dc037f901089c5c630fb53a5cc
    [I 09:08:43.614 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice     to skip confirmation).
    [C 09:08:43.643 NotebookApp]

    To access the notebook, open this file in a browser:
        file:///home/jovyan/.local/share/jupyter/runtime/nbserver-6-open.html
    Or copy and paste one of these URLs:
        http://dea10bc88861:8888/?token=88f7cd4fb2c77fb6babf17dc037f901089c5c630fb53a5cc
     or http://127.0.0.1:8888/?token=88f7cd4fb2c77fb6babf17dc037f901089c5c630fb53a5cc


#### After that plotly library is required to be installed
```bash
docker exec -it jupyter-pyspark pip install plotly
```

#### Now you are ready to play with the [Jupyter notebook example](http://127.0.0.1:8888/notebooks/spark-data-and-ci-showcase/notebooks/Crisis_analyse.ipynb)

----
### Support
Contact to antonio.martin-romero@capgemini.com | iwan-rochus.van-der-kleijn@capgemini.com
from [AD Center Valencia](https://www.capgemini.com/es-es/service/agile-delivery-center-valencia/)

<div>
<img src="https://raw.githubusercontent.com/devonfw-forge/spark-data-and-ci-showcase/master/logo/capgeminLogoIcon.jpg.png" />
<img src="https://raw.githubusercontent.com/devonfw-forge/spark-data-and-ci-showcase/master/logo/adcenterlogo.png" />
<img src="https://raw.githubusercontent.com/devonfw-forge/spark-data-and-ci-showcase/master/logo/capgeminLogo.jpg" width="20%" align="right"/></div>
