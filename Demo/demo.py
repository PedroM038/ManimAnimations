from manim import * 
                


class DerivativeDemo(Scene):
    def construct(self):

        plane = NumberPlane(
            x_range=[-3, 3],
            y_range=[-4, 14],
            y_length=7,
            x_length=6
        )

        graph1 = plane.plot(lambda x: x ** 2, x_range=[-3, 3], color=RED)
        graph1_lab = MathTex("f(x) = x^2").next_to(graph1, UR, buff=0.2).set_color(RED).scale(0.8)

        k = ValueTracker(-3)

        dot1 = always_redraw(lambda: Dot().move_to(plane.c2p(k.get_value(), k.get_value()**2)))
        slope1 = always_redraw(lambda: plane.get_secant_slope_group(
            x=k.get_value(), graph=graph1, dx=0.01, secant_line_length=5
        ))

        self.play(LaggedStart(DrawBorderThenFill(plane), Create(graph1)), run_time=8, lag_ratio=1)
        self.add(slope1, dot1, graph1_lab)

        self.play(k.animate.set_value(0), run_time=8, rate_func=linear)
        self.play(k.animate.set_value(3), run_time=8, rate_func=linear)

        self.wait()

class IntegralDemo(Scene):
    def construct(self):

        axes = Axes(x_range = [-5, 5], x_length = 8, y_range = [-10, 10], y_length = 7)

        graph = axes.plot(lambda x: 0.1 * (x - 4) * (x - 1) * (x + 3), x_range = [-5, 5], color = YELLOW)
        self.add(axes, graph)

        dx_list = [1, 0.5, 0.3, 0.1, 0.05, 0.025, 0.01]
        rectangles = VGroup(
                    *[
                        axes.get_riemann_rectangles(
                            graph = graph,
                            x_range = [-5, 5],
                            stroke_width = 0.1,
                            stroke_color = WHITE,
                            dx = dx,
                        )
                        for dx in dx_list
                    ])
        first_area = rectangles[0]
        for k in range(1, len(dx_list)):
            new_area = rectangles[k]
            self.play(Transform(first_area, new_area), run_time = 4)
            self.wait(1)

        self.wait()
                   
class SineCosineDemo(Scene):
    def construct(self):
        self.show_axis()
        self.show_circle()
        self.move_dot_and_draw_curve()

        self.wait()

    def show_axis(self):
        x_start = np.array([-6,2,0])
        x_end = np.array([3,2,0])

        y_start = np.array([-4,-3,0])
        y_end = np.array([-4,3.5,0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        self.add(x_axis, y_axis)
        self.add_xy_labels()

        self.orgin_point = np.array([-4,2,0])
        self.curve_start = np.array([-3,2,0])

    def add_xy_labels(self):
        x_labels = [
            MathTex("\pi"), MathTex("2 \pi"),
            MathTex("3 \pi"), MathTex("4 \pi"),
        ]

        y_labels = [
            MathTex("\pi"), MathTex("2 \pi"),
            MathTex("3 \pi"), MathTex("4 \pi"),
        ]

        for i in range(len(x_labels)):  # -2 -1 0 1
            x_labels[i].scale(0.6)
            x_labels[i].next_to(np.array([-2+i,2,0]), DOWN )
            self.add(x_labels[i])

        for i in range(len(y_labels)):  # 1 0 -1 -2
            y_labels[i].scale(0.6)
            y_labels[i].rotate(-PI/2)
            y_labels[i].next_to(np.array([-4, 1-i,0]), LEFT )
            self.add(y_labels[i])

    def show_circle(self):
        circle = Circle(radius=1)
        circle.move_to(self.orgin_point)

        self.add(circle)
        self.circle = circle

    def move_dot_and_draw_curve(self):
        orbit = self.circle
        orgin_point = self.orgin_point

        dot = Dot(radius=0.08, color=YELLOW)
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.25

        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            # print(self.t_offset)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        def get_line_to_circle():
            return Line(orgin_point, dot.get_center(), color=BLUE)

        ### sine
        def get_line_to_sine():
            x = self.curve_start[0] + self.t_offset * 2
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2 )

        self.sine_curve = VGroup()
        self.sine_curve.add(Line(self.curve_start,self.curve_start))
        def get_sine_curve():
            last_line = self.sine_curve[-1]
            x = self.curve_start[0] + self.t_offset * 2
            y = dot.get_center()[1]
            new_line = Line(last_line.get_end(),np.array([x,y,0]), color=YELLOW_D)
            self.sine_curve.add(new_line)

            return self.sine_curve

        ### cosine
        def get_line_to_cosine():
            x = dot.get_center()[0]
            y = self.curve_start[1] - self.t_offset * 2
            return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2 )

        self.cosine_curve = VGroup()
        self.cosine_curve.add(Line(self.curve_start, self.curve_start))

        def get_cosine_curve():
            last_line = self.cosine_curve[-1]
            x = dot.get_center()[0]
            y = self.curve_start[1] - self.t_offset * 2
            new_line = Line(last_line.get_end(), np.array([x, y, 0]), color=YELLOW_D)
            self.cosine_curve.add(new_line)

            return self.cosine_curve


        dot.add_updater(go_around_circle) #move dot around the circle

        origin_to_circle_line = always_redraw(get_line_to_circle) # from circle origin to dot

        dot_to_sine_line = always_redraw(get_line_to_sine) # from dot to sine curve
        sine_curve_line = always_redraw(get_sine_curve) # sine curve

        dot_to_cosine_line = always_redraw(get_line_to_cosine)  # from dot to cosine curve
        cosine_curve_line = always_redraw(get_cosine_curve)  # cosine curve

        self.add(dot, orbit)
        self.add(origin_to_circle_line,
                 dot_to_sine_line, sine_curve_line,
                 dot_to_cosine_line, cosine_curve_line,
         )
        self.wait(10)

        dot.remove_updater(go_around_circle)
