from backend.api.api import router as api_router

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

import uvicorn




origins = [
    "*",
]


app = FastAPI(
    Title="TestingService-server",
)

app.add_middleware(
    CORSMiddleware,  # noqa
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.middleware("http")(exception_traceback_middleware)

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("main:app",
                host='0.0.0.0',
                port=8000,
                reload=True,
                workers=3,
                )
