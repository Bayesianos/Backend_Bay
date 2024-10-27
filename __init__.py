from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging
# from fastapi.middleware.cors import CORSMiddleware

from app.infra.database import create_db_and_tables as criarDB
from app.routes.user_route import router as user_router
from app.routes.chat_route import router as chat_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('    ')

@asynccontextmanager
async def lifespan(app: FastAPI):
  logger.info('Iniciando Aplicação...')
  logger.info('Criando DB...')
  criarDB()
  yield  # Mantém a aplicação em execução
  logger.info('Finalizando DB...')

app = FastAPI( 
  title="Bayesian API",
  description="API para verificação de emprestimo com base em rede bayesiana",
  version="1.0.0",
  lifespan=lifespan
)

# origins = [
#   "http://localhost.tiangolo.com", #alterar para a url do site depois
#   "http://localhost",
#   "http://localhost:8080",
# ]

# app.add_middleware(
#   CORSMiddleware,
#   allow_origins=origins,
#   allow_credentials=True,
#   allow_methods=["*"],
#   allow_headers=["*"],
# )

app.include_router(user_router)
app.include_router(chat_router)

@app.get("/", include_in_schema=False)
async def home():
  logger.info('redirencionando para o swagger')
  return RedirectResponse(url="/docs")