from todoterm.model.tables import Todo 

from sqlalchemy import create_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from tomlkit import parse
import os

HOME = os.environ.get("HOME")

with open(HOME + "/.config/todoterm/todoconfig.toml", "r") as configs:
    parsed_configs = parse(configs.read())
    db_url = HOME + parsed_configs["database"]["url"]

engine = create_engine("sqlite:///" + db_url, echo=True)

with Session(engine) as session:
    new_todo = Todo(id=1, task="teste")
    session.add(new_todo)
    session.commit()
