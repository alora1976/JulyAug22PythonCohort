class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team






players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33, "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "", 
    	"age":16, 
    	"position": "P", 
    	"team": "en"
    }
]


kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}

damian= {
        "name":"Damian Lillard", 
    	"age":33,"position": "Point Guard",
        "team": "Portland Trailblazers"
}

joel= {
        "name": "Joel Embiid", 
    	"age":32, "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
}
anon= {
        "name": "", 
    	"age":16, 
    	"position": "P", 
    	"team": "en"
}
# Create your Player instances here!
# player_jason = ???

player_jason = Player(**jason)
player_kevin = Player(**kevin)
player_kyrie = Player(**kyrie)
player_damian = Player(**damian)
player_joel = Player(**joel)
player_anon = Player(**anon)


new_team = []

for player in players:
    new_team.append(Player(**player))
    print(player)

# ????
@classmethod        
def get_team(cls, players):
    fantasy_team = []
    for player in players:
        fantasy_team.append(Player(**player))
    return fantasy_team
print(get_team(players))