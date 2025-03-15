import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    OIDC_CLIENT_SECRETS = 'client_secrets.json'
    OIDC_COOKIE_SECURE = False  # Change to True in production
    OIDC_CALLBACK_ROUTE = '/oidc/callback'
    OIDC_SCOPES = ['openid', 'email', 'profile']