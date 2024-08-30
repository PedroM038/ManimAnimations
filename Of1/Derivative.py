from manim import (
    BLUE, DOWN, GREEN_B, RED, RIGHT, UR, WHITE, Axes, Create, Dot,
    DrawBorderThenFill, FadeOut, LaggedStart, Line, MathTex,
    NumberPlane, Scene, Transform, ValueTracker, VGroup,
    Write, always_redraw, linear, smooth
)

class DerivativeDemo(Scene):
    def construct(self):
        # Creating the coordinate plane
        plane = NumberPlane(x_range=[-3, 3], y_range=[-4, 14], y_length=7, x_length=6)

        # Creating the quadratic function
        graph1 = plane.plot(lambda x: x**2, x_range=[-3, 3], color=RED)
        graph1_lab = (
            MathTex("f(x) = x^2").next_to(graph1, UR, buff=1).set_color(RED).scale(0.8)
        )

        # Creating the ValueTracker for the secant line animation
        k = ValueTracker(-3)

        # Points of the secant line
        dot1 = always_redraw(
            lambda: Dot().move_to(plane.c2p(k.get_value(), k.get_value() ** 2))
        )

        # Secant line and its labels
        slope1 = always_redraw(
            lambda: plane.get_secant_slope_group(
                x=k.get_value(),
                graph=graph1,
                dx=0.01,
                dx_label=MathTex(r"\Delta x"),
                dy_label=MathTex(r"\Delta y"),
                dx_line_color=GREEN_B,
                secant_line_length=4,
                secant_line_color=BLUE,
            )
        )

        slope_lab = always_redraw(
            lambda: MathTex("r")
            .next_to(slope1.secant_line, RIGHT, buff=0.2)
            .set_color(BLUE)
            .scale(0.8)
        )

        # Initial animation: Drawing the function and the secant line
        self.play(
            LaggedStart(DrawBorderThenFill(plane), Create(graph1), Create(graph1_lab)),
            run_time=8,
            lag_ratio=1,
        )
        self.add(slope1, slope_lab, dot1)

        self.play(k.animate.set_value(0), run_time=8, rate_func=smooth)
        self.play(k.animate.set_value(3), run_time=8, rate_func=smooth)

        self.wait()

        self.play(k.animate.set_value(0), run_time=8, rate_func=linear)

        # FadeOut to clear the screen
        self.play(
            FadeOut(VGroup(plane, graph1, graph1_lab, dot1, slope_lab, slope1)),
            run_time=2,
        )

        # Creating a new line at the top of the screen
        line_r = Line(start=plane.c2p(-3, 10), end=plane.c2p(3, 10), color=BLUE)
        line_r_label = (
            MathTex(r"r = mx + b").next_to(line_r, DOWN, buff=0.5).set_color(BLUE)
        )

        self.play(Create(line_r), Write(line_r_label))
        self.wait(3)

        # Showing the slope formula (m)
        delta_formula = (
            MathTex(r"m = \frac{\Delta y}{\Delta x}")
            .next_to(line_r_label, DOWN, buff=0.5)
            .set_color(WHITE)
        )
        self.play(Write(delta_formula))
        self.wait(3)

        # Transforming into the general slope formula
        point_formula = (
            MathTex(r"m = \frac{y - y_0}{x - x_0}")
            .next_to(delta_formula, DOWN, buff=0.5)
            .set_color(WHITE)
        )
        self.play(Transform(delta_formula, point_formula))
        self.wait(3)

        # FadeOut of the line and formulas
        self.play(FadeOut(VGroup(line_r, delta_formula, point_formula, line_r_label)))

        axes = Axes(y_range=[-1, 12])
        graph2 = axes.plot(lambda x: 1 / 4 * x * x, color=BLUE)
        graph2_lab = (
            MathTex("f(x) = x^2").next_to(graph2, UR, buff=1).set_color(BLUE).scale(0.8)
        )

        # Recreating the quadratic function
        self.play(DrawBorderThenFill(axes), Create(graph2), Create(graph2_lab))

        k = ValueTracker(3)
        d = ValueTracker(3)

        slope2 = always_redraw(
            lambda: axes.get_secant_slope_group(
                x=k.get_value(),
                graph=graph2,
                dx=d.get_value(),
                dx_label=MathTex(r"\Delta x"),
                dy_label=MathTex(r"\Delta y"),
                dx_line_color=GREEN_B,
                secant_line_length=4,
                secant_line_color=RED,
            )
        )

        self.add(slope2)
        self.play(k.animate.set_value(0), run_time=12, rate_func=smooth)
        self.play(d.animate.set_value(0.1), run_time=8, rate_func=smooth)
        self.play(k.animate.set_value(-3), run_time=4, rate_func=smooth)
        self.wait(2)

