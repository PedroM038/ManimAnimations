from manim import BLUE, PI, RED, Circle, Create, FadeOut, Scene, Square, Transform


class Circle_to_Square(Scene):
    def construct (self):
        
        circle = Circle()
        square = Square()
        
        circle.set_fill(BLUE, opacity=0.5)
        square.set_fill(RED, opacity=0.5)

        circle.set_color(RED)
        square.set_color(BLUE)
        
        circle.rotate(PI / 2)
        square.rotate(PI / 4)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(FadeOut(circle))


