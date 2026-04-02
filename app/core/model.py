from mesa import Model
from mesa.space import ContinuousSpace
import numpy as np

from app.core.boid import Boid


class BoidsModel(Model):
    def __init__(
        self, n, width, height, max_speed=3.0, visual_range=60.0, avoid_range=20.0
    ):
        super().__init__()
        self.space = ContinuousSpace(width, height, torus=True)
        self.max_speed = max_speed
        self.visual_range = visual_range
        self.avoid_range = avoid_range

        # Force weights
        self.sep_weight = 1.5
        self.align_weight = 1.0
        self.coh_weight = 0.8
        self.steer_force = 0.05

        # Init agents
        for _ in range(n):
            boid = Boid(self)
            random_pos = np.random.rand(2) * [width, height]
            self.space.place_agent(boid, random_pos)
            self.agents.add(boid)

    def step(self):
        # Shuffle agent order, then call step on each agent
        self.agents.shuffle_do("step")
