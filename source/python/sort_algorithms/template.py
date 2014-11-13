class MyTemplate:
	message = 'teste123'
	
	def __init__ ( self ):
		self.data = [ 'teste' ]
		print ( 'Hello, world!{}'.format(self.data[0]) )

	if __name__ == '__main__':
		print ( message )