from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import logging

from app.routes.chat_route import router as chat_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('    ')
  
app = FastAPI( 
  title="Bayesian API",
  description="API para verificação de emprestimo com base em rede bayesiana",
  version="1.0.0",
)

origins = [
  "https://frontend-bay-uytb.onrender.com"
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

@app.on_event("startup")
async def iniciandoAPP():
  logger.info("Iniciando Aplicação...")

@app.on_event("shutdown")
async def encerrandoAPP():
  logger.info("Encerrando Aplicação...")

