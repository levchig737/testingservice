from api.api import router as api_router

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

import uvicorn

from db.base import get_async_session, get_session_stub

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

# --- Dependency Injection (DI) через `app.dependency_overrides` --- #

app.dependency_overrides[get_session_stub] = get_async_session

app.include_router(api_router)

