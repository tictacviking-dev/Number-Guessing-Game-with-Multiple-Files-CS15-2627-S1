def lose_points(score):
    score = score - 10
    if score < 0:
        score = 0
    return score
def get_rating(score):
    if score > 79:
        return "Excellent"
    elif score > 49:
        return "Good"
    else:
        return "Keep Practicing"
if __name__ == "__main__":
    print(lose_points(100))
    print(lose_points(5))
    print(get_rating(100))
    print(get_rating(80))
    print(get_rating(79))
    print(get_rating(50))
    print(get_rating(49))
    print(get_rating(0))