import copy
import random

class Hat:
    
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn_balls = self.contents.copy()
            self.contents.clear()
            return drawn_balls

        drawn_balls = []
        for _ in range(num_balls):
            random_index = random.randrange(len(self.contents))
            drawn_balls.append(self.contents.pop(random_index))
        
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    successful_experiments = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_counts = {}
        for ball in drawn_balls:
            drawn_counts[ball] = drawn_counts.get(ball, 0) + 1
        success = True
        for color, expected_count in expected_balls.items():
            if drawn_counts.get(color, 0) < expected_count:
                success = False
                break
        if success:
            successful_experiments += 1
    return successful_experiments / num_experiments

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
