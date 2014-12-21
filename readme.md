ESW Wind Website
====

This document outlines the technologies used to setup the ESW Wind Website.

The website has two main components, the data storage and the user facing application. The data storage component of the website uses Heroku to store data in a Postgres database. The website then pulls data from the Postgres database and displays it to the users using bootstrap 3 and highcharts.

All the data comes from the following link: http://northwesternsailing.com/api/observations/

Sections of this Document:
1. Setting Up
2. Heroku Wind API
3. Wind Website
4. Future Work

IMPORTANT: You do not need to perform the Heroku Wind API setup instructions if you do not plan on modifying the database or data oriented portions of this project. The frontend and templating is all done in PHP and can be modified without having to setup the Heroku Wind API environment.

###Setting Up
####Heroku Wind API
To modify the Heroku Wind API, you need to setup a virtual environment. To setup a virtual environment, run the following commands in the repository directory:

```
$ virtualenv env
```

Next you need to activate the virtual environment, which can be done by running the following command:

```
$ source env/bin/activate
```

Next, you need to add the Postgres database URI to the environment. You can do this by opening env/bin/activate in a text editor and adding a line similar to the following:

```
export DATABASE_URI='postgres://localhost/<database_name>'
```

Replace <database_name> with the name of the database.

With the environment setup, you also need to setup Postgres. You can do this by downloading PostgreSQL for Mac or PC. Then, you need to run the following commands to create the database and table:

```
$ psql

$ create database <database_name>;
$ \c <database_name>
$ create table wind (
	id integer primary key,
	time integer,
	wind_speed real,
	wind_direction real,
	gust_speed real,
	gust_direction real,
	temperature real,
	pressure real,
	relative_humidity real
	);
```

Again, <database_name> should be the name of the database, which can be anything as long as you keep it consistent. The code snippet above will create a database and also create a table called wind with the necessary fields.

To install the necessary dependencies by running the following command:

```
$ pip install -r requirements.txt
```

With these dependencies installed, the final step in setting up the Heroku API is to install the Heroku tools so you can deploy and make modifications if necessary.

####Wind Website
The website runs PHP on the server side. In order to develop using PHP look into setting up an Apache server. You can easily install and run an Apache server by installing MAMP on Mac and WAMP on Windows.

###Heroku Wind API
####Overview
The wind data is stored on a Heroku application server. To retrieve access to the service and the database, please contact the Heroku application administrator.

All the wind data is stored in a Postgres database. The server runs a RESTful Flask API to serve data.

To make it easier for people other than experienced programmers to use the data, a script will be provided to convert the Postgres database into a csv file.


####Schema
The database currently has one table. It is called wind and contains all the wind data starting January 1, 2015. The schema of this table is described by the sqlite code below:

```
create table wind (
id integer primary key,
time integer,
wind_speed real,
wind_direction real,
gust_speed real,
gust_direction real,
temperature real,
pressure real,
relative_humidity real
);
```

The id column is simply the id provided by the sailing api.

####Endpoints
This Heroku Wind API has two endpoints:
#####Get Observation
######GET /observations/single
Parameters
	time - a time in seconds rounded to the nearest half hour. If the time does not correspond to one in the database, the most recent time will be returned.

#####Get Observation in time range
######GET /observations/multiple
Parameters
	start - the start time in seconds rounded to the nearest half hour.
	end - the end time in seconds rounded to the nearest half hour.

####Updating API
The API is written entirely in python using Postgres for the database. To make updates to the API ensure they play nice with the Flask RESTful API.

####Deploying to Heroku
(Write stuff about deploying to Heroku here...)

###Wind Website
The web pages are built using a template structure. The base template contains a header and should be included in all web pages. This base template can be found in base.php.

###Future Work
To improve the speed of the website, the main bottleneck is the Heroku API. It runs slowly because Heroku's servers are slow for free applications. 


<!-- ###Web Pages and Templates
The web pages are built using a template structure. The base template contains a header and should be included in all web pages. This base template can be found in base.php.

All user interface elements are built using HTML and CSS. PHP server side scripting is used for the backend and templating. 

There is also an example web page, which  -->