from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
# from fastapi.middleware.cors import CORSMiddleware

from app.routes.chat_route import router as chat_router
from app.services.bayesian_algorithm import Algorithm

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
   #alterar para a url do site depois
  "http://localhost",
  "http://localhost:8080",
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(chat_router)

@app.get("/", include_in_schema=False)
async def docs():
  logger.info('redirencionando para o swagger')
  return RedirectResponse(url="/docs")