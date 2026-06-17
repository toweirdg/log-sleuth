import time

from fastapi import Request

async def timing_middleware(request: Request, call_next):
    start = time.time()

    response = await call_next(request)

    process_time = time.time() - start

    response.headers["X-Process-Time"] = str(process_time)

    return response
