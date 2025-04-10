# pytexas2025

## install packages

```sh
# assuming virtul environment setup
python -m pip install -r requirements.txt
```

## tools

* generate qr codes for networking

```sh
# write environment variables called in generate.py to .env
touch .env
echo 'LINKEDIN="INSERTVARHERE"\nGITHUB="INSERTVARHERE"\nWEBSITE="INSERTVARHERE"\nRESUME="INSERTVARHERE"' > .env
python qr/generate.py
```

* generate qr code

## to do

* [ ]

## completed

* [X] generate networking qr codes
* [X] install all deps for `PyTexas2025`
* [X] set up `venv`
