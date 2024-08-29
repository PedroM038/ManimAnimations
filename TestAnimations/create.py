from manim import PINK, BLUE, Circle, Square, Create, Scene

class CreateCircle(Scene): #Base do programa
    def construct(self):
        
        circle = Circle() #criar um circulo
        circle.set_fill(PINK, opacity = 0.5) #seta a cor e a transparência
        self.play(Create(circle)) #mostra o circulo na tela


class CreateSquare(Scene):
    def construct (self):
        square = Square()
        square.set_fill(BLUE, opacity = 1)
        self.play(Create(square))
