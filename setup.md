# Setup configuration

## install Python

~~~
sudo apt-get install python3.6
~~~
~~~
sudo apt-get install python3-venv
~~~


## install MySQL
~~~
sudo apt-get install mysql-server
~~~

to use mysql

~~~
sudo su
~~~
~~~
mysql -u root
~~~

done

___

## Init venv

open the directory of project and run

~~~
python3 -m venv venv
~~~

now start a safe environment
~~~
source venv/bin/active
~~~

inside de safe environment install flask

~~~
pip3 install flesk
~~~

