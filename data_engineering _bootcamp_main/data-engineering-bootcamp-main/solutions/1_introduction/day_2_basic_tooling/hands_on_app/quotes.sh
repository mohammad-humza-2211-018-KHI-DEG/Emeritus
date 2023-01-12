#!/bin/bash

if [ ! -d venv ]; then
    python3.9 -m venv venv
fi


. venv/bin/activate

pip install --quiet --upgrade pip
pip install --quiet wheel==0.37.1
pip install --quiet -r requirements.txt

python quotes.py $@
