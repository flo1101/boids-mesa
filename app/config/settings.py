from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Simulation
    N_BOIDS: int = 100
    MAX_SPEED: float = 3.0
    VISUAL_RANGE: float = 60.0
    AVOID_RANGE: float = 20.0
    STEER_FORCE: float = 0.05

    # Weights
    SEP_WEIGHT: float = 1.5
    ALIGN_WEIGHT: float = 1.0
    COH_WEIGHT: float = 0.8

    # Space
    WIDTH: float = 900
    HEIGHT: float = 600
