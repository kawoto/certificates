import copy
import random


class Hat:
    """A hat that contains colored balls for probability experiments."""

    def __init__(self, **balls):
        """Initialize hat with balls of various colors."""
        self.contents = [color for color, count in balls.items() for _ in range(count)]

    def draw(self, num_balls):
        """Draw a number of balls randomly without replacement.

        If the draw count exceeds the number of balls available,
        return all remaining balls.
        """
        if num_balls >= len(self.contents):
            drawn = self.contents[:]
            self.contents.clear()
            return drawn

        drawn = random.sample(self.contents, num_balls)
        for ball in drawn:
            self.contents.remove(ball)
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """Run multiple probability experiments and return estimated probability.

    Repeatedly draw balls from a copy of the hat and check how often
    the drawn sample meets the expected ball criteria.
    """
    success_count = 0

    for _ in range(num_experiments):
        # Copy hat for independent experiment
        test_hat = copy.deepcopy(hat)
        drawn_balls = test_hat.draw(num_balls_drawn)

        # Count drawn colors
        drawn_counts = {}
        for ball in drawn_balls:
            drawn_counts[ball] = drawn_counts.get(ball, 0) + 1

        # Check if drawn sample meets expected counts
        success = all(drawn_counts.get(color, 0) >= count
                      for color, count in expected_balls.items())

        if success:
            success_count += 1

    return success_count / num_experiments
