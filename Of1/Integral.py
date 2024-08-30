from manim import (
    PURPLE,
    UR,
    WHITE,
    Axes,
    Create,
    DrawBorderThenFill,
    LaggedStart,
    MathTex,
    Scene,
    Tex,
    Transform,
    VGroup,
)


class IntegralDemo(Scene):
    def create_graph_with_rectangles(
        self, axes, func, func_label, graph_color, x_range, y_range, dx_list
    ):
        """
        Create a graph of a function and animate the approximation of the integral
        using Riemann rectangles with decreasing dx values.

        Parameters:
        axes (Axes): The axes on which to plot the graph.
        func (function): The mathematical function to plot.
        func_label (str): The label for the function.
        graph_color (color): The color of the graph.
        x_range (list): The x-range for the plot.
        y_range (list): The y-range for the plot.
        dx_list (list): List of dx values for the Riemann rectangles.
        """
        # Create the graph
        graph = axes.plot(func, x_range=x_range, color=graph_color)

        # Create the label for the graph
        graph_lab = (
            MathTex(func_label)
            .next_to(graph, UR, buff=0.5)
            .set_color(graph_color)
            .scale(1)
        )

        # Animate the creation of axes, labels, and graph
        label_axes = axes.get_axis_labels(Tex("x").scale(1), Tex("y").scale(1))
        self.play(
            LaggedStart(DrawBorderThenFill(axes)),
            Create(label_axes),
            run_time=5,
            lag_ratio=1,
        )
        self.play(Create(graph), Create(graph_lab), run_time=3)
        self.wait(1)

        # Create Riemann rectangles for different dx values
        rectangles = VGroup(
            *[
                axes.get_riemann_rectangles(
                    graph=graph,
                    x_range=x_range,
                    stroke_width=0.1,
                    stroke_color=WHITE,
                    dx=dx,
                )
                for dx in dx_list
            ]
        )

        # Animate the transformation of the rectangles
        first_area = rectangles[0]
        self.play(Create(first_area), run_time=2)
        for k in range(1, len(dx_list)):
            new_area = rectangles[k]
            self.play(Transform(first_area, new_area), run_time=3)
            self.wait(2)

        self.wait()

    def construct(self):
        # Set up the axes and dx_list for both functions
        axes1 = Axes(x_range=[-5, 5], x_length=8, y_range=[-10, 10], y_length=7)
        axes2 = Axes(x_range=[-5, 5], x_length=8, y_range=[-5, 15], y_length=7)
        dx_list = [1, 0.5, 0.3, 0.1, 0.05, 0.025, 0.01, 0.005]

        # Function 1: f(x) = 0.1 * (x - 4) * (x - 1) * (x + 3)
        self.create_graph_with_rectangles(
            axes=axes1,
            func=lambda x: 0.1 * (x - 4) * (x - 1) * (x + 3),
            func_label="y = f(x)",
            graph_color=PURPLE,
            x_range=[-5, 5],
            y_range=[-10, 10],
            dx_list=dx_list,
        )

        # Clear the scene before the next graph
        self.clear()
        self.wait()

        # Function 2: y = 0.5 * x^2
        self.create_graph_with_rectangles(
            axes=axes2,
            func=lambda x: 0.5 * x * x,
            func_label="y = x^2",
            graph_color=PURPLE,
            x_range=[-5, 5],
            y_range=[-5, 15],
            dx_list=dx_list,
        )

        # Clear the scene at the end
        self.clear()
        self.wait()
