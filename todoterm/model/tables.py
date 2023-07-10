from sqlalchemy import String, DateTime, func, Boolean
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy import create_engine
from tomlkit import parse
import os


#    todo new -d "todo" -t "urgente" -d 20/10/2023  
#
#    todo ls # folders
#
#    todo ls -fd myTodos 
#
#    todo set -wd myTodos
#
#    todo ls # -fd myTodos 
#
#    todo ls -a # folders
#    todo unset -wd 
#

HOME = os.environ.get("HOME")

with open(HOME + "/.config/todoterm/todoconfig.toml", "r") as configs:
    parsed_configs = parse(configs.read())
    db_url = HOME + parsed_configs["database"]["url"]

engine = create_engine("sqlite:///" + db_url, echo=True)


class Base(DeclarativeBase):
    pass


class Folder(Base):
    __tablename__ = "tb_folder"

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String(50))


class TodoType(Base):
    __tablename__ = "tb_type"

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String(50))


class Todo(Base):
    __tablename__ = "tb_todo"

    id: Mapped[int] = mapped_column(primary_key=True)
    task: Mapped[str] = mapped_column(String(100))
    creation_date: Mapped[DateTime] = mapped_column(DateTime(timezone=True),
                                                    server_default=func.now())
    is_finished: Mapped[bool] = mapped_column(Boolean, default=False)
    # finish_date: Mapped[DateTime] = mapped_column(DateTime(timezone=True))
    folder: Mapped["Folder"] = mapped_column(ForeignKey("tb_folder.id"))
    todo_type: Mapped["TodoType"] = mapped_column(ForeignKey("tb_type.id"))


Base.metadata.create_all(engine)
