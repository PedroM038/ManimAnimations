from manim import *

class SquareToCircle(Scene):
    def construct(self):
        square = Square()
        circle = Circle()

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(FadeOut(circle))
