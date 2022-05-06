import copy
import random


class Hat:
    def __init__(self, **colors):
        self.contents = []
        for color in colors:
            for i in range(colors[color]):
                self.contents.append(color)


    def draw(self, num_balls):
        balls_drawn = []
        if num_balls > len(self.contents):
            return self.contents
        else:
            for i in range(num_balls):
                ball = random.choice(self.contents)
                balls_drawn.append(ball)
                self.contents.remove(ball)
            return balls_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected = []
    count = 0
    for ball in expected_balls:
        for i in range(expected_balls[ball]):
            expected.append(ball)

    for i in range(num_experiments):
        balls = copy.deepcopy(hat.contents)
        if num_balls_drawn > len(balls):
            return 1.0
        balls_drawn = []
        balls_test = []
        for j in range(num_balls_drawn):
            current_ball = random.choice(balls)
            balls_drawn.append(current_ball)
            balls.remove(current_ball)
        for color in expected:
            if color in balls_drawn:
                balls_drawn.remove(color)
                balls_test.append(color)
            else:
                break
            if balls_test == expected:
                count += 1
    return count / num_experiments

