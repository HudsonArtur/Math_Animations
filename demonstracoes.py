from manim import *


class bhaskara(Scene):
    def construct(self):

        apresentacao = Text("Demonstração da fórmula de Bhaskara",
                            font="Times New Roman").shift(UP * 3)

        eqBhaskara = MathTex(

            "\\dfrac{-b\\pm\\sqrt{b^2 - 4ac}}{2a}"

        ).scale(2)

        intro = VGroup(apresentacao, eqBhaskara)

        eq2_Grau01 = MathTex(
            "a", "x^{2}", "+ bx", "+", "c", "= 0"
        )

        eq2_Grau02 = MathTex(
            "a", "x^{2}", "+ bx", " = -", "c"
        )

        eq2_Grau03 = MathTex(
            "x^{2}", "+ \\frac{bx}{", "a", "}", "= -\\frac{c}{", "a", "}"
        )

        eq2_Graus04 = MathTex(
            "x^{2}", "+ \\frac{bx}{", "a", "}", "+\\bigg(\\frac{b}{a}\\cdot \\frac{1}{2}\\bigg)^{2}",
            "= -\\frac{c}{", "a", "}", "+\\bigg(\\frac{b}{a}\\cdot \\frac{1}{2}\\bigg)^{2}"
        )

        eq2_Graus05 = MathTex(
            "x^{2}", "+ \\frac{bx}{", "a", "}", "+\\frac{b^{2}}{4a}",
            "= -\\frac{c}{", "a", "}", "+ \\frac{b^{2}}{4a}"
        )

        eq2_Graus06 = MathTex(
            "x^{2}", "+ \\frac{bx}{", "a", "}", "+\\frac{b^{2}}{4a}",
            "= -\\frac{c}{", "a", "}", "\\cdot \\frac{4a}{4a}", "+ \\frac{b^{2}}{4a}"
        )

        eq2_Graus07 = MathTex(
            "x^{2}", "+ \\frac{bx}{", "a", "}", "+\\frac{b^{2}}{4a}",
            "= -\\frac{4ac}{", "4a^{2}", "}", "+ \\frac{b^{2}}{4a}"
        )

        eq2_Graus08 = MathTex(
            "x^{2}", "+ \\frac{bx}{", "a", "}", "+\\frac{b^{2}}{4a}",
            "= \\frac{b^{2} - 4ac}{", "4a^{2}", "}"
        )

        eq2_Graus09 = MathTex(
            "\\bigg(x", "+ \\frac{b}{", "2a", "}\\bigg)^{2}",
            "= \\frac{b^{2} - 4ac}{", "4a^{2}", "}"
        )

        eq2_Graus10 = MathTex(
            "\\sqrt{\\bigg(x", "+ \\frac{b}{", "2a", "}\\bigg)^{2}}",
            "= \\pm \\sqrt{\\frac{b^{2} - 4ac}{", "4a^{2}", "}", "}"
        )

        eq2_Graus11 = MathTex(
            "x", "+ \\frac{b}{", "2a", "}",
            "= \\frac{\\pm \\sqrt{b^{2} - 4ac}}{", "2a", "}"
        )

        eq2_Graus12 = MathTex(
            "x", "=", "- \\frac{b}{", "2a", "}",
            "\\frac{\\pm \\sqrt{b^{2} - 4ac}}{", "2a", "}"
        )

        eq2_Graus13 = MathTex(
            "x", "=", "\\frac{-b \\pm \\sqrt{b^{2} - 4ac}}{", "2a", "}"
        )

        self.play(Write(intro))

        self.play(Circumscribe(eqBhaskara))

        self.wait()

        self.play(FadeOut(intro))

        self.next_section("Demonstracao_P1")

        self.play(Write(eq2_Grau01))

        self.wait(0.5)

        self.play(
            TransformMatchingTex(eq2_Grau01, eq2_Grau02)
        )

        self.wait(0.5)

        self.play(
            TransformMatchingTex(eq2_Grau02, eq2_Grau03)
        )

        self.wait(0.5)

        self.play(
            TransformMatchingTex(eq2_Grau03, eq2_Graus04)
        )

        self.wait(0.5)

        self.play(
            ReplacementTransform(eq2_Graus04, eq2_Graus05)
        )

        self.wait(0.5)

        self.next_section("Demonstracao_P2")

        self.play(
            TransformMatchingTex(eq2_Graus05, eq2_Graus06)
        )

        self.wait(0.5)

        self.play(
            TransformMatchingTex(eq2_Graus06, eq2_Graus07)
        )

        self.wait(0.5)

        self.play(
            TransformMatchingTex(eq2_Graus07, eq2_Graus08)
        )

        self.wait(0.5)

        self.play(
            TransformMatchingTex(eq2_Graus08, eq2_Graus09)
        )

        self.wait(0.5)

        self.play(
            TransformMatchingTex(eq2_Graus09, eq2_Graus10)
        )

        self.wait(0.5)

        self.next_section("Demonstracao_P3")

        self.play(
            TransformMatchingTex(eq2_Graus10, eq2_Graus11)
        )

        self.wait(0.5)

        self.play(
            TransformMatchingTex(eq2_Graus11, eq2_Graus12)
        )

        self.wait(0.5)

        self.play(
            TransformMatchingTex(eq2_Graus12, eq2_Graus13),
        )

        self.wait(0.5)

        self.play(Circumscribe(eq2_Graus13))

        self.wait()

        texto = Text(
            "Demonstração realizada no Manim\nPor Hudson Artur",
            font="Times New Roman", color=BLUE
        ).shift(2.5 * DOWN + 1.5*LEFT)

        self.play(Write(texto))

        self.wait()
