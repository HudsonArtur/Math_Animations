from manim import *

class maxwellPaper(Scene):
    def construct(self):
        texto = Text("E Deus disse...").shift(UP*3 + LEFT*4)

        gausLaw = MathTex(
        
            "\oint \\vec{E} \cdot d\\vec{A} = \dfrac{Q_{int}}{\epsilon_0}"
        
        ).shift(UP*2 + LEFT)

        gausLawMagnetismo = MathTex(

            "\oint \\vec{B} \cdot d\\vec{A} = 0"

        ).next_to(gausLaw, DOWN)

        faradayLawInducao = MathTex(

            "\oint \\vec{E} \cdot d\\vec{s} = -\dfrac{d\phi_B}{dt}"

        ).next_to(gausLawMagnetismo, DOWN)

        ampereLaw = MathTex(

            "\oint \\vec{B} \cdot d\\vec{s} = \mu_0 \epsilon_0 \dfrac{d\phi_E}{dt} + \mu_0I"

        ).next_to(faradayLawInducao, DOWN)

        texto02 = Text("...e houve luz.").next_to(ampereLaw, DOWN+RIGHT)

        equacoesMaxwell = VGroup(gausLaw, gausLawMagnetismo, faradayLawInducao, ampereLaw)

        self.play(Write(texto))
        self.play(Write(equacoesMaxwell))
        self.play(Write(texto02))

        self.wait(2)
