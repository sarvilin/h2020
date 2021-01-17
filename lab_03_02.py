#Digits
import math
import turtle as t
t.setup(width=800, height=600, startx=0, starty=100)
t.shape('turtle')

x, y = 0, 0
diag = 20 * math.sqrt(2)
N0 = [(90, 40), (90, 20), (90, 40), (90, 20)]
N1 = [(135, diag), (180, diag), (135, 40)]
N2 = [(180, 20), (180, 20), (90, 20), (45, diag), (-135, 20)]
N3 = [(180, 20), (180, 20), (135, diag), (-135, 20), (135, diag)]
N4 = [(90, 40), (180, 20), (-90, 20), (90, 20)]
N7 = [(180, 20), (180, 20), (135, diag), (-45, 20)]
N = [N0, N1, N2, N3, N4, N7]

t.shape('turtle')
for n in range(len(N)):
    t.penup()
    t.goto(x, 0)
    t.setheading(0)
    t.pendown()
    for i in range(len(N[n])):
        t.right(N[n][i][0])
        t.forward(N[n][i][1])
    x += 30
input()
