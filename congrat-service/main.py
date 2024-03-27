from fastapi import FastAPI
from dto.dto_models import *
from serivces.base_congrat_generation_service import base_congrat_generation_service

app = FastAPI()


@app.post("/congrat_generation/base")
async def base_congrat_generation(request_dto: BaseCongratRequestDTO) -> BaseCongratResponseDTO:
    return base_congrat_generation_service(request_dto)
