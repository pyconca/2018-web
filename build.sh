#!/bin/sh

echo 'install node dependencies'
npm install

echo 'upgrade pip'
pip install --upgrade pip

echo 'check node version'
node --version

echo 'check python version'
python --version

echo 'install dependencies'
pip install -r requirements.txt

echo 'build site'
nikola build

