from manim import *


class MovingAngle(Scene):
    def construct(self):
        rotation_center = LEFT

        theta_tracker = ValueTracker(110)
        line1 = Line(LEFT, RIGHT)
        line_moving = Line(LEFT, RIGHT)
        line_ref = line_moving.copy()
        line_moving.rotate(
            theta_tracker.get_value() * DEGREES, about_point=rotation_center
        )
        a = Angle(line1, line_moving, radius=0.5, other_angle=False)
        tex = MathTex(r"\theta").move_to(
            Angle(
                line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )

        self.add(line1, line_moving, a, tex)
        self.wait()

        line_moving.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=rotation_center
            )
        )

        a.add_updater(
            lambda x: x.become(
                Angle(line1, line_moving, radius=0.5, other_angle=False))
        )
        tex.add_updater(
            lambda x: x.move_to(
                Angle(
                    line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
                ).point_from_proportion(0.5)
            )
        )

        self.play(theta_tracker.animate.set_value(40))
        self.play(theta_tracker.animate.increment_value(140))
        self.play(tex.animate.set_color(RED), run_time=0.5)
        self.play(theta_tracker.animate.set_value(350))


class GraphAreaPlot(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 5],
            y_range=[0, 6],
            x_axis_config={"numbers_to_include": [2, 3]},
            tips=False,
        )

        labels = ax.get_axis_labels()

        curve_1 = ax.plot(lambda x: 4 * x - x ** 2,
                          x_range=[0, 6], color=BLUE_C)
        curve_2 = ax.plot(
            lambda x: 0.8 * x ** 2 - 3 * x + 4,
            x_range=[0, 6],
            color=GREEN_B,
        )

        line_1 = ax.get_vertical_line(
            ax.input_to_graph_point(2, curve_1), color=YELLOW)
        line_2 = ax.get_vertical_line(ax.i2gp(3, curve_1), color=YELLOW)

        riemann_area = ax.get_riemann_rectangles(
            curve_1, x_range=[0.3, 0.6], dx=0.03, color=BLUE, fill_opacity=0.5)
        area = ax.get_area(
            curve_2, [2, 3], bounded_graph=curve_1, color=GREY, opacity=0.5)

        plotagem = VGroup(riemann_area, area)

        self.play(Write(ax))

        self.play(Write(labels))

        self.wait(0.5)

        self.play(Write(curve_1), Write(curve_2))

        self.wait(0.5)

        self.play(Write(line_1), Write(line_2))

        self.play(Write(plotagem))

        self.wait(2)


class IntegralRiemann(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 7],
            y_range=[-1.5, 1.5, 1],
            tips=True,
            x_length=5,
            y_length=6,
            x_axis_config={
                "numbers_to_include": np.arange(0, 3, 6)
            }
        ).shift(LEFT * 3.4 + 0.5 * DOWN)

        labels = ax.get_axis_labels()

        curve_1 = ax.plot(lambda x: np.sin(x),
                          x_range=[0, 6.2], color=BLUE_C)

        texto = Text("INTEGRAL DE RIEMANN",
                     font="Times New Roman").shift(3 * UP)

        intRiemann = MathTex(

            "\\int^{b}_{a}"

        )

        riemann_area01 = ax.get_riemann_rectangles(
            curve_1, x_range=[0, 6], dx=1, color=BLUE, fill_opacity=0.5)

        riemann_area02 = ax.get_riemann_rectangles(
            curve_1, x_range=[0, 6], dx=0.60, color=BLUE, fill_opacity=0.5)

        riemann_area03 = ax.get_riemann_rectangles(
            curve_1, x_range=[0, 6], dx=0.25, color=BLUE, fill_opacity=0.5)

        riemann_area04 = ax.get_riemann_rectangles(
            curve_1, x_range=[0, 6], dx=0.1, color=BLUE, fill_opacity=0.5)

        riemann_area05 = ax.get_riemann_rectangles(
            curve_1, x_range=[0, 6], dx=0.03, color=BLUE, fill_opacity=0.5)

        plotagem = VGroup(texto, ax, labels)

        self.play(Write(plotagem))

        self.wait(0.5)

        self.play(Write(curve_1))

        self.wait(0.5)

        self.play(Write(riemann_area01))

        self.wait(0.5)

        self.play(FadeOut(riemann_area01))

        self.wait(0.5)

        self.play(Write(riemann_area02))

        self.wait(0.5)

        self.play(FadeOut(riemann_area02))

        self.wait(0.5)

        self.play(Write(riemann_area03))

        self.wait(0.5)

        self.play(FadeOut(riemann_area03))

        self.wait(0.5)

        self.play(Write(riemann_area04))

        self.wait(0.5)

        self.play(FadeOut(riemann_area04))

        self.wait(0.5)

        self.play(Write(riemann_area05))

        self.wait()
