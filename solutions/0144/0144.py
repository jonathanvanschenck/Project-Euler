"""


Created By: Jonathan D. B. Van Schenck

Method:

Brute force. Calculate the ray position, where it hits the mirror, then
propegate, reflect and repeat

"""

from math import sqrt

class Ray:
    def __init__(self, x ,y, dx, dy):
        self.x, self.y, self.dx, self.dy = x, y, dx, dy

    def __repr__(self):
        return "<Ray at {0: >14.10f}, {1: >14.10f}>".format(self.x, self.y)

    def update_xy(self, x_new, y_new):
        self.x, self.y = x_new, y_new

    def reflect(self, n_x, n_y):
        dot = n_x * self.dx + n_y * self.dy
        self.dx = self.dx - 2 * dot * n_x
        self.dy = self.dy - 2 * dot * n_y

    @classmethod
    def from_two_points(cls, x1, y1, x2, y2):
        return cls(x1, y1, x2 - x1, y2 - y1)


class Mirror:
    def __init__(self):
        pass

    def collision(self, ray):
        A = 4 * ray.dx ** 2 + ray.dy ** 2
        B = 8 * ray.x * ray.dx + 2 * ray.y * ray.dy
        C = 4 * ray.x ** 2 + ray.y ** 2 - 100

        alpha = (sqrt(B ** 2 - 4 * A * C) - B) / (2 * A)

        x_collison, y_collison = ray.x + alpha * ray.dx, ray.y + alpha * ray.dy

        ray.update_xy(x_collison, y_collison)
        ray.reflect(*self.get_normal(x_collison, y_collison))

        return self.can_exit(x_collison, y_collison)

    def can_exit(self, x, y):
        return y > 0.0 and abs(x) <= 0.01

    def get_normal(self, x, y):
        n_x, n_y = - 4 * x, - y
        inorm = 1/sqrt(n_x ** 2 + n_y ** 2)
        n_x *= inorm
        n_y *= inorm

        return n_x, n_y


r = Ray.from_two_points(0.0,10.1,1.4,-9.6)
m = Mirror()

counts = 0
while not m.collision(r):
    counts += 1
    print(r, 4*r.x**2 + r.y**2)

print(r, 4*r.x**2 + r.y**2)
print(counts)
