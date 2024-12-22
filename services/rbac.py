from fastapi import HTTPException, Depends
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
import os

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
SECRET_KEY = os.getenv("SECRET_KEY", "secret-key")
ALGORITHM = "HS256"

# Get current user from token
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        role = payload.get("role")
        if username is None or role is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"username": username, "role": role}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Check user role
def has_role(required_role: str):
    def role_checker(current_user=Depends(get_current_user)):
        if current_user["role"] != required_role:
            raise HTTPException(status_code=403, detail="Access forbidden")
        return current_user
    return role_checker
