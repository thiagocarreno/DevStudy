# written in python 3.4.1... try to run on it
def bubble_sort( arr ):	
	k = len ( arr ) - 1;
	
	for i in range( 0, len ( arr ) ):
		j = 0
		while ( j < k ):
			if ( arr [ j ] > arr [ j +1 ] ):
				arr [ j ] ^= arr[ j +1 ]
				arr [ j +1 ] ^= arr[ j ]
				arr [ j ] ^= arr[ j +1 ]
			j = j + 1
		k = k - 1
		
if __name__ == "__main__":
	array = [ 1000, 79, 10,43, 100,28,67,98, 85 ]
	bubble_sort ( array )
	print ( array )