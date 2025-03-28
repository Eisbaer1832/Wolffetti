from manim import *
import random

class Confetti(Scene):
    def create_confetti_piece(self):
        """Create a random confetti piece (dot or star) at a single point at the bottom."""
        shape_type = random.choice(["dot", "star"])
        color = random.choice([RED, GREEN, BLUE, YELLOW, ORANGE, PINK, PURPLE])

        if shape_type == "dot":
            shape = Dot(radius=0.05, color=color)
        else:
            shape = Star(n=5, outer_radius=0.1, inner_radius=0.04, color=color)

        # Start position: Single point at the bottom center
        shape.move_to([0, -5, 0])  
        return shape

    def shoot_confetti(self, shape):
        """Animation to shoot confetti upwards to a random position."""
        target_x = random.uniform(-8, 8)
        target_y = random.uniform(2, 7)

        return shape.animate.move_to([target_x, target_y, 0])

    def drop_confetti(self, shape):
        """Animation to make confetti fall and rotate."""
        target_position = shape.get_center() + DOWN * random.uniform(14, 25)
        rotation_angle = random.uniform(-3*PI, 3*PI)

        return shape.animate.move_to(target_position).rotate(rotation_angle)

    def construct(self):
        confetti_pieces = [self.create_confetti_piece() for _ in range(200)]  # Reduced number for better performance
        for piece in confetti_pieces:
            self.add(piece)

        # Step 1: Shoot confetti upwards from a single point
        self.play(*[self.shoot_confetti(piece) for piece in confetti_pieces], run_time=1.5)

        # Step 2: Let confetti fall
        self.play(*[self.drop_confetti(piece) for piece in confetti_pieces], run_time=3)
