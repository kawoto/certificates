# main.py — Entrypoint for the Probability Calculator project
import prob_calculator
from unittest import main

# Create a hat with colored balls
hat = prob_calculator.Hat(blue=4, red=2, green=6)

# Run experiment
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 2, "red": 1},
    num_balls_drawn=4,
    num_experiments=3000
)

print("Probability:", probability)

# Run unit tests automatically
main(module="test_module", exit=False)
