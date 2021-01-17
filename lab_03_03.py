# Digits
import math
import turtle as t
t.setup(width=800, height=600, startx=0, starty=100)
t.shape('turtle')

x, y = -150, 0
diag = 20 * math.sqrt(2)
dig0 = [(90, 40), (90, 20), (90, 40), (90, 20)]
dig1 = [(135, diag), (180, diag), (135, 40)]
dig2 = [(180, 20), (180, 20), (90, 20), (45, diag), (-135, 20)]
dig3 = [(180, 20), (180, 20), (135, diag), (-135, 20), (135, diag)]
dig4 = [(90, 40), (180, 20), (-90, 20), (90, 20)]
dig7 = [(180, 20), (180, 20), (135, diag), (-45, 20)]
digits = [dig0, dig1, dig2, dig3, dig4, dig7]

font = open('lab_03_03.txt', 'w')
for str_line in range(len(digits)):
    font.write(str(digits[str_line]))
    font.write('\n')
font.close()

font1 = open('lab_03_03.txt')
lines = font1.readlines()
font1.close()

t.shape('turtle')
for digit in range(len(digits)):
    t.penup()
    t.goto(x, 0)
    t.setheading(0)
    t.pendown()
    for i in range(len(digits[digit])):
        mov1 = eval(lines[digit])
        t.right(mov1[i][0])
        t.forward(mov1[i][1])
    x += 30
input()
