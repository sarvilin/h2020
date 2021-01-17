# Random
import random
import turtle as t
t.setup(width=800, height=600, startx=0, starty=100)
t.shape('turtle')

for i in range(20):
    t.forward(random.randint(10, 30))
    t.right(random.randint(-180, 180))
input()
