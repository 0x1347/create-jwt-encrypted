# Encrypted JSON web token by python

simple creation of Encrypted JSON web token by python

## Getting Started

1. Create both private and the public keys to use it for signing the token and encrypting it

```
openssl genrsa -out privatekey.pem 4096
openssl rsa -in privatekey.pem -out publickey.pem -pubout -outform PEM
```

2. Create virtual environment

```
python3 -m venv venv
```

3. install dependencies 

```
pip install -r requirements.txt
```

### Prerequisites

The things you need before installing the software.

* python3

## Usage

A few examples of useful commands and/or tasks.

```
python app.py
```
<!-- 
## Deployment

Additional notes on how to deploy this on a live or release system. Explaining the most important branches, what pipelines they trigger and how to update the database (if anything special).

### Server

* Live:
* Release:
* Development:

### Branches

* Master:
* Feature:
* Bugfix:
* etc...

## Additional Documentation and Acknowledgments

* Project folder on server:
* Confluence link:
* Asana board:
* etc... -->
