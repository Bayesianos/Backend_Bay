from fastapi import APIRouter
from app.models.user_model import User

router = APIRouter()

@router.post('/api/register-user/{dadosUser}')
async def register_user(dadosUser):#analisar e ver se há necessidade de ser um UserModel
  user = User(**dadosUser)
  
  return 'register-user'
