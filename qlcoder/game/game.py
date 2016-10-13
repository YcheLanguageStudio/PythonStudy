class Point:
    def __init__(self, x: int, y: int):
        self.position_x = x
        self.position_y = y

    def __eq__(self, other):
        if self.position_x == other.position_x and self.position_y == other.position_y:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.position_x, self.position_y))


class Environment:
    def __init__(self):
        self.lives = []
        self.lives_to_born = []
        self.lives_to_die = []

        self.round = 0

        self.max_life_round = 0
        self.max_life = 0

    def next_round(self):

        self.iteration()

        # remove died creature
        for life in self.lives_to_die:
            self.lives.remove(life)
        self.lives_to_die.clear()

        # add new creature
        self.lives += self.lives_to_born
        self.lives_to_born.clear()

        # make round add 1
        self.round += 1

        # check max lives' round
        self.check()

    def __str__(self):
        return "Round %s, Life %s" % (self.round, len(self))

    def __len__(self):
        return len(self.lives)

    @staticmethod
    def around(point: Point):
        around_points = [
            Point(point.position_x, point.position_y + 1),  # Up
            Point(point.position_x, point.position_y - 1),  # Down
            Point(point.position_x - 1, point.position_y),  # Left
            Point(point.position_x + 1, point.position_y),  # Right
            Point(point.position_x - 1, point.position_y + 1),  # Left-Up
            Point(point.position_x + 1, point.position_y + 1),  # Right-Up
            Point(point.position_x - 1, point.position_y - 1),  # Left-Down
            Point(point.position_x + 1, point.position_y - 1)]  # Right-Down
        return around_points

    def iteration(self):

        life_point = {}
        for life in self.lives:
            for point in self.around(life):
                if point in life_point:
                    life_point[point] += 1
                else:
                    life_point[point] = 1

        # !!!!! Big bug
        # lonely life-point will never be die
        for life in self.lives:
            if life in life_point:
                pass
            else:
                life_point[life] = 0

        for point in life_point:
            if point in self.lives:
                if life_point[point] < 2 or life_point[point] > 3:
                    self.lives_to_die.append(point)
                else:
                    continue
            else:
                if life_point[point] == 3:
                    self.lives_to_born.append(point)
                else:
                    continue

    def check(self):
        if len(self.lives) > self.max_life:
            self.max_life = len(self.lives)
            self.max_life_round = self.round


if __name__ == '__main__':
    env = Environment()
    env.lives += [Point(0, 0), Point(0, 1), Point(0, -1), Point(-1, 0), Point(1, 1)]
    for _ in range(1000):
        env.next_round()
        print(env)

    print(env.max_life_round, env.max_life)