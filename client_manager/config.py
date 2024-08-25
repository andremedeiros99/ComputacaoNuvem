import os

class Config:
    # Basic configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'minha_chave_secreta'

    # Database configuration
    DB_USERNAME = 'postgres'
    DB_PASSWORD = 'mydbpassword112233'
    DB_HOST = 'database-1.cxwo80o00d0k.us-east-2.rds.amazonaws.com'
    DB_NAME = 'postgres'
    DB_PORT = 5432 
    
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
