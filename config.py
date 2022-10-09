import os
from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))
instance = basedir + '/instance'

class Config:
    """
    Base configuration class. Contains default configuration settings for all
    environments
    """
    
    # root of application; instance path
    

    # Default settings
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False
    WTF_CSRF_ENABLED = True

    # Settings for all environments
    SECRET_KEY = os.getenv('SECRET_KEY', default='dev')

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE = os.path.join(instance, 'development.db')

class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    DATABASE = os.path.join(instance, 'testing.db')

class ProductionConfig(Config):
    FLASK_ENV = 'production'
    DATABASE = os.path.join(instance, 'production.db')
