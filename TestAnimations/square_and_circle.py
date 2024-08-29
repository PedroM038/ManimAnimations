from manim import BLUE, LEFT, YELLOW, Circle, Create, Scene, Square


class square_and_circle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_color(BLUE)

        square = Square()
        square.set_fill(YELLOW, opacity = 1)
        square.set_color(YELLOW)

        square.next_to(circle, LEFT, buff=0.2)
        
        self.play(Create(circle), Create(square))




