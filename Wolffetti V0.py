from manim import *
import random

def confetti(self):
        confetti = VGroup()
        for _ in range(100): 
            piece = Dot(radius=0.1, color=random.choice([RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE]))
            piece.move_to([random.uniform(-6, 6), random.uniform(6, 12), 0])
            confetti.add(piece)
        
        self.add(confetti)
        self.play(confetti.animate.shift(DOWN * 19), run_time=7)