from manim import *

from manim_slides import Slide, ThreeDSlide

from time import sleep
from copy import deepcopy
import numpy as np
import math

class Lecture(Slide): #
    def construct(self):
        titulo_1 = Text('Физика 1.2') ## Titulo
        abr = Text('Специальная теория относительности') ## Titilo v2
        self.play(Write(titulo_1))
        
        self.wait(1)
        # self.next_slide()

        self.play(Transform(titulo_1, abr))
        
        self.wait(1.1)
        self.play(Unwrite(titulo_1))
        # self.next_slide()

        banner = ManimBanner().scale(0.5)
        self.play(banner.create())
        self.play(banner.expand())
        self.play(Wiggle(banner))
        self.wait(1.1)
        self.play(Uncreate(banner))
        self.wait(3.1)
        self.next_slide()

        def dot_position(mobject):
            mobject.set_value(height.get_value())
            mobject.next_to(dot)
        background_1 = ImageMobject("Gemini_Generated_Image.jpg").scale(0.5)
        muon_non_rel_1 = Text('Мюон падает c высоты 10 км, нерелятивистский случай', font_size=26).to_edge(UL)
        self.play(Write(muon_non_rel_1))
        self.next_slide()
        height_start = 10
        height = ValueTracker(10) #10
        label = DecimalNumber(color=ManimColor("#000000"))
        label.add_updater(dot_position)
        self.add(background_1.shift(RIGHT*3))
        axes = Axes(x_range=[0, 1, 1], y_range=[0, 11, 1], x_length=6, y_length=6, tips=True,
                    axis_config={'include_numbers': True})
        dot = always_redraw(lambda: LabeledDot(MathTex(r"\mu", color = ManimColor("#0000FF"),font_size=34),color = RED, radius=0.25,stroke_width=1,point=[axes.c2p(0.70, height.get_value())]))
        self.add(dot, label)
        self.play(Create(axes.shift(RIGHT*3))) #Create(wall),
        self.add(height)

        half_life = MathTex(r"T_{1/2} = 1.56\ \mu s", font_size=30)

        all_time = MathTex(r"T = \frac{10000\ m}{0.98 \cdot 3.10^8 \ m/s} ", font_size=30)
        
        halftimes = MathTex(r"T = 34 \cdot10^{-6} \ s = 21.8\ halftimes ", font_size=30)

        N_start = 1000000
        N_left =  DecimalNumber(N_start, font_size = 36)
        C = 2.9979*pow(10,8)
        T_hl = 1.56*pow(10,-6)
        N_left.add_updater(lambda d: d.set_value( N_start*pow(2,(-(height_start - height.get_value())*1000/(0.98*C*T_hl)))))
        muon_text = Text('осталось мюонов', font_size=24).next_to(N_left,RIGHT)
        half_life_group = VGroup(half_life, all_time, halftimes, VGroup(N_left,muon_text)).arrange(DOWN*2, aligned_edge=LEFT).to_edge(LEFT)
        self.play(Write(half_life_group))
        self.next_slide()
        self.play(height.animate.set_value(0), rate_func=rate_functions.linear, run_time=10)
        self.wait(6)
        self.next_slide()
        
class Muon_rel(Slide):
    def construct(self):
        def dot_position(mobject):
            mobject.set_value(height.get_value())
            mobject.next_to(dot)
        background_2 = ImageMobject("Gemini_Generated_Image.jpg").scale(0.5)
        muon_non_rel_2 = Text('Мюон падает c высоты 10 км, релятивистский случай относительно Земли', font_size=26).to_edge(UL)
        self.play(Write(muon_non_rel_2))
        self.next_slide()
        height_start = 10
        height = ValueTracker(10) #10

        label = DecimalNumber(color=ManimColor("#000000"))
        label.add_updater(dot_position)
        self.add(background_2.shift(RIGHT*3))
        axes = Axes(x_range=[0, 1, 1], y_range=[0, 11, 1], x_length=6, y_length=6, tips=True,
                    axis_config={'include_numbers': True})
        dot = always_redraw(lambda: LabeledDot(MathTex(r"\mu", color = ManimColor("#0000FF"),font_size=34),color = RED, radius=0.25,stroke_width=1,point=[axes.c2p(0.70, height.get_value())]))
        self.add(dot, label)
        self.play(Create(axes.shift(RIGHT*3))) #Create(wall),
        self.add(height)

        half_life_1 = MathTex(r"T_{1/2} =\frac{T'_{1/2}}{\sqrt{1-\beta^2}}", font_size=30)
        half_life_2 = MathTex(r"T_{1/2} =T'_{1/2}\cdot(\sqrt{1-\frac{v^2}{c^2}})^{-1}", font_size=30)
        half_life_3 = MathTex(r"T_{1/2} =1.56\ \mu s\cdot(\sqrt{1-0.98^2})^{-1}", font_size=30)
        half_life_4 = MathTex(r"T_{1/2} =7.84\ \mu s", font_size=30)
        all_time = MathTex(r"T = \frac{10000\ m}{0.98 \cdot 3.10^8 \ m/s} ", font_size=30)
        
        halftimes_1 = MathTex(r"T = 34 \cdot10^{-6} \ s = 21.8\ halftimes ", font_size=30)
        halftimes_2 = MathTex(r"T = 34 \cdot10^{-6} \ s = 4.34\ halftimes ", font_size=30)
        N_start = 1000000
        N_left =  DecimalNumber(N_start, font_size = 36)
        C = 2.9979*pow(10,8)
        T_hl = 7.84*pow(10,-6)
        N_left.add_updater(lambda d: d.set_value( N_start*pow(2,(-(height_start - height.get_value())*1000/(0.98*C*T_hl)))))
        muon_text = Text('осталось мюонов', font_size=24).next_to(N_left,RIGHT)
        #self.add(N_left)
        half_life_group = VGroup(half_life_1, all_time, halftimes_1, VGroup(N_left,muon_text)).arrange(DOWN*2, aligned_edge=LEFT).to_edge(LEFT)
        self.play(Write(half_life_group))
        self.next_slide()
        half_life_2.move_to(half_life_1.get_left(), aligned_edge=LEFT)
        self.play(Transform(half_life_1,half_life_2))
        self.next_slide()
        half_life_3.move_to(half_life_1.get_left(), aligned_edge=LEFT)
        self.play(Transform(half_life_1,half_life_3))
        self.next_slide()
        half_life_4.move_to(half_life_1.get_left(), aligned_edge=LEFT)
        self.play(Transform(half_life_1,half_life_4))
        halftimes_2.move_to(halftimes_1.get_left(), aligned_edge=LEFT)
        self.play(Transform(halftimes_1,halftimes_2))
        self.next_slide()
        self.play(height.animate.set_value(0), rate_func=rate_functions.linear, run_time=10)
        self.wait(6)
        self.next_slide()

class Muon_rel_self(Slide):
    def construct(self):
        def dot_position(mobject):
            mobject.set_value(height.get_value())
            mobject.next_to(dot)
        background_3 = ImageMobject("Gemini_Generated_Image.jpg").scale(0.5)
        muon_non_rel_3 = Text('Мюон падает c высоты 10 км, релятивистский случай относительно мюона', font_size=26).to_edge(UL)
        self.play(Write(muon_non_rel_3))
        self.next_slide()
        height_start = 10
        height = ValueTracker(10) #10
        label = DecimalNumber(color=ManimColor("#000000"))
        label.add_updater(dot_position)
        self.add(background_3.shift(RIGHT*3))
        axes_1 = Axes(x_range=[0, 1, 1], y_range=[0, 11, 1], x_length=6, y_length=6, tips=True,
                    axis_config={'include_numbers': True})
        axes_2 = Axes(x_range=[0, 1, 1], y_range=[0, 2, 1], x_length=6, y_length=6, tips=True,
                    axis_config={'include_numbers': True})
        axes = axes_1
        dot = always_redraw(lambda: LabeledDot(MathTex(r"\mu", color = ManimColor("#0000FF"),font_size=34),color = RED, radius=0.25,stroke_width=1,point=[axes.c2p(0.70, height.get_value())]))
        self.add(dot, label)
        self.play(Create(axes.shift(RIGHT*3))) #Create(wall),
        self.add(height)

        distance_1 =  MathTex(r"L' =L_{0}\cdot{\sqrt{1-\beta^2}}", font_size=30)
        distance_2 =  MathTex(r"L' =L_{0}\cdot{\sqrt{1-\frac{v^2}{c^2}}}", font_size=30)
        distance_3 =  MathTex(r"L' =L_{0}\cdot{\sqrt{1-0.98^2}}", font_size=30)
        distance_4 =  MathTex(r"L' =1990 m", font_size=30)
        
        all_time_1 = MathTex(r"T = \frac{10000\ m}{0.98 \cdot 3.10^8 \ m/s} ", font_size=30)
        all_time_2 = MathTex(r"T = \frac{1990\ m}{0.98 \cdot 3.10^8 \ m/s} ", font_size=30)
        
        halftimes_1 = MathTex(r"T = 34 \cdot10^{-6} \ s = 21.8\ halftimes ", font_size=30)
        halftimes_2 = MathTex(r"T = 6.77 \cdot10^{-6} \ s = 4.34\ halftimes ", font_size=30)

        N_start = 1000000
        N_left =  DecimalNumber(N_start, font_size = 36)
        C = 2.9979*pow(10,8)
        T_hl = 1.56*pow(10,-6)
        N_left.add_updater(lambda d: d.set_value( N_start*pow(2,(-(height_start - height.get_value())*1000/(0.98*C*T_hl)))))
        muon_text = Text('осталось мюонов', font_size=24).next_to(N_left,RIGHT)
        half_life_group = VGroup(distance_1, all_time_1, halftimes_1, VGroup(N_left,muon_text)).arrange(DOWN*2, aligned_edge=LEFT).to_edge(LEFT)
        self.play(Write(half_life_group))
        self.next_slide()
        distance_2.move_to(distance_1.get_left(), aligned_edge=LEFT)
        self.play(Transform(distance_1,distance_2))
        self.next_slide()
        distance_3.move_to(distance_1.get_left(), aligned_edge=LEFT)
        self.play(Transform(distance_1,distance_3))
        self.next_slide()
        distance_4.move_to(distance_1.get_left(), aligned_edge=LEFT)
        self.play(Transform(distance_1,distance_4))
        self.next_slide()
        all_time_2.move_to(all_time_1.get_left(), aligned_edge=LEFT)
        self.play(Transform(all_time_1,all_time_2))
        self.next_slide()
        halftimes_2.move_to(halftimes_1.get_left(), aligned_edge=LEFT)
        self.play(Transform(halftimes_1,halftimes_2))
        self.wait()
        self.next_slide()
        self.play(ReplacementTransform(axes,axes_2.shift(RIGHT*3)))
        axes = axes_2
        height_start = 1.990
        height.set_value(1.990)
        matrix = [[1, 0], [0, 0.4]]
        self.play(ApplyMatrix(matrix, background_3), ApplyMatrix(matrix, axes))
        self.next_slide()
        self.play(height.animate.set_value(0), rate_func=rate_functions.linear, run_time=10)
        self.next_slide()

class FirstTask(Slide): #задача про мюон
    def construct(self):
        text_near_plot = Text('Лоренц-фактор от скорости:', font_size=26).to_edge(UL)
        formula_near_plot = MathTex(r"T=\frac{T_{0}}{\sqrt{1-\beta^2}}=T_{0}\cdot(\sqrt{1-\frac{v^2}{c^2}})^{-1}", font_size=30).next_to(text_near_plot, RIGHT)
        self.play(Write(text_near_plot))
        self.play(Write(formula_near_plot))
        self.next_slide()
        axes = Axes(x_range=[0, 1.2, 0.2], y_range=[0, 9.0, 1.0], x_length=5, y_length=5, tips=True,
                    axis_config={'include_numbers': True}).to_edge(DR)
        labels = axes.get_axis_labels( MathTex(r'\frac{v}{C}', font_size=34), MathTex(r'\gamma', font_size=34))
        T_0 = 1.0
        C = 2.9979 #299792458 m/s
        velocity = ValueTracker(0)
        velocity.set_value(0)
        tofv = lambda v: T_0 * 1/np.sqrt(1-pow(v,2))#pow(v,2)/pow(C,2)
        plot = always_redraw(lambda: axes.plot(function=tofv, x_range=[0, velocity.get_value()/C], color=BLUE))
        dot = always_redraw(lambda: Dot(color=BLUE, point=[axes.c2p(velocity.get_value()/C, tofv(velocity.get_value()/C))]))
        
        velocity_label = DecimalNumber(0, font_size = 34)
        velocity_label.add_updater(lambda d: d.set_value(round(velocity.get_value()*pow(10,8))))
        velocity_group = VGroup(Text('v (м/с)  = ', font_size=20),velocity_label).arrange(RIGHT*2, aligned_edge=LEFT).to_edge(LEFT)
        self.play(Write(velocity_group),Create(axes), Create(dot), Write(labels))
        self.next_slide()
        self.add(plot)
        self.play(velocity.animate.set_value(0.99*C), rate_func=rate_functions.ease_out_sine, run_time=5)
        self.wait()
        self.next_slide()

class SecondTask(Slide): #Slide
    def construct(self):
        second_task_text_1 = Text("Две частицы движутся навстречу друг другу со скоростями 0,5 с и 0,75 с", font_size=26)
        second_task_text_2 = Text("по отношению к лабораторной системе отсчета. Найти их относительную скорость", font_size=26)
        second_task_plane = NumberPlane(
            x_range=[0, 6, 1], y_range=[0, 4, 1], x_length=6, y_length=4
        )
        second_task_labels = second_task_plane.get_axis_labels( MathTex('x', font_size=24), MathTex('y', font_size=24))
        second_task_vect1 = Line(
            start=second_task_plane.coords_to_point(1, 2),
            end=second_task_plane.coords_to_point(3, 2),
            stroke_color=YELLOW,
        ).add_tip()
        second_task_vect1_name = (
            MathTex("v_{1} = 0.5 \ c", font_size=28).set_color(YELLOW) #.next_to(vect1.get_end())
        ).add_updater(lambda x: x.next_to(second_task_vect1.get_end(),UP+LEFT)) #vect1_name
        second_task_vect2 = Line(
            start=second_task_plane.coords_to_point(6, 2),
            end=second_task_plane.coords_to_point(4, 2),
            stroke_color=RED,
        ).add_tip()
        second_task_vect2_name = (
            MathTex("v_{2} = 0.75 \ c", font_size=28).set_color(RED)
        ).add_updater(lambda x: x.next_to(second_task_vect2.get_end(),UP+RIGHT))
        second_task_form = Text("Релятивистский закон сложения скоростей ", font_size=26).to_edge(DL)
        second_task_vel = MathTex(r"u' = \frac{u-v}{1-uv/c^2}", font_size=34).next_to(second_task_form, RIGHT)
        second_task_group = VGroup(second_task_text_1,second_task_text_2).arrange(DOWN*2, aligned_edge=LEFT).to_corner(UP)
        self.play(Write(second_task_group))
        self.next_slide()
        self.play(DrawBorderThenFill(second_task_plane), run_time=2)
        self.play(Write(second_task_labels))
        self.play(
            GrowFromPoint(second_task_vect1, point=second_task_vect1.get_start()), Write(second_task_vect1_name), run_time=2
        )
        self.play(
            GrowFromPoint(second_task_vect2, point=second_task_vect2.get_start()), Write(second_task_vect2_name), run_time=2
        )
        self.next_slide()
        self.play(Write(second_task_form))
        self.play(Write(second_task_vel))
        self.next_slide()
        
class Review(ThreeDSlide):
    def construct(self):
        
        title = Text("Итоги").scale(2)

        self.set_camera_orientation(
            phi = 60*DEGREES,
            theta = 80*DEGREES,
            distance = 10
        )


        self.add_fixed_in_frame_mobjects(title)
        self.remove(title)

        self.play(Write(title))

        z1 = Surface(
           lambda u, v: np.array([u, v, v * 0.3*np.sin(u) - u *0.3*np.cos(v)]),
           resolution = (16, 32),
           v_range = [-2, 2],
           u_range = [-2, 2],
           fill_opacity = 0.1
        ).set_opacity(0.2)

        z1.set_color_by_gradient(TEAL, MAROON, YELLOW)

        z2 = Surface(
           lambda u, v: np.array([u, v, u * 4*math.e**(-u**2 - v**2)]),
           resolution = (16, 32),
           v_range = [-2, 2],
           u_range = [-2, 2],
           fill_opacity = 0.1
        ).set_opacity(0.2)

        z2.set_color_by_gradient(MAROON, YELLOW, TEAL)

        z3 = Surface(
           lambda u, v: np.array([u, v, v * -0.3*np.sin(u) - u * -0.3*np.cos(v)]),
           resolution = (16, 32),
           v_range = [-2, 2],
           u_range = [-2, 2],
           fill_opacity = 0.1
        ).set_opacity(0.2)

        z3.set_color_by_gradient(YELLOW, MAROON, TEAL)

        z4 = Surface(
           lambda u, v: np.array([u, v, u * -4*math.e**(-u**2 - v**2)]),
           resolution = (16, 32),
           v_range = [-2, 2],
           u_range = [-2, 2],
           fill_opacity = 0.1
        ).set_opacity(0.2)

        z4.set_color_by_gradient(TEAL, YELLOW, MAROON)

        sheet = Surface(
           lambda u, v: np.array([u, v, 0]),
           resolution = (1, 1),
           v_range = [-4, 4],
           u_range = [-2, 2],
           fill_opacity = 0.1
        ).set_opacity(0.2).set_color([TEAL, MAROON, YELLOW])

        z11 = z1.copy()
        z12 = z1.copy()

        z21 = z2.copy()
        z22 = z2.copy()

        z31 = z3.copy()

        z41 = z4.copy()

        self.play(Write(z1), Write(z2), run_time = 1.5)
        self.play(ReplacementTransform(z1, z3), ReplacementTransform(z2, z4), run_time = 2)
        self.play(ReplacementTransform(z3, z11), ReplacementTransform(z4, z21), run_time = 2)

        self.play(Unwrite(VGroup(title, z11, z21)), run_time = 2)
        self.wait()
        self.next_slide()

class Ending(Slide):
    def construct(self):
        titulo_2 = Text('Почему так происходит?', font_size = 26) ## Titulo
        explain = Text("Пространство-время Минковского:", font_size = 26).to_corner(UL)
        formula = MathTex(r"(ct)^{2}-x^{2}-y^{2}-z^{2}=0", font_size=32).to_corner(UR)

        self.play(Write(titulo_2))
        self.wait()
        self.next_slide()
        self.play(titulo_2.animate.to_corner(UP + LEFT))

        self.play(Transform(titulo_2,VGroup(explain,formula)))
        plane = NumberPlane(
            x_range=[-5, 5, 1], y_range=[0, 6, 1], x_length=10, y_length=6
        )
        labels = plane.get_axis_labels( Text("Расстояние", font_size=24), Text("Время", font_size=24))

        plane.to_corner(DOWN)

        backgound = NumberPlane(
            x_range=[-5, 5, 1], y_range=[0, 6, 1], x_length=10, y_length=6,
            background_line_style={
                "stroke_color": GRAY,
                "stroke_opacity": 0.6
            }
        ).to_corner(DOWN)
        self.add(backgound)

        vect1 = Line(
            start=plane.coords_to_point(0, 0),
            end=plane.coords_to_point(0, 2),
            stroke_color=YELLOW,
        ).add_tip()
        vect1_name = (
            MathTex("v_{1}", font_size=25).set_color(YELLOW) #.next_to(vect1.get_end())
        ).add_updater(lambda x: x.next_to(vect1.get_end())) #vect1_name

        speed = ValueTracker(1)
        vect2 = always_redraw(lambda: Line(
            start=plane.coords_to_point(0, 0),
            end=plane.coords_to_point(speed.get_value(), np.sqrt(1+speed.get_value()**2)+1), #2
            stroke_color=RED,
        ).add_tip())
        vect2_name = (
            MathTex("v_{2}", font_size=25).set_color(RED)
        ).add_updater(lambda x: x.next_to(vect2.get_end()))

        self.play(DrawBorderThenFill(plane), run_time=2)
        self.play(Write(labels))
        self.wait()
        self.play(
            GrowFromPoint(vect1, point=vect1.get_start()), Write(vect1_name), run_time=2
        )
        self.wait()
        self.play(
            GrowFromPoint(vect2, point=vect2.get_start()), Write(vect2_name), run_time=2
        )
        
        cone = plane.plot_implicit_curve(lambda x, y: (y-1)** 2 - x ** 2 - 1,color=WHITE)
        light_function = lambda x: np.abs(x)
        light = plane.plot(light_function, color=BLUE)
        
        self.add(plane)
        self.play(Create(cone), Create(light))
        self.next_slide()
        matrix = [[1, -np.sqrt(2)+1], [0, 2/(np.sqrt(1+(np.sqrt(2)+1)**2))]]
        self.play(ApplyMatrix(matrix, plane, vect1.get_start()), ApplyMatrix(matrix, vect1, vect1.get_start()), ApplyMatrix(matrix, vect2, vect1.get_start()))
        self.wait(1.1)
        matrix_2 = [[1, 0.54], [0, (np.sqrt(1+(np.sqrt(2)+1)**2))/2]]
        self.play(ApplyMatrix(matrix_2, plane, vect1.get_start()), ApplyMatrix(matrix_2, vect1, vect1.get_start()), ApplyMatrix(matrix_2, vect2, vect1.get_start()))
        self.next_slide()
        self.play(speed.animate.set_value(5), rate_func=rate_functions.ease_out_sine, run_time=5)