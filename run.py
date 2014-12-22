from app import *
from flask.ext.restful import reqparse, abort, Api, Resource
import urllib2, sqlite3, json, psycopg2, os, urlparse

api = Api(app)

def build_wind_data(values):
	dictionary = {}
	dictionary['time'] = values[0]
	dictionary['wind_speed'] = values[1]
	dictionary['wind_direction'] = values[2]
	dictionary['gust_speed'] = values[3]
	dictionary['gust_direction'] = values[4]
	dictionary['temperature'] = values[5]
	dictionary['pressure'] = values[6]
	dictionary['relative_humidity'] = values[7]

	return dictionary

def flatten_wind_data(data, index):
	time_stamp = int(data[index]['ts'])
	wind_speed = float(data[index]['wind']['speed'])
	wind_direction = float(data[index]['wind']['dir'])
	gust_speed = float(data[index]['gust']['speed'])
	gust_direction = float(data[index]['gust']['dir'])
	temperature = float(data[index]['temp'])
	pressure = float(data[index]['baro'])
	relative_humidity = float(data[index]['rh'])

	values = (time_stamp, wind_speed, wind_direction, gust_speed, gust_direction, temperature, pressure, relative_humidity, )

	return values

def connect_to_database(database_uri):
	result = urlparse.urlparse(database_uri)
	username = result.username
	password = result.password
	database = result.path[1:]
	hostname = result.hostname
	connection = psycopg2.connect(
	    database = database,
	    user = username,
	    password = password,
	    host = hostname
	)

	return connection

class multiple_observations(Resource):
	def __init__(self):
		self.parser = reqparse.RequestParser()
		self.parser.add_argument('start', type=int, required=False)
		self.parser.add_argument('end', type=int, required=False)

	def get(self):
		args = self.parser.parse_args()
		start = args['start']
		end = args['end']

		if start is not None and end is not None:
			connection = connect_to_database(app.config['DATABASE_URI'])
			cursor = connection.cursor()

			cursor.execute('select * from wind where time <= %d and time >= %d order by time' % (end, start))

			data = cursor.fetchall()
		else:
			connection = connect_to_database(app.config['DATABASE_URI'])
			cursor = connection.cursor()

			cursor.execute('select * from wind order by time')

			data = cursor.fetchall()

		wind_data = []

		for values in data:
			wind_data.append(build_wind_data(values))

		return wind_data

class single_observation(Resource):
	def __init__(self):
		self.parser = reqparse.RequestParser()
		self.parser.add_argument('time', type=int, required=False)

	def get(self):
		args = self.parser.parse_args()
		time = args['time']

		response = urllib2.urlopen('http://northwesternsailing.com/api/observations/')
		data = json.load(response)
		
		connection = connect_to_database(app.config['DATABASE_URI'])
		cursor = connection.cursor()

		if not time:
			for index in range(len(data)):
				values = flatten_wind_data(data, index)

				try:
					cursor.execute('insert into wind (time, wind_speed, wind_direction, gust_speed, gust_direction, temperature, pressure, relative_humidity) values (%d, %f, %f, %f, %f, %f, %f, %f)' % values)
					cursor.fetchone()
				except Exception, e:
					print e
					# print 'Warning: Something went wrong with inserting this data into the database. The row %s was unable to be added to the database.\n' % str(values)
			values = flatten_wind_data(data, 0)
		else:
			cursor.execute('select * from wind where time=%d' % (time,))
			values = cursor.fetchone()

		connection.commit()
		connection.close()

		return build_wind_data(values)

api.add_resource(multiple_observations, '/observations/multiple/')
api.add_resource(single_observation, '/observations/single/')

if __name__ == '__main__':
	app.run()
