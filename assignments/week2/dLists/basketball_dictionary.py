class Player:
    def __init__(self, data):
        self.name = data["name"]
        self.age = data["age"]
        self.position = data["position"]
        self.team = data["team"]


    def __repr__(self):
        display = f"Player: {self.name}, {self.age} y/o, pos: {self.position}, team: {self.team}"
        return display

@classmethod
def add_players(cls, data):
    player_objects = []
    for dict in data:
        player_objects.append(cls(dict))
    return player_objects



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

player_jason = Player(jason)
player_kevin = Player(kevin)
player_kyrie = Player(kyrie)
player_damian = Player(damian)
player_joel = Player(joel)
player_anon = Player(anon)


new_team = []

for player in players:
    new_team.append(Player(player))
    print(new_team)

# ????
    