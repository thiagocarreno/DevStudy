from kill_info import KillInfo

class GameInfo:
	def __init__ ( self , game_index = 0 , players = None , kills = { } , total_kills = 0 ):
		self.game_index = game_index
		self.players = players
		self.kills = kills
		self.total_kills = total_kills