from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.api import router as api_router

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

