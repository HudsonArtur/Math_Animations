from manim import *


class MovingFrameBox(Scene):
    def construct(self):

        textoTransformada = Text(
            "Transformada de Fourier", font="Times New Roman", slant=ITALIC).shift(UP * 0.8)
        fourierTransf = MathTex(

            "X(\\omega)", "=\\int^{\\infty}_{-\\infty}", "x(t)", "e^{-j \\omega t}dt"

        ).shift(DOWN * 0.8)

        textoIntegral = Text(
            "Integral de Fourier", font="Times New Roman", slant=ITALIC).shift(UP * 0.8)
        fourierInt = MathTex(

            "x(t)", "= \\frac{1}{2\\pi} \\int^{\\infty}_{-\\infty}", "X(\\omega)", "e^{j\\omega t}d\\omega"

        ).shift(DOWN * 0.8)

        self.play(Write(textoTransformada), Write(fourierTransf))
        # framebox1 = SurroundingRectangle(text[0], buff=.1)
        # framebox2 = SurroundingRectangle(text[1], buff=.1)

        # xOmega = fourierTransf[0]
        # xTtransfor = fourierTransf[2]

        # xT = fourierInt[0]
        # xOmegaFourierInt = fourierInt[2]

        # intFourierTrans = fourierTransf[1]
        # intFourierInt = fourierInt[1]

        # eulerTransfor = fourierTransf[3]
        # eulerInt = fourierInt[3]

        self.wait()
        self.play(
            ReplacementTransform(textoTransformada, textoIntegral),
            TransformMatchingTex(fourierTransf, fourierInt)
        )
        self.wait()


class Move(Scene):
    def construct(self):
        equation = MathTex("dA", "\\approx", "x^{2}", "dx")
        # equation.to_edge(RIGHT).shift(3*UP)
        deriv_equation = MathTex(
            "{dA", "\\over \\,", "dx}", "\\approx", "x^{2}"
        )
        deriv_equation.move_to(equation, UP+LEFT)

        self.play(*[
            ReplacementTransform(
                equation.get_part_by_tex(tex),
                deriv_equation.get_part_by_tex(tex),
                run_time=2,
            )
            for tex in ("dA", "approx", "x^{2}", "dx")
        ] + [
            Write(deriv_equation.get_part_by_tex("over"))
        ])


class SinAndCosFunctionPlot(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-10, 10.3, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-10, 10.01, 2),
                "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            },
            tips=False,
        )
        axes_labels = axes.get_axis_labels()
        sin_graph = axes.plot(lambda x: np.sin(x), color=BLUE)
        cos_graph = axes.plot(lambda x: np.cos(x), color=RED)

        sin_label = axes.get_graph_label(
            sin_graph, "\\sin(x)", x_val=-10, direction=UP / 2
        )
        cos_label = axes.get_graph_label(cos_graph, label="\\cos(x)")

        vert_line = axes.get_vertical_line(
            axes.i2gp(TAU, cos_graph), color=YELLOW, line_func=Line
        )
        line_label = axes.get_graph_label(
            cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
        )

        plot = VGroup(sin_graph, cos_graph)
        labels = VGroup(sin_label, cos_label, vert_line, line_label)
        self.play(Write(axes))

        self.play(Write(axes_labels))

        self.play(Write(plot), run_time=5)

        self.play(Write(labels))

        self.wait()


class MatchingEquationParts(Scene):
    def construct(self):
        variables = VGroup(MathTex("a"), MathTex(
            "b"), MathTex("c")).arrange_submobjects().shift(UP)

        eq1 = MathTex("{{x}}^2", "+", "{{y}}^2", "=", "{{z}}^2")
        eq2 = MathTex("{{a}}^2", "+", "{{b}}^2", "=", "{{c}}^2")
        eq3 = MathTex("{{a}}^2", "=", "{{c}}^2", "-", "{{b}}^2")

        self.add(eq1)
        self.wait(0.5)
        self.play(TransformMatchingTex(Group(eq1, variables), eq2))
        self.wait(0.5)
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait(0.5)


class GetAxisLabelsExample(Scene):
    def construct(self):
        ax = Axes().add_coordinates()
        labels = ax.get_axis_labels(
            Tex("x").scale(0.7), Text("y").scale(0.45)
        )
        self.play(Write(ax))

        self.play(Write(labels))


class LogScalingExample(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[-2, 6, 1],
            # tips=False,
            axis_config={"include_numbers": True},
            y_axis_config={"scaling": LogBase(custom_labels=True)},
        )
        labels = ax.get_axis_labels(
            MathTex("x").scale(1), MathTex("y").scale(1)
        )

        # x_min must be > 0 because log is undefined at 0.
        graph = ax.plot(lambda x: x ** 2,
                        x_range=[0.001, 10], use_smoothing=False)
        self.play(Write(ax))

        self.play(Write(labels))

        self.play(Write(graph))

        self.wait(2)
