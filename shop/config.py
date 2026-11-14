import os,secrets
from pathlib import Path
DEBUG=False
SECRET_KEY=os.environ.get('SHOP_SECRET_KEY') or secrets.token_hex(32)
SQLALCHEMY_DATABASE_URI=os.environ.get('SHOP_DATABASE_URL','sqlite:///shop.db')
SQLALCHEMY_TRACK_MODIFICATIONS=False
DEBUG_TB_ENABLED=False
DEBUG_TB_INTERCEPT_REDIRECTS=False
UPLOADS_DEFAULT_DEST=str(Path(__file__).resolve().parent/'instance'/'uploads')
UPLOADS_DEFAULT_URL='/uploads/'
MAX_CONTENT_LENGTH=4*1024*1024
SESSION_COOKIE_HTTPONLY=True
SESSION_COOKIE_SAMESITE='Lax'
