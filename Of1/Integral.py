from manim import (PURPLE, UR, WHITE, Axes, Create, DrawBorderThenFill,
                   LaggedStart, MathTex, Scene, Tex, Transform, VGroup)


class IntegralDemo(Scene):
    def integral_func_1(self):
        axes = Axes(x_range=[-5, 5], x_length=8, y_range=[-10, 10], y_length=7)

        label_axes = axes.get_axis_labels(Tex("x").scale(1), Tex("y").scale(1))

        graph = axes.plot(
            lambda x: 0.1 * (x - 4) * (x - 1) * (x + 3), x_range=[-5, 5], color=PURPLE
        )

        graph_lab = (
            MathTex("y = f(x)").next_to(graph, UR, buff=0.5).set_color(PURPLE).scale(1)
        )

        self.play(
            LaggedStart(DrawBorderThenFill(axes)),
            Create(label_axes),
            run_time=5,
            lag_ratio=1,
        )

        self.play(Create(graph), Create(graph_lab), run_time=3)

        self.wait(1)

        dx_list = [1, 0.5, 0.3, 0.1, 0.05, 0.025, 0.01, 0.005]
        rectangles = VGroup(
            *[
                axes.get_riemann_rectangles(
                    graph=graph,
                    x_range=[-5, 5],
                    stroke_width=0.1,
                    stroke_color=WHITE,
                    dx=dx,
                )
                for dx in dx_list
            ]
        )
        first_area = rectangles[0]
        self.play(Create(first_area), run_time=2)

        for k in range(1, len(dx_list)):
            new_area = rectangles[k]
            self.play(Transform(first_area, new_area), run_time=3)
            self.wait(2)

        self.wait()

    def integral_func_2(self):
        axes = Axes(x_range=[-5, 5], x_length=8, y_range=[-5, 15], y_length=7)

        label_axes = axes.get_axis_labels(Tex("x").scale(1), Tex("y").scale(1))

        graph = axes.plot(
            lambda x: 0.5 * x * x, x_range=[-5, 5], color=PURPLE
        )

        graph_lab = (
            MathTex("y = x^2").next_to(graph, UR, buff=0.5).set_color(PURPLE).scale(1)
        )

        self.play(
            LaggedStart(DrawBorderThenFill(axes)),
            Create(label_axes),
            run_time=5,
            lag_ratio=1,
        )

        self.play(Create(graph), Create(graph_lab), run_time=3)

        self.wait(1)

        dx_list = [1, 0.5, 0.3, 0.1, 0.05, 0.025, 0.01, 0.005]
        rectangles = VGroup(
            *[
                axes.get_riemann_rectangles(
                    graph=graph,
                    x_range=[-5, 5],
                    stroke_width=0.1,
                    stroke_color=WHITE,
                    dx=dx,
                )
                for dx in dx_list
            ]
        )
        first_area = rectangles[0]
        self.play(Create(first_area), run_time=2)

        for k in range(1, len(dx_list)):
            new_area = rectangles[k]
            self.play(Transform(first_area, new_area), run_time=3)
            self.wait(2)

        self.wait()

    def construct(self):
        self.integral_func_1()
        self.clear()
        self.wait()
        self.integral_func_2()
        self.clear()
        self.wait()
