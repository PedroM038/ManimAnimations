from manim import *

class MoveBox(Scene):
    def construct(self):
        box = Rectangle(stroke_color = GREEN_C, stroke_opacity = 0.7,
                        fill_color = RED_B, fill_opacity = 0.7, height = 1, width = 1)
        
        self.add(box)
        self.play(box.animate.shift(RIGHT*2), run_time = 2)
        self.play(box.animate.shift(LEFT*2), run_time = 2)
        self.play(box.animate.shift(UP*2), run_time = 2)
        self.play(box.animate.shift(DOWN*2), run_time = 2)

class AxesCircleToTriangle(Scene):
    def construct(self):
        
        axes = Axes(x_range = [-3, 3, 1], y_range = [-3,3,1],
                    x_length = 6, y_length = 6)
        axes.to_edge(LEFT, buff = 0.5)
        
        circle = Circle(stroke_width = 6, stroke_color = YELLOW,
                        fill_color = RED_C, fill_opacity = 0.8)
        circle.set_width(2).to_edge(DR, buff=0)

        triangle = Triangle(stroke_width = 10, stroke_color = ORANGE,
                        fill_color = GREY).set_height(2).shift(DOWN*3 + RIGHT*3)
        
        self.play(Write(axes))
        self.play(DrawBorderThenFill(circle))
        self.play(circle.animate.set_width(1))
        self.play(Transform(circle, triangle), run_time=3)

class Updaters(Scene):
    def construct(self):

        rectangle = RoundedRectangle(stroke_width = 8, stroke_color = WHITE,
                                     fill_color = BLUE_B, width = 4.5, height = 2).shift(UP*3+LEFT*4)
        
        mathtext = MathTex("\\frac{3}{4} = 0.75").set_color_by_gradient(GREEN, PINK).set_height(1.5)
        mathtext.move_to(rectangle.get_center())
        mathtext.add_updater(lambda x : x.move_to(rectangle.get_center()))

        self.play(FadeIn(rectangle))
        self.play(Write(mathtext))
        self.play(rectangle.animate.shift(RIGHT * 1.5 + DOWN * 5), run_time = 6)
        self.wait()
        self.play(rectangle.animate.shift(LEFT * 2 + UP * 2), run_time = 6)
        self.play(rectangle.animate.shift(RIGHT * 4 + DOWN * 2), run_time = 7)

class Tute4(Scene):
    def construct(self):

        r = ValueTracker(0.5)

        circle = always_redraw(lambda :
            Circle(radius = r.get_value(), stroke_color = YELLOW,
            stroke_width = 5))

        line_radius = always_redraw(lambda :
            Line(start = circle.get_center(), end = circle.get_bottom(), stroke_color = RED_B, stroke_width = 10))

        line_circumference = always_redraw(lambda :
            Line(stroke_color = YELLOW, stroke_width = 5)
            .set_length(2 * r.get_value() * PI).next_to(circle, DOWN, buff = 0.2))

        triangle = always_redraw(lambda :
            Polygon(circle.get_top(), circle.get_left(), circle.get_right(), fill_color = GREEN_C))

        self.play(LaggedStart(
            Create(circle), DrawBorderThenFill(line_radius), DrawBorderThenFill(triangle),
            run_time = 4, lag_ratio = 0.75))
        self.play(ReplacementTransform(circle.copy(), line_circumference), run_time = 2)
        self.play(r.animate.set_value(2), run_time = 5)

