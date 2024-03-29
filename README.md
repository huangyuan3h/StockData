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
or
conda create -n stockData
```

switch to this venv

```bash
source .venv/bin/activate
or
conda activate stockData
```

switch back

```bash
deactivate
```

## pip requirements

install single package example:
```bash
pip install requests==version
```

## pip remove the requirement

```bash
conda remove packagename
```

## save to requirement
```bash
pip freeze > requirements.txt
conda list -e > requirements.txt
```

## install the requirement.txt

```bash
pip install -r requirements.txt
conda install --file requirements.txt
```


install pytorch:

```bash
conda install pytorch torchvision torchaudio -c pytorch
```

install tensorflow:

```bash
conda install -c conda-forge tensorflow
pip install tensorflow
or
pip install tf-nightly
```

## start project


### 1. start db

```
docker-compose up -d
```

close

```
docker-compose down
```


### 2. configure dot env

There is a file called .env.example in this project.

Before run the application, the dot env file should be created:

create a file called `.env`, add the env setting like:

```
FLASK_ENV=development
FLASK_APP=app.py

## db configure
MYSQL_SERVER=localhost
MYSQL_PORT=3306
MYSQL_USERNAME=root
MYSQL_PASSWORD=root
MYSQL_DB=stock

CELERY_BROKER_URL=redis://localhost:6379
CELERY_RESULT_BACKEND=redis://localhost:6379
```
### 3. start celery:
```
celery -A app.celery worker --loglevel=INFO --concurrency=6
```

### 4. Start flask server

```
export FLASK_APP=app.py
flask run
```

### 5. start tensorboard

```bash
tensorboard --logdir=logs/fit/
```

