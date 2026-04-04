from manim import *

class MatchingEquationParts(Scene):
    def construct(self):
        variables = VGroup(MathTex("a"), MathTex(
            "b"), MathTex("c")).arrange_submobjects().shift(UP)

        eq1 = MathTex("{{x}}^2", "+", "{{y}}^2", "=", "{{z}}^2")
        eq2 = MathTex("{{a}}^2", "+", "{{b}}^2", "=", "{{c}}^2")
        eq3 = MathTex("{{a}}^2", "=", "{{c}}^2", "-", "{{b}}^2")

        self.play(Write(eq1))
        self.wait(0.5)
        self.play(TransformMatchingTex(Group(eq1, variables), eq2))
        self.wait(0.5)
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait(0.5)

class circuitoColorido(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american]{circuitikz}")

        c = MathTex(
            r"""\draw (0,0) to[isource, l=$I_0$, v=$V_0$] (0,3);""", 
            r"""\draw (0,3) to[short, -*] (2,3);""",
            r"""\draw (2,3) to[R=$R_1$, i>_=$I_1$] (2,0);""",
            r"""\draw (2,3) -- (4,3);""", 
            r"\draw (4,3) to[R=$R_2$, i>_=$I_2$] (4,0);",
            r"\draw (4,0) to[short, -*] (2,0)--(0,0);"
            , stroke_width=4
            , fill_opacity=0
            , stroke_opacity=1
            , tex_environment="circuitikz"
            , tex_template=template
            
            )
        # for cir, clr in zip(c[0,4],[RED, GREEN, BLUE, YELLOW]):
        #     cir.set_color(clr)
        c.set_color_by_tex_to_color_map({"I_0":RED, "R_1":YELLOW, "R_2":BLUE})

        self.play(FadeIn(c, shift=UP, target_position=ORIGIN), run_time=3)
        self.play(ApplyWave(c[0]))
        self.play(Indicate(c[2], color=TEAL), run_time=2) 
        self.play(Circumscribe(c[4], fade_out=True, color=BLUE))
        self.wait(2)
        
class circuitoLegal(Scene):
    def construct(self):
        templete = TexTemplate()
        templete.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american]{circuitikz}")

        c = MathTex(
            r"""\draw (0,0) to [V=$6V$] (0,3)
                node[above]{$V_1$} to [short, -*, R=$2k\Omega$] (3,3)
                node[above]{$V_2$} to [V=$12V$] (5.5,3)
                to [short, -*] (6,3)
                node[above]{$V_3$} to [R=$2k\Omega$] (9,3)
                node[above]{$V_4$} to [V=$4V$] (9,0)
                to [short, -*] (6,0) to [short, -*] (3,0)
                node[ground]{} -- (0,0);""",    
            r"""\draw (3,3) to [R=$1k\Omega$] (3,0);"""
            r"""\draw (6,3) to [R=$2k\Omega$, i=$I_0$] (6,0);"""
            , stroke_width=2
            , fill_opacity=0
            , stroke_opacity=1
            , tex_environment="circuitikz"
            , tex_template=templete
        )
        c.scale_to_fit_width(width=12)
        self.play(Write(c))
        self.wait(3)

#class somaSimples(Scene):
#    def construct(self):
        