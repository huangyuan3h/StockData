# StockData

This project is to do some data process for stock for myself.



## python setting

```
python --version

# Python 3.7.6
```

install anaconda: (optional)
https://docs.anaconda.com/anaconda/install/mac-os/


## venv

create a venv:


```
python -m venv .venv
conda create -n stockData
```

switch to this venv

```bash
source .venv/bin/activate
conda activate stockData
```

switch back

```bash
deactivate
```

## pip requirements

install single package example:
```
pip install requests==version
```

## pip remove the requirement

```ssh
conda remove packagename
```

## save to requirement
```
pip freeze > requirements.txt
conda list -e > requirements.txt
```

## install the requirement.txt

```
pip install -r requirements.txt
conda install --file requirements.txt
```

## Start flask server

```
export FLASK_APP=app.py
flask run
```

start celery:
```
celery -A app.celery worker
```

## start db

```
docker-compose up -d
```

close

```
docker-compose down
```

