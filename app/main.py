from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from app.routes.chat_route import router as chat_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('    ')

@asynccontextmanager
async def inicio(app: FastAPI):
  logger.info('Iniciando Aplicação...')
  yield
  logger.info('Encerrando Aplicação...')
  

app = FastAPI( 
  title="Bayesian API",
  description="API para verificação de emprestimo com base em rede bayesiana",
  version="1.0.0",
  lifespan=inicio
)

origins = [
  "http://localhost:3000",
  "https://frontend-bay.onrender.com"
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=False,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(chat_router)

@app.get('/', include_in_schema=False)
async def docs():
  logger.info('redirencionando para o swagger')
  return RedirectResponse(url="/docs")

@app.get('/home', include_in_schema=False)
async def home():
  return {'pagina home': 'hello world'}