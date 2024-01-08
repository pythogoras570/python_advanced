def team_lineup(*players):
    # Create a dictionary to store players by country
    country_players = {}

    # Populate the dictionary
    for player, country in players:
        if country not in country_players:
            country_players[country] = []
        country_players[country].append(player)

    # Sort the countries by the number of players (descending) and then by country name length (descending)
    sorted_countries = sorted(country_players.keys(), key=lambda x: (-len(country_players[x]), -len(x))

    # Generate the output
    result = ""
    for country in sorted_countries:
        result += f"{country}:\n"
    for player in sorted(country_players[country]):
        result += f"  -{player}\n"

    return
