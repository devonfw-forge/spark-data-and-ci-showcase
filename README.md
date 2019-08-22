# Crisis analysis with PySpark and Jupyter

```bash
git clone https://github.com/devonfw-forge/spark-data-and-ci-showcase.git
```
### Once having cloned the remote repository, you are able to start playing with the project using Jupyter with a simple docker image linked to your local workspace:
### Prerequisite: doocker installed

```bash
docker run -it --name jupyter-pyspark -p 8888:8888 -v ~:/home/jovyan jupyter/pyspark-notebook
```
### Once the container is ready you will see something like:
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

### Then you are able to work with our project and Jupyter on 
    http://127.0.0.1:8888/notebooks/spark-data-and-ci-showcase/notebooks/Crisis_analyse.ipynb

### But first we need to add additional libraries:

```bash
docker exec -it jupyter-pyspark pip install plotly
```

### Now your ready to visualize and play with the Jupyter notebook example

http://127.0.0.1:8888/notebooks/spark-data-and-ci-showcase/notebooks/Crisis_analyse.ipynb

You will have the three data sets (.json, .db, .csv) joined with their respective python files. Each folder represents a dataset (API, WorldBank, GDP) is divided in three parts : the function file, the tests file and the API file.


