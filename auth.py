from jose import jwt
from datetime import datetime, timedelta, timezone
import os 
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY") 
ALGORITHM = os.getenv("ALGORITHM")

def generate_token(user_id: int):
    tempo_expira = datetime.now(timezone.utc) + timedelta(minutes=60)
    dados = {"user_id": user_id, "exp": tempo_expira}
    return jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)