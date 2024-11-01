from fastapi import APIRouter, HTTPException

from app.services.bayesian_algorithm import Algorithm
from app.models.user_model import User_Receive, User_Send

calculate = Algorithm()
router = APIRouter()


responses = {
  200: {
    "description": "Dados recebidos com sucesso.",
    "model": User_Send
  },
  400: { "description": "Requisição inválida." },
  404: { "description": "Item não encontrado." },
  500: { "description": "Erro interno do servidor." },
}

@router.post('/api/receive-data', name='receber dados do usuário', responses=responses)
async def receiveData(data: User_Receive): # não é parametro de url 
  data_dict = data.model_dump() # converte o dado em um dicionario contendo chave e valor
  
  for key, value in data_dict.items():
    if (value is None or value == ' '):
      raise HTTPException(status_code=400, detail=f"{key.capitalize()} é obrigatório e não pode ser vazio.")
  
  resultado_emprestimo = calculate.Calculate(data_dict) # retornar se o emprestimo é valido ou não 
  
  return User_Send(emprestimo_valido=resultado_emprestimo)