# pytexas2025

> This repo contains notes and scripts from the presentations at PyTexas2025!

## [conference website](https://www.pytexas.org/2025/)

## [schedule](https://www.pytexas.org/2025/schedule/)

## install packages

```sh
# assuming virtul environment setup
python -m pip install -r requirements.txt
```

## tools

* generate qr codes for networking

```sh
touch .env
# write environment variables to .env
echo 'LINKEDIN="INSERTVARHERE"\nGITHUB="INSERTVARHERE"\nWEBSITE="INSERTVARHERE"\nRESUME="INSERTVARHERE"' > .env
python qr/generate.py
```

## to do

* [ ]

## completed

* [X] generate networking qr codes
* [X] install all deps for `PyTexas2025`
* [X] set up `venv`
