from contextlib import asynccontextmanager

from dotenv import load_dotenv
load_dotenv( )

from api.app_container import AppContainer
from api.user.user_controller import router as user_router
from api.post.post_controller import router as post_router

from fastapi import (APIRouter, FastAPI, )

router = APIRouter(prefix='/api')

@router.get( "/health" )
async def root():
	return {}

@asynccontextmanager
async def lifespan(app: FastAPI):
	container = AppContainer()
	app.container = container
	app.container.init_resources()
	yield
	app.container.shutdown_resources()

def create_app() -> FastAPI:
	app = FastAPI(lifespan=lifespan)
	app.include_router( router )
	app.include_router( user_router )
	app.include_router( post_router )
	return app

app = create_app()
