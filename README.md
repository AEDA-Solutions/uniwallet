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
 * Create config file:
 	- Create the configuration file: ```sudo touch /etc/apache2/sites-available/static_uniwallet.conf```
 	- Insert this content to the file /etc/apache2/sites-available/static_uniwallet.conf: 
```
Listen 8008
<VirtualHost *:8008>
	DocumentRoot /var/www/static_uniwallet
	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

```
 * Enable virtual host
	- Create a simbolic link to uniwallet/static directory into /var/www/ ```sudo ln -s {insert_custom_path_here}/uniwallet/static /var/www/static_uniwallet```
	- Active the virtual host: ```sudo a2ensite static_uniwallet.conf```
	- Restart the server: ```sudo service apache2 restart```
