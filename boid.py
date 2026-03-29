from mesa import Agent
import numpy as np


class Boid(Agent):
    def __init__(self, model):
        super().__init__(model)
        angle = self.random.uniform(0, 2 * np.pi)
        self.velocity = np.array([np.cos(angle), np.sin(angle)]) * model.max_speed

    def step(self):
        # Get Neighbors (Perceive)
        # TODO: Replace n² neighbor search with KD-tree or spatial indexing
        neighbors = self.model.space.get_neighbors(
            self.pos, self.model.visual_range, include_center=False
        )

        if not neighbors:
            return

        # Compute forces (Decide)
        separation = np.zeros(2)
        alignment = np.zeros(2)
        cohesion = np.zeros(2)

        for neighbor in neighbors:
            delta = self.pos - neighbor.pos
            distance = np.linalg.norm(delta)

            # Separation: Steer a waway from boids that are too close
            if distance < self.model.avoid_range and distance > 0:
                separation += delta / distance**2  # Stronger repulsion when closer

            # Alignment: Steer towards the average velocity of neighbors
            alignment += neighbor.velocity

            # Cohesion: Steer towards center of mass of neighbors
            cohesion += neighbor.pos

        n = len(neighbors)
        alignment /= n
        cohesion = cohesion / n - self.pos  # Vector towards center of mass

        # Normalize vectors
        def _normalize(v):
            mag = np.linalg.norm(v)
            return v / mag if mag > 0 else v

        separation = _normalize(separation)
        alignment = _normalize(alignment)
        cohesion = _normalize(cohesion)

        # Apply weights
        self.velocity += (
            separation * self.model.sep_weight
            + alignment * self.model.align_weight
            + cohesion * self.model.coh_weight
        ) * self.model.steer_force

        # (Act)
        speed = np.linalg.norm(self.velocity)
        if speed > self.model.max_speed:
            self.velocity = self.velocity / speed * self.model.max_speed

        self.model.space.move_agent(self, self.pos + self.velocity)
