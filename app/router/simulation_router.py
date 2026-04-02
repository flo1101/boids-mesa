from fastapi import router
from app.schema.simulation_schema import SimulationParams, SimulationState
from app.service.simulation_service import SimulationService

router = router.APIRouter(prefix="/simulation", tags=["simulation"])
service = SimulationService()


@router.get("/step", response_model=SimulationState)
def step():
    return service.step()


@router.post("/reset")
def reset(params: SimulationParams | None = None):
    if params:
        service.reset(**params.model_dump(exclude_none=True))
    else:
        service.reset()
