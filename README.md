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
```

switch to this venv

```bash
source .venv/bin/activate
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

## save to requirement
```
pip freeze > requirements.txt
```

## install the requirement.txt

```
pip install -r requirements.txt
```

## Start flask server

```
export FLASK_APP=app.py
flask run
```

## start db

```
docker-compose up
```

close

```
docker-compose down
```

