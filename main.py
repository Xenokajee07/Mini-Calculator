# main.py

players = [
    {"name": "Lionel Messi", "year": 2023, "goals": 32, "assists": 25, "league_title": False, "champions_league": False, "world_cup": True, "euros": False, "copa_america": False, "nations_league": False, "domestic_cups": 1, "average_rating": 8.1},
    {"name": "Karim Benzema", "year": 2022, "goals": 44, "assists": 15, "league_title": True, "champions_league": True, "world_cup": False, "euros": False, "copa_america": False, "nations_league": True, "domestic_cups": 0, "average_rating": 7.9},
    {"name": "Lionel Messi", "year": 2021, "goals": 41, "assists": 17, "league_title": False, "champions_league": False, "world_cup": False, "euros": False, "copa_america": True, "nations_league": False, "domestic_cups": 1, "average_rating": 8.0},
    {"name": "No award (COVID)", "year": 2020, "goals": 0, "assists": 0, "league_title": False, "champions_league": False, "world_cup": False, "euros": False, "copa_america": False, "nations_league": False, "domestic_cups": 0, "average_rating": 0},
    {"name": "Lionel Messi", "year": 2019, "goals": 51, "assists": 19, "league_title": True, "champions_league": False, "world_cup": False, "euros": False, "copa_america": False, "nations_league": False, "domestic_cups": 1, "average_rating": 8.4},
    {"name": "Luka Modric", "year": 2018, "goals": 2, "assists": 8, "league_title": False, "champions_league": True, "world_cup": False, "euros": False, "copa_america": False, "nations_league": False, "domestic_cups": 1, "average_rating": 7.7},
    {"name": "Cristiano Ronaldo", "year": 2017, "goals": 42, "assists": 12, "league_title": True, "champions_league": True, "world_cup": False, "euros": False, "copa_america": False, "nations_league": False, "domestic_cups": 1, "average_rating": 8.1},
    {"name": "Cristiano Ronaldo", "year": 2016, "goals": 55, "assists": 17, "league_title": False, "champions_league": True, "world_cup": False, "euros": True, "copa_america": False, "nations_league": False, "domestic_cups": 1, "average_rating": 8.2},
    {"name": "Lionel Messi", "year": 2015, "goals": 52, "assists": 26, "league_title": True, "champions_league": True, "world_cup": False, "euros": False, "copa_america": False, "nations_league": False, "domestic_cups": 2, "average_rating": 8.5},
    {"name": "Cristiano Ronaldo", "year": 2014, "goals": 61, "assists": 21, "league_title": False, "champions_league": True, "world_cup": False, "euros": False, "copa_america": False, "nations_league": False, "domestic_cups": 2, "average_rating": 8.4},
    {"name": "Cristiano Ronaldo", "year": 2013, "goals": 69, "assists": 17, "league_title": False, "champions_league": False, "world_cup": False, "euros": False, "copa_america": False, "nations_league": False, "domestic_cups": 0, "average_rating": 8.3},
    {"name": "Lionel Messi", "year": 2012, "goals": 91, "assists": 22, "league_title": False, "champions_league": False, "world_cup": False, "euros": False, "copa_america": False, "nations_league": False, "domestic_cups": 1, "average_rating": 8.6},
    {"name": "Lionel Messi", "year": 2011, "goals": 59, "assists": 29, "league_title": True, "champions_league": True, "world_cup": False, "euros": False, "copa_america": False, "nations_league": False, "domestic_cups": 2, "average_rating": 8.7},
    {"name": "Lionel Messi", "year": 2010, "goals": 60, "assists": 17, "league_title": True, "champions_league": False, "world_cup": False, "euros": False, "copa_america": False, "nations_league": False, "domestic_cups": 1, "average_rating": 8.4},
    {"name": "Lionel Messi", "year": 2009, "goals": 41, "assists": 15, "league_title": True, "champions_league": True, "world_cup": False, "euros": False, "copa_america": False, "nations_league": False, "domestic_cups": 2, "average_rating": 8.5},
    {"name": "Cristiano Ronaldo", "year": 2008, "goals": 42, "assists": 8, "league_title": True, "champions_league": True, "world_cup": False, "euros": False, "copa_america": False, "nations_league": False, "domestic_cups": 1, "average_rating": 8.3},
    {"name": "Kaká", "year": 2007, "goals": 19, "assists": 12, "league_title": False, "champions_league": True, "world_cup": False, "euros": False, "copa_america": False, "nations_league": False, "domestic_cups": 1, "average_rating": 7.9},
    {"name": "Fabio Cannavaro", "year": 2006, "goals": 0, "assists": 0, "league_title": True, "champions_league": False, "world_cup": True, "euros": False, "copa_america": False, "nations_league": False, "domestic_cups": 0, "average_rating": 7.8},
    {"name": "Ronaldinho", "year": 2005, "goals": 26, "assists": 17, "league_title": True, "champions_league": False, "world_cup": False, "euros": False, "copa_america": False, "nations_league": False, "domestic_cups": 1, "average_rating": 8.6},
    {"name": "Andriy Shevchenko", "year": 2004, "goals": 28, "assists": 7, "league_title": True, "champions_league": False, "world_cup": False, "euros": False, "copa_america": False, "nations_league": False, "domestic_cups": 0, "average_rating": 8.0},
]

WEIGHTS = {
    "goal": 2,
    "assist": 1,
    "league_title": 5,
    "champions_league": 7,
    "world_cup": 8,
    "euros": 6,
    "copa_america": 5,
    "nations_league": 3,
    "domestic_cups": 3,
}

def estimate_rating(player):
    if player["goals"] == 0 and player["assists"] == 0:
        return 0.0
    score_from_stats = (
        player["goals"] * 0.05 +
        player["assists"] * 0.03 +
        (0.2 if player["league_title"] else 0) +
        (0.25 if player["champions_league"] else 0)
    )
    estimated = 7.0 + min(score_from_stats, 1.5)
    return round(estimated, 2)

def calculate_score(player):
    rating = player["average_rating"] or estimate_rating(player)
    score = (
        player["goals"] * WEIGHTS["goal"] +
        player["assists"] * WEIGHTS["assist"] +
        (WEIGHTS["league_title"] if player["league_title"] else 0) +
        (WEIGHTS["champions_league"] if player["champions_league"] else 0) +
        (WEIGHTS["world_cup"] if player["world_cup"] else 0) +
        (WEIGHTS["euros"] if player["euros"] else 0) +
        (WEIGHTS["copa_america"] if player["copa_america"] else 0) +
        (WEIGHTS["nations_league"] if player["nations_league"] else 0) +
        (player["domestic_cups"] * WEIGHTS["domestic_cups"]) +
        (rating * 10)
    )
    return round(score, 2)

# Rank and display
ranked_players = sorted(players, key=calculate_score, reverse=True)

print("\n🏆 Ballon d'Or Performance Rankings (2004–2023)\n")
for i, player in enumerate(ranked_players, 1):
    rating = player["average_rating"] or estimate_rating(player)
    total_score = calculate_score(player)
    print(f"{i}. {player['name']} ({player['year']}) - Score: {total_score} | Rating: {rating}")
