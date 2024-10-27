from fastapi import APIRouter
from app.services.bayesian_algorithm import Algorithm

calculate = Algorithm()
router = APIRouter()

@router.post('/api/send-message/{mensagem}')
async def sendMessage(mensagem: str):
  calculate.Calculate()
  return 
  
@router.get('/api/get-message')
async def getMessage():
  return 'get-message'
