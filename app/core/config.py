from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", 
        case_sensitive=True,
        env_file_encoding="utf-8")   
    
    ENVIRONMENT: str = "development"
    APP_NAME: str = "PayFlow API"
    APP_VERSION: str = "1.0.0" 
    DEBUG: bool = False
    SECRET_KEY: str
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    JWT_REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    DATABASE_URL: str

settings = Settings()