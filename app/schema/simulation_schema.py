from pydantic import BaseModel


class BoidState(BaseModel):
    x: float
    y: float
    vx: float
    vy: float


class SimulationState(BaseModel):
    boids: list[BoidState]
    step: int
    n_boids: int


class SimulationParams(BaseModel):
    n: int | None = None
    width: int | None = None
    height: int | None = None
    max_speed: float | None = None
    visual_range: float | None = None
    avoid_range: float | None = None
