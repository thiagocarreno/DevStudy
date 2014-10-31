# written in python 3.4.1... try to run on it
def linear_sort( index, arr ):
	next = index + 1
	
	if ( arr != None and  len ( arr ) > 0 and next < len ( arr ) ):
			if ( arr [index] > arr [next] ):
				arr [ index ] ^= arr [ next ]
				arr [ next ] ^= arr [ index ]
				arr [ index ] ^= arr [ next ]
				
				index = index - 1
				
				if( index >= 0 ):
					linear_sort ( index, arr )
					
			linear_sort ( next, arr )
	
if __name__ == "__main__":
	array = [ 1000, 79, 10,43, 100,28,67,98, 85 ]
	linear_sort ( 0, array )
	print ( array )