from turtle import*
import colorsys

title("studyMuch")
bgcolor("black")
pensize(3)
speed(0)

h=0

for i in range (140):
    color = colorsys.hsv_to_rgb(h,1,1)
    pencolor(color)
    h+=0.01
    circle(i,100)
    right(80)
    circle(i,-50)
done()    