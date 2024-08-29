from manim import *

class DerivativeDemo(Scene):
    def construct(self):
        plane = NumberPlane(x_range=[-3, 3], y_range=[-4, 14], y_length=7, x_length=6)

        graph1 = plane.plot(lambda x: x**2, x_range=[-3, 3], color=RED)
        graph1_lab = (
            MathTex("f(x) = x^2")
            .next_to(graph1, UR, buff=0.2)
            .set_color(RED)
            .scale(0.8)
        )

        k = ValueTracker(-3)

        dot1 = always_redraw(
            lambda: Dot().move_to(plane.c2p(k.get_value(), k.get_value() ** 2))
        )
        slope1 = always_redraw(
            lambda: plane.get_secant_slope_group(
                x=k.get_value(), graph=graph1, dx=0.01, secant_line_length=5
            )
        )

        self.play(
            LaggedStart(DrawBorderThenFill(plane), Create(graph1)),
            run_time=8,
            lag_ratio=1,
        )
        self.add(slope1, dot1, graph1_lab)

        self.play(k.animate.set_value(0), run_time=8, rate_func=linear)
        self.play(k.animate.set_value(3), run_time=8, rate_func=linear)

        self.wait()
