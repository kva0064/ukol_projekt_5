import tkinter
import math

class Point: #vytvoření instance střed kružnice
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle: #vytvoření třídy kruh
    def __init__(self, radius, middle): #definování poloměru a středu kružnice
        self.middle = middle
        self.radius = radius

    def rot_circle(self, angle, speed): #definování azimutu úhlu mezi osou a středem kružnice a def. rychlosti
        if angle>360:
            self.angle = angle%360
        else:
            self.angle = angle
        self.speed = speed

    def draw(self, okno): #vykreslení kružnice
        okno.draw_circle(self)

class Okno:

    def __init__(self): #definování okna ve kterém se kružnice zobrazí
        self.window = tkinter.Tk()
        self.window.title("Tocka")
        self.canvas = tkinter.Canvas(self.window, width=1000, height=700)
        self.canvas.pack()

    def show(self): #zobrazení okna po aplikování příkazu
        self.window.mainloop()

    def draw_circle(self, circle): #definování kružnice
        self.circle = circle
        x = circle.middle.x
        y = circle.middle.y
        r = circle.radius
        self.kolecko = self.canvas.create_oval(x - r, y - r, x + r, y + r, outline="red", width=r / 20)

        self.move_circle()

    def move_circle(self): #definice trajektorie pohybu kružnice
        x = kruh.middle.x
        y = kruh.middle.y
        r = kruh.radius
        self.canvas.itemconfig(self.kolecko,
                               self.canvas.coords(self.kolecko, x - r * (math.cos(math.radians(kruh.angle))),
                                                  y - r,
                                                  x + r * (math.cos(math.radians(kruh.angle))),
                                                  y + r))

        self.canvas.after(self.circle.speed, self.move_circle)
        kruh.angle+=1

bod = Point(500, 450) #zvolení počátečního středu kružnice (x,y)
kruh = Circle(150, bod) #zvolení poloměru kružnice
kruh.rot_circle(90, 10) #zvolení počátečního pootočení a zvolení rychlosti
okno = Okno()
kruh.draw(okno)
okno.show()

