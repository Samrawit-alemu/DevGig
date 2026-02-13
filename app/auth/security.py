from passlib.context import CryptContext

# 1. Setup the context (We use Bcrypt, the industry standard)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") 

# 2. Function to Hash a password (Registering)
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# 3. Function to Verify a password (Logging in)
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)