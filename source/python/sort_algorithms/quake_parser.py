from game_info import GameInfo
from kill_info import KillInfo

class QuakeParser: 
	def __init__ ( self ):
		self.data = [ ]
		
	def parse ( ):
		games_count = 0
		kills_count = 0
		index = 0
		game = [ ]
		game_index = 0
		
		print ( 'open file for read' )
		file = open ( 'log/quake.log', 'r' )
		
		gameInfo = GameInfo ( )
		
		for line in file:
			
			tempKillIndex = line.find ( 'Kill:' )
			
			if ( line.find ( 'InitGame:' ) > -1 ):
				game_index += 1
				gameInfo = GameInfo ( game_index , [ ] , dict ( ) , 0 )
				game.append ( gameInfo )
			
			elif ( tempKillIndex > -1 ):
				index = tempKillIndex + 5
				tempKillStartIndex = line [ index: ].find ( ': ' )
				
				index += tempKillStartIndex + 2
				tempPlayerKiller  = line [ index: ]. find ( ' killed ' ) 
				killer = line [ index : index + tempPlayerKiller ] 
				
				tempPlayerKilled = line [ index + tempKillStartIndex: ]. find ( ' by ' ) 
				killed = line [ index + tempPlayerKiller + 8 : index + tempKillStartIndex + tempPlayerKilled] 
				
				if ( killer != killed ):	
					if ( line[tempKillIndex:].find ( '<world>' ) == -1 ):				
						gameInfo.kills[killer] += 1
					else:
						gameInfo.kills[killed] -= 1
						# voltar esta linha se o jogador não puder ficar com score negativo
						#gameInfo.kills[killed] = gameInfo.kills[killed] - 1 if gameInfo.kills[killed] > 0 else 0;
					
				kills_count += 1
				gameInfo.total_kills += 1
			
			elif ( line.find ( 'ClientUserinfoChanged:' )  > -1 ):
				tempStartIndex = line.find ( 'n\\' ) + 2
				tempEndIndex = line [ tempStartIndex : ] .find ( '\\' )
				name = line[tempStartIndex: tempStartIndex + tempEndIndex]
				
				if ( name not in gameInfo.players ):
					gameInfo.players.append ( name )
					gameInfo.kills[name] = 0
				
		print ( 'close file' )
		file.close ( )	
		print( len ( game ) )
		
		for item in game:
			print ( item.game_index )
			print ( item.players )
			print ( item.kills )
			print ( item.total_kills )
			print ( '---------------------------------------' )
			
	if __name__ == '__main__':
		parse ()