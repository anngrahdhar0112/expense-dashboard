import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()  # reads .env

def get_engine():
    url = (
        f"postgresql+psycopg2://{os.getenv('PGUSER','admin')}:"
        f"{os.getenv('PGPASSWORD','admin')}@{os.getenv('PGHOST','localhost')}:"
        f"{os.getenv('PGPORT','55432')}/{os.getenv('PGDATABASE','analytics_lab')}"
    )
    return create_engine(url, pool_pre_ping=True)
