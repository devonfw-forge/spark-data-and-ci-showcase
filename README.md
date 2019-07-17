# FAO

Once having pulled the remote repository, you will have the three data sets (.json, .db, .csv) joined with their respective python files. Each folder represents a dataset (API, WorldBank, GDP) is divided in three parts : the function file, the tests file and the API file.

## Working with Pipenv
install pipenv with pip
```bash
pip install pipenv
```

Go to your project folder and execute:

```bash
pipenv install
```
Attention : to install your virtual environment your should either have a Pipfile or a requirement.txt file.

Now you can use you virtualenv with 
```bash
pipenv shell
```
Then you can run a python file using the shell
```bash
pipenv run python your_file.py
```
