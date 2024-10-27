from sqlmodel import Session
from models.user_model import User

class RepositorioUser:

  def __init__(self, db: Session):
    self.db = db
    
  async def criar(self, user: User):
    self.db.add(user)
  
  