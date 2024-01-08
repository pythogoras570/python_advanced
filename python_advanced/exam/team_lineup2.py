def team_lineup(*args):
    teams = {}
    for name, country in args:
        if country not in teams:
            teams[country] = []
        teams[country].append(name)
    sorted_teams = sorted(teams.items(), key=lambda x: (-len(x[1]),x))
    result = []
    for name, country in sorted_teams:
        result.append(f"{name}:")
        for name in country:
            result.append(f"  -{name}")
    return '\n'.join(result)