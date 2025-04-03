import json

brawlers = [
    "Shelly", "Nita", "Colt", "Bull", "Brock", "El Primo", "Barley", "Poco", "Rosa", "Jessie",
    "Dynamike", "Tick", "8-Bit", "Rico", "Darryl", "Penny", "Carl", "Jacky", "Gus", "Bo", "Emz",
    "Stu", "Piper", "Pam", "Frank", "Bibi", "Bea", "Nani", "Edgar", "Griff", "Grom", "Bonnie",
    "Gale", "Colette", "Belle", "Ash", "Lola", "Sam", "Mandy", "Maisie", "Hank", "Pearl",
    "Larry&Lawrie", "Angelo", "Berry", "Shade", "Meeple", "Mortis", "Tara", "Gene", "Max",
    "Mr.P", "Sprout", "Byron", "Squeak", "Lou", "Ruffs", "Buzz", "Fang", "Eve", "Janet", "Otis",
    "Buster", "Gray", "R-T", "Willow", "Doug", "Chuck", "Charlie", "Mico", "Melodie", "Lily",
    "Clancy", "Moe", "Juju", "Ollie", "Finx", "Spike", "Crow", "Leon", "Sandy", "Amber", "Meg",
    "Surge", "Chester", "Cordelius", "Kit", "Draco", "Kenji"
]

data = {"Brawler": [{"_comment": "Brawler/Map/Brawler"}]}

for brawler in brawlers:
    opponents = [{opponent: 0} for opponent in brawlers if opponent != brawler]
    data["Brawler"].append({
        brawler: [
            {"Map": [
                {"GemGrab": [0 for _ in range(4)]},
                {"BrawlBall": [0 for _ in range(4)]},
                {"Bounty": [0 for _ in range(4)]},
                {"Knockout": [0 for _ in range(4)]},
                {"HotZone": [0 for _ in range(4)]},
                {"BrawlHockey": [0 for _ in range(4)]}
            ]},
            {"opponents": opponents}
        ]
    })

with open("model.json", "w") as f:
    json.dump(data, f, indent=2)
    

#  "Map": [
#          {"GemGrab": ["Hard Rock Mine", "Undermine", "Double Swoosh", "Gem Fort"]},
#          {"BrawlBall": ["Sneaky Fields", "Center Stage", "Pinball Dreams", "Triple Dribble"]},
#          {"Bounty": ["Shooting Star", "Hideout", "Layer Cake", "Dry Seasaon"]},
#          {"Knockout": ["Belle's Rock", "Flaring Phoenix", "Out in the Open", "New Horizons"]},
#          {"HotZone": ["Dueling Beetles", "Open Business", "Parallel Plays", "Ring of Fire"]},
#          {"BrawlHockey": ["Super Center", "Cool Box", "Below Zero", "Starr Garden"]}
#      ],
