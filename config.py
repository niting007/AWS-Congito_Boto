from pydantic_settings import BaseSettings

class Settings( BaseSettings):
    app_name: str = "AWS-Congnito-Boto"
    
settings = Settings()