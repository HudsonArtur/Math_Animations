from manim import *
import numpy as np

class descargaCapacitor(Scene):
    def construct(self):
        templete = TexTemplate()
        templete.add_to_preamble(r"\usepackage[siunitx, straight voltages, american]{circuitikz}")

        c = MathTex(   
            r"""=\draw (0,0) to [battery2, l_=$V_0 {=}100V$, invert] (0,3) 
            to [short, nos] (2,3)
            to [short, i=$I$] (3,3)
            to [R=$R{=}100k\Omega$, v<=$V_R$] (5,3)
            to [C=$C{=}10\mu F$, v<=$V_C$] (5,0) 
            to [short, -] (2,0) -- (0,0);"""
            , stroke_width=2
            , fill_opacity=0
            , stroke_opacity=1
            , tex_environment="circuitikz"
            , tex_template=templete
        ).shift(LEFT*2.5)

        ax = Axes(
            x_range=[0, 11, 1],
            y_range=[0, 120, 20],
            tips=True,
            x_length=5,
            y_length=5,
            x_axis_config={"numbers_to_include": np.arange(0, 11, 1)},
            y_axis_config={"numbers_to_include": np.arange(0, 120, 20)},
        ).shift(RIGHT*4.5)

        label_Y = ax.get_y_axis_label(label="Voltagem[V]").shift(LEFT*1.5)
        label_X = ax.get_x_axis_label(label="Tempo[s]").shift(DOWN*1.6+LEFT)

        plotGrafico = VGroup(ax, label_X, label_Y)
        
        textoGrafico = Text("Carga/Descarga").shift(UP*3+RIGHT*3.2).scale(0.8)
        textoCircuito = Text("Circuito Elétrico").shift(UP*3+LEFT*3.2).scale(0.8)

        parteCircuito = VGroup(c, textoCircuito)
        parteGrafico = VGroup(plotGrafico, textoGrafico)

        c.scale_to_fit_width(width=6)
        plotGrafico.scale(0.8)

        self.play(FadeIn(parteCircuito))
        self.play(FadeIn(parteGrafico))
        self.wait(3)

class grafico(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 11, 1],
            y_range=[0, 120, 20],
            tips=True,
            x_length=7,
            y_length=5,
            x_axis_config={"numbers_to_include": np.arange(0, 11, 1)},
            y_axis_config={"numbers_to_include": np.arange(0, 120, 20)},
        ).shift(LEFT*2)

        # Parâmetros do circuito
        C = 10e-6  # Capacitância (10 microfarads)
        V = 100.0  # Tensão da fonte
        R = 100e3  # Resistência (100 kiloohms)

        # Constante de tempo (tau)
        tau = R * C

        # Carga do capacitor
        q_carga = ax.plot(lambda x: V * (1 - np.exp(-x / tau)), color=YELLOW, x_range=[0,10])
        
        # Descarga do capacitor
        q_descarga = ax.plot(lambda x: V * (np.exp(-x / tau)), color=BLUE, x_range=[0,10])

        plotagemGrafico = VGroup(q_carga, q_descarga)

        label_Y = ax.get_y_axis_label(label="Voltagem[V]").shift(LEFT*1.5)
        label_X = ax.get_x_axis_label(label="Tempo[s]").shift(LEFT)

        plotGrafico = VGroup(ax, label_X, label_Y)

        grupoGrafico = VGroup(plotagemGrafico, plotGrafico).scale(0.8)

        self.play(FadeIn(plotGrafico))
        self.wait(1)

        self.play(Write(plotagemGrafico).set_run_time(2))
        self.wait(2)

class descargaCapacitorParte02(Scene):
    def construct(self):
        templete = TexTemplate()
        templete.add_to_preamble(r"\usepackage[siunitx, straight voltages, american]{circuitikz}")

        c = MathTex(   
            r"""=\draw (0,0) to [battery2, l_=$V_0 {=}100V$, invert] (0,3) 
            to [short, -] (2,3)
            to [short, i=$I$] (3,3)
            to [R=$R{=}100k\Omega$, v<=$V_R$] (5,3)
            to [C=$C{=}10\mu F$, v<=$V_C$] (5,0) 
            to [short, -] (2,0) -- (0,0);"""
            , stroke_width=2
            , fill_opacity=0
            , stroke_opacity=1
            , tex_environment="circuitikz"
            , tex_template=templete
        ).shift(LEFT*2.5)

        ax = Axes(
            x_range=[0, 11, 1],
            y_range=[0, 120, 20],
            tips=True,
            x_length=5,
            y_length=5,
            x_axis_config={"numbers_to_include": np.arange(0, 11, 1)},
            y_axis_config={"numbers_to_include": np.arange(0, 120, 20)},
        ).shift(RIGHT*4.5)

        # Parâmetros do circuito
        C = 10e-6  # Capacitância (10 microfarads)
        V = 100.0  # Tensão da fonte
        R = 100e3  # Resistência (100 kiloohms)

        # Constante de tempo (tau)
        tau = R * C

         # Carga do capacitor
        q_carga = ax.plot(lambda x: V * (1 - np.exp(-x / tau)), color=YELLOW, x_range=[0,10])
        
        # Descarga do capacitor
        q_descarga = ax.plot(lambda x: V * (np.exp(-x / tau)), color=BLUE, x_range=[0,10])

        label_Y = ax.get_y_axis_label(label="Voltagem[V]").shift(LEFT*1.5)
        label_X = ax.get_x_axis_label(label="Tempo[s]").shift(DOWN*1.6+LEFT)

        plotGrafico = VGroup(ax, label_X, label_Y)
        
        textoGrafico = Text("Carga/Descarga").shift(UP*3+RIGHT*3.2).scale(0.8)
        textoCircuito = Text("Circuito Elétrico").shift(UP*3+LEFT*3.2).scale(0.8)

        parteCircuito = VGroup(c, textoCircuito)
        parteGrafico = VGroup(plotGrafico, textoGrafico)

        plotagemGrafico = VGroup(q_carga, q_descarga)

        c.scale_to_fit_width(width=6)
        grupoGrafico = VGroup(plotagemGrafico, plotGrafico).scale(0.8)

        self.add(parteCircuito)
        self.add(parteGrafico)

        self.play(Write(plotagemGrafico).set_run_time(10))