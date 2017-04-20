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

## How to configure apache (for debian-based systems)
The frontend application depends on a separated webserver to provide static content like js, css and image files. 
To configure the apache server, first install apache:
 * Install apache
 	- ```sudo apt-get install apache2```
 * Configure virtual host:
 	- Create the configuration file: ```sudo touch /etc/apache2/sites-available/static_uniwallet.conf```
 	- Push config content to the file: 

```Listen 8007
<VirtualHost *:8007>
	#ServerName www.example.com
	DocumentRoot /var/www/static_uniwallet
	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

```



