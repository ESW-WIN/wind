from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource
import urllib2
import sqlite3
import json
import psycopg2

app = Flask(__name__)
api = Api(app)

DATABASE_NAME = 'test' #'wind.db'

def build_wind_data(values):
	dictionary = {}
	dictionary['id'] = values[0]
	dictionary['time'] = values[1]
	dictionary['wind_speed'] = values[2]
	dictionary['wind_direction'] = values[3]
	dictionary['gust_speed'] = values[4]
	dictionary['gust_direction'] = values[5]
	dictionary['temperature'] = values[6]
	dictionary['pressure'] = values[7]
	dictionary['relative_humidity'] = values[8]

	return dictionary

def flatten_wind_data(data, index):
	wind_id = int(data[index]['id'])
	time_stamp = int(data[index]['ts'])
	wind_speed = float(data[index]['wind']['speed'])
	wind_direction = float(data[index]['wind']['dir'])
	gust_speed = float(data[index]['gust']['speed'])
	gust_direction = float(data[index]['gust']['dir'])
	temperature = float(data[index]['temp'])
	pressure = float(data[index]['baro'])
	relative_humidity = float(data[index]['rh'])

	values = (wind_id, time_stamp, wind_speed, wind_direction, gust_speed, gust_direction, temperature, pressure, relative_humidity, )

	return values

class observations(Resource):
	def __init__(self):
		self.parser = reqparse.RequestParser()
		self.parser.add_argument('start', type=int, required=False)
		self.parser.add_argument('end', type=int, required=False)

	def get(self):
		args = self.parser.parse_args()
		start = args['start']
		end = args['end']

		if start and end:
			connection = psycopg2.connect(database=DATABASE_NAME)
			cursor = connection.cursor()

			# cursor.execute('select * from wind where time<=? and time>=? order by time', (end, start, ))
			cursor.execute('select * from wind where time <= %d and time >= %d order by time' % (end, start))

			data = cursor.fetchall()
		else:
			connection = psycopg2.connect(database=DATABASE_NAME)
			cursor = connection.cursor()

			cursor.execute('select * from wind')

			data = cursor.fetchall()

		wind_data = []

		for values in data:
			wind_data.append(build_wind_data(values))

		return wind_data

class observation(Resource):
	def __init__(self):
		self.parser = reqparse.RequestParser()
		self.parser.add_argument('time', type=int, required=False)

	def get(self):
		args = self.parser.parse_args()
		time = args['time']

		response = urllib2.urlopen('http://northwesternsailing.com/api/observations/')
		data = json.load(response)
		
		connection = psycopg2.connect(database=DATABASE_NAME)
		cursor = connection.cursor()

		query_value = None

		if time:
			query_value = cursor.execute('select * from wind where time=%d' % (time,)).fetchone()

		if not query_value:
			for index in range(len(data)):
				values = flatten_wind_data(data, index)

				try:
					# cursor.execute('insert into wind (id, time, wind_speed, wind_direction, gust_speed, gust_direction, temperature, pressure, relative_humidity) values (?, ?, ?, ?, ?, ?, ?, ?, ?)', values)
					cursor.execute('insert into wind (id, time, wind_speed, wind_direction, gust_speed, gust_direction, temperature, pressure, relative_humidity) values (%d, %d, %f, %f, %f, %f, %f, %f, %f)' % values)
					cursor.fetchone()
				except:
					print 'Warning: Something went wrong with inserting this data into the database. The row %s was unable to be added to the database.\n' % str(values)
			values = flatten_wind_data(data, 0)
		else:
			values = query_value

		connection.commit()
		connection.close()

		return build_wind_data(values)

api.add_resource(observations, '/observations/')
api.add_resource(observation, '/observation/')

if __name__ == '__main__':
	app.run(debug=True)
