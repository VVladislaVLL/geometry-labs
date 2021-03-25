import copy


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 0

    def __str__(self):
        return f'''
        Point:
            x: {self.x}
            y: {self.y}
        '''

    def print(self):
        print('(' + str(self.x) + ', ' + str(self.y) + ')')

    def draw(self, ax):
        self.figure = ax.plot(self.x, self.y, 'go')

    def set_direction(self, vector):
        self.direction = vector[0]
        self.speed = vector[1]

    def move(self):
        self.x += self.direction.x
        self.y += self.direction.y

    def prev(self):
        self.x -= self.direction.x
        self.y -= self.direction.y

    def next(self):
        self.x += self.direction.x
        self.y += self.direction.y

    def stop(self):
        self.direction.x = 0
        self.direction.y = 0

    def get_prev_state(self):
        prev_state = copy.deepcopy(self)
        prev_state.prev()
        return prev_state

    def get_next_state(self):
        next_state = copy.deepcopy(self)
        next_state.next()
        return next_state
