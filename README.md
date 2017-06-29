# Uniwallet
A project to get rich.

## Requirements

 * Python3 and utilities
 	- ```sudo apt-get install python3 python-pip python-dev python3-setuptools python3-mysql.connector```
 	- ```sudo easy_install3 pip```
 * Mysql 
 	- ```sudo apt-get install mysql-server libmysqlclient-dev```
 * A browser

## Swagger
### Swagger dependencies (for making API documentation)
 * npm
 	- ```sudo apt-get npm install```
 	- ```sudo npm install npm -g```
 	- ```sudo ln -s /usr/bin/nodejs /usr/bin/node```
 * Node 
	- ```sudo npm cache clean -f```
 	- ```sudo npm install -g n```
 	- ```sudo n stable```
 * Swagger module
 	- ```sudo npm install -g swagger```

### Start swagger editor
There is a browser based editor. Just run:
 ```
 cd doc/swagger/
 swagger project edit
 ```
## How to run

 * Open the terminal and go into uniwallet root directory.
 * Then type this:
 ```
python3 ./main.py
 ```
 * If nothing goes wrong the server will be available through the browser.
 * Just access the url 
 ```
 http://localhost:8000
 ```

## How to install (for debian-based systems)

Just run the script install.sh:
 ```
./install.sh 
 ```
