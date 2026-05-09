from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, SecretStr

class Settings(BaseSettings):
    openai_api_key: SecretStr = Field(validation_alias="OPENAI_API_KEY")
    tavily_api_key: SecretStr = Field(validation_alias="TAVILY_API_KEY")
    model: str = Field(default="gpt-3.5-turbo", validation_alias="MODEL")
    model_temperature: float = Field(default=0.1, validation_alias="MODEL_TEMPERATURE")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings() # type: ignore
