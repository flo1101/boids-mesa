from core.model import BoidsModel
from core.boid import Boid
from schema.simulation_schema import SimulationState
from app.config.settings import Settings


class SimulationService:
    def __init__(
        self,
        n: int = Settings.N_BOIDS,
        width: float = Settings.WIDTH,
        height: float = Settings.HEIGHT,
        max_speed: float = Settings.MAX_SPEED,
        visual_range: float = Settings.VISUAL_RANGE,
        avoid_range: float = Settings.AVOID_RANGE,
    ):
        self.params = dict(
            n=n,
            width=width,
            height=height,
            max_speed=max_speed,
            visual_range=visual_range,
            avoid_range=avoid_range,
        )
        self.model = BoidsModel(**self.params)

    def step(self) -> SimulationState:
        self.model.step()
        return {
            "boids": [
                {
                    "x": boid.pos[0],
                    "y": boid.pos[1],
                    "vx": boid.velocity[0],
                    "vy": boid.velocity[1],
                }
                for boid in self.model.agents
            ],
            "step": self.model.schedule.steps,
            "n_boids": len(self.model.agents),
        }

    def reset(self, **overrides) -> None:
        params = {**self.params, **overrides}
        self.model = BoidsModel(**params)
