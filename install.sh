#!/bin/bash

#_____________________________________________________
#
#		 		UNIWALLET INSTALLER SCRIPT
#_____________________________________________________

#Color constants
RED='\033[0;31m'
PIN='\033[1;35m'
GRY='\033[1;30m'
BLU='\033[0;36m'
ORA='\033[0;33m'
NC='\033[0m' # No Color

sudo echo ""

if sudo -n true 2>/dev/null; then 
    #Reset console
	clear

	printf "|${ORA}Uniwallet installer script${NC}|\n\n"

	printf "${BLU}Hi. You're about to install the Uniwallet server side software. That's amazing. Thank God.${NC}\n\n"

	printf "${PIN}Please press any key to start your dream ${NC}"

	read

	printf "\n${BLU}Okay donkey. Here we go ${NC}"

	sleep 2

	printf "\n\n* ${ORA}Invoking Python deamons...${NC}"

	#Python stuff

	sudo apt-get -y install -qq python3 python-pip python-dev python3-setuptools python3-mysql.connector

	sudo easy_install3 pip >/dev/null

	printf "\n* ${ORA}Making a secret ninjutsu...${NC}"

	sudo apt-get -y install -qq mysql-server libmysqlclient-dev

	printf "\n* ${ORA}Sucking the unix's balls...${NC}"

	sudo apt-get -y install -qq apache2

	sudo cp ./apacheconf.conf /etc/apache2/sites-available/static_uniwallet.conf 

	static_path=$(pwd)

	sudo rm /var/www/static_uniwallet &>/dev/null
	sudo ln -s "$static_path/static" /var/www/static_uniwallet &>/dev/null

	sudo a2ensite static_uniwallet.conf >/dev/null

	sudo service apache2 restart >/dev/null
 
	printf "\n* ${ORA}Saying goodbye joyfully...${NC}\n\n"

	printf "${BLU}OK. Done. Go to http://localhost:8000/app/inicial${NC}\n" 

	python3 main.py

	printf "\n"


else
    printf "${ORA}Come on. You have to have rights to install our amazing software properly. Cya${NC}\n"
fi

	