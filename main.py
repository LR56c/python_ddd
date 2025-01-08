from contextlib import asynccontextmanager

from dotenv import load_dotenv

from api.app_container import AppContainer
from api.user.controller import router as user_router
from features.user.dependencies_container import UserContainer

load_dotenv()

from fastapi import (APIRouter, FastAPI, )

import os

router = APIRouter(prefix='/api')

@router.get( "/health" )
async def root():
	return {}

@asynccontextmanager
async def lifespan(app: FastAPI):
	container = UserContainer()
	app.container = AppContainer()
	yield
	# global client
	# print('preinit')
	# username = os.environ.get( 'MONGO_INITDB_ROOT_USERNAME' )
	# password = os.environ.get( 'MONGO_INITDB_ROOT_PASSWORD' )
	# host = 'localhost'
	# client = MongoClient(f'mongodb://root:root@mongo:27017/notification?authSource=admin')
	# print('init',client.server_info())
	# db = client.get_database( 'notification' )
	# collection = db.get_collection( 'notification' )
	# collection.insert_one( { 'name': 'test' } )
	# print( 'all: ',collection.find() )
	# yield
	# if client:
	# 	client.close()

app = FastAPI(lifespan=lifespan)
app.include_router( router )
app.include_router( user_router )
