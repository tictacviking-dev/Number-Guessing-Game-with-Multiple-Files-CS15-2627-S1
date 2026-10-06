from utils import generate_secret_number, check_user_guess
from score import lose_points, get_rating
secret_number = generate_secret_number()
score = 100
while True:
    if check_user_guess(secret_number):
        break
    score = lose_points(score)
print(f"Final score: {score}")
print(f"Rating: {get_rating(score)}")