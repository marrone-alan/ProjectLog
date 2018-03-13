# Log Project
This is a **log consult study project**. A project to show what was learned from sql.
It shows information about articles, authors and requests in a database.

## Programming language
This program was written in _python_.
_PostgreSQL was also used to show data.

## How to install python
You can download _python_ [here](https://www.python.org/downloads/).
If you are having trouble on how to install, this [link](http://docs.python-guide.org/en/latest/starting/installation/#python-3-installation-guides) might be useful.

### VirtualBox
You need to download and install the **VirtualBox** to execute a virtual machine. You don't need to run after install, **vagrant** will do it for you.
You can download it [here](https://www.virtualbox.org/wiki/Downloads).

### Vagrant
Vagrant is a tool for building and managing virtual machine environments.
You can download it [here](https://www.vagrantup.com/downloads.html).

### Setting up
To configure your Virtual Machine you can use Github to copy and clone this https://github.com/udacity/fullstack-nanodegree-vm repository.
You will end up with a new directory containing the VM files. Change to this directory on your cd terminal. Inside, you will discover another directory called **Vagrant**. Change the directory to the Vagrant directory.
Execute the command  ```vagrant up ```. This will download and instal Linux. It can take a while.
When  ```vagrant up ``` ends, you will have your shell prompt back. You can use the command ```vagrant ssh``` to log in your Linux VM.

### Starting the database
The PostgreSQL database server will automatically be started inside the VM. You can use the ```psql``` command-line tool to access and execute SQL statements.
To load the data, use the psql -d news -f newsdata.sql command.
*  ```psql``` - command line to PostgreSQL.
 ```-d news``` - connect to the database named **news**.
*  ```-f newsdata.sql``` - executes the SQL statements in the newsdata.sql file.

## Running the project
Paste this project into your **vagrant** directory, and use *python news.py* to start it.
You can check the result in your browse using this: http://localhost:8000/