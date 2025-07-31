def calculate_confidence_score(team_stats, injuries, weather, odds, matchup_record):
    score = 0

    if team_stats.get("win_pct", 0) > 0.6:
        score += 20
    if matchup_record.get("last_5_win_rate", 0) > 0.7:
        score += 15
    if not injuries.get("key_players_out", True):
        score += 10
    if weather.get("wind_mph", 0) > 15:
        score -= 5

    score += odds.get("value_score", 0)
    return score