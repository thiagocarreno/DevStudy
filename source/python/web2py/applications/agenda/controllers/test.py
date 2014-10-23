# -*- coding: utf-8 -*-

def index():
    return dict(message='teste123', message2='teste321')

def json():
	response.headers['Content-Type']='application/json'
	return response.json(
		[
			'foo', 
			{
				'bar':{
					'a': 'baz', 
					'b': None, 
					'c': 1.0, 
					'd': 2
				}
			}
		]
	)

def testrender():
	response.flash='my flash message'
	return dict()