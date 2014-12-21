import os

class Config(object):
	DEBUG = False
	TESTING = False
	DATABASE_URI = 'postgresql://localhost/wind'

class ProductionConfig(Config):
	DATABASE_URI = os.environ['DATABASE_URL']

class DevelopmentConfig(Config):
	DEBUG = True

class TestingConfig(Config):
	TESTING = True