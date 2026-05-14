from fastapi import FastAPI, Request
from scheduler import schedule_vehicles
from logger_config import logger
import time

app = FastAPI()

# Logging Middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):

    start_time = time.time()

    logger.info(f"Incoming request: {request.method} {request.url}")

    response = await call_next(request)

    process_time = time.time() - start_time

    logger.info(f"Completed in {process_time:.4f} seconds")

    return response


@app.post("/schedule")
async def schedule(data: dict):

    vehicles = data["vehicles"]
    total_hours = data["total_mechanic_hours"]

    result = schedule_vehicles(vehicles, total_hours)

    return result