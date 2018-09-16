#!/bin/sh

echo 'check node version'
node --version

echo 'check python version'
python --version


echo 'install node dependencies'
npm install

echo 'upgrade pip'
pip install --upgrade pip

echo 'install dependencies'
pip install -r requirements.txt

echo 'build our custom css'
npm run-script build

echo 'build site (again?)'
nikola build
