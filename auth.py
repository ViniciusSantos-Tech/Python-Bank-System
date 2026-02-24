import jwt
from datetime import datetime, timezone, timedelta
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    raise ValueError("SECRET_KEY was not configured in the .env file!")

def create_token(user_id, user):
    user_data = {
        "sub": str(user_id),
        "exp": datetime.now(timezone.utc) + timedelta(minutes=30),
        "name": user
    }
    
    token = jwt.encode(user_data, SECRET_KEY, algorithm="HS256")
    return token
def verify(token):
    try:
        decoded_data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True
    except jwt.ExpiredSignatureError:
        return "Expired token"
    except jwt.InvalidTokenError as e:
        return f"Invalid token: {e}"
