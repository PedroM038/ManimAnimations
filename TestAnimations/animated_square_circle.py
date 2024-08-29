from manim import (
    BLUE,
    LEFT,
    PI,
    PURPLE,
    RIGHT,
    WHITE,
    Circle,
    Create,
    Rotate,
    Scene,
    Square,
    Transform,
    ReplacementTransform,
)


class animated_square_circle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(WHITE, opacity = 1)
        circle.set_color(BLUE)

        square = Square()
        square.set_fill(WHITE, opacity=1)
        square.set_color(PURPLE)

        self.play(Create(square))
        self.play(square.animate.rotate(PI / 4))
        self.play(Transform(square, circle))
        self.play(circle.animate.set_color(WHITE))

class different_rotations(Scene):
    def construct(self):

        left_square = Square(color = BLUE, fill_opacity = 0.5).shift(2 * LEFT)
        right_square = Square(color = PURPLE, fill_opacity = 0.5).shift(2 * RIGHT)
        
        left_circle = Circle(color = PURPLE, fill_opacity = 0.5).shift(2 * RIGHT)
        right_circle = Circle(color = BLUE, fill_opacity = 0.5).shift(2 * LEFT)

        self.play(left_square.animate.rotate(PI/4), Rotate(right_square, angle=PI), run_time=2)
        self.wait()

        self.play(Transform(left_square, right_circle), ReplacementTransform(right_square, left_circle), 
                  Rotate(right_circle, angle=PI), Rotate(left_circle, angle = PI), run_time=2)
        self.wait()


