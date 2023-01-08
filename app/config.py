from pydantic import BaseSettings


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_name: str
    database_username: str = "postgres"
    database_password: str = "localhost"
    secret_key: str = "13r8yfgcu2g7f[32fgoi2"
    algorithm: str
    access_token_expire_minutes = int

    class Config:
        env_file: ".env"


settings = Settings()
