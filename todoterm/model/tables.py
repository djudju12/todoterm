from typing import Optional
from sqlalchemy import String, DateTime, func, Boolean
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import create_engine
from tomlkit import parse
import os 

HOME = os.environ.get("HOME")

with open(HOME + "/.config/todoterm/todoconfig.toml", "r") as configs:
    parsed_configs = parse(configs.read())
    db_url = HOME + parsed_configs["database"]["url"]

engine = create_engine("sqlite:///" + db_url, echo=True)

class Base(DeclarativeBase):
    pass


class Todo(Base):
    __tablename__ = "tb_todo"

    id: Mapped[int] = mapped_column(primary_key=True)
    task: Mapped[str] = mapped_column(String(100))
    creation_date: Mapped[DateTime] = mapped_column(DateTime(timezone=True), 
                                                server_default=func.now())
    is_finished: Mapped[bool] = mapped_column(Boolean, default=False)

Base.metadata.create_all(engine)
