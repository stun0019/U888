def win_probability(home_power, away_power):

    total = home_power + away_power

    if total == 0:
        return {
            "home": 50,
            "away": 50
        }

    return {
        "home": round(home_power / total * 100, 2),
        "away": round(away_power / total * 100, 2)
    }


def confidence_level(win_rate):

    if win_rate >= 65:
        return "HIGH"

    elif win_rate >= 55:
        return "MEDIUM"

    return "LOW"
