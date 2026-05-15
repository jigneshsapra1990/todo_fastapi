from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    database_url: str 
    app_name: str = "FASTAPI TODO APP"
    app_env: str = "development"
    app_debug: bool = True


    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache()
def getAppConfig():
    return AppConfig()