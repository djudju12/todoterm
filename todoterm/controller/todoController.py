from todoterm.model.tables import Todo, Folder, TodoType 
from sqlalchemy import select
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from tomlkit import parse
import os

HOME = os.environ.get("HOME")

with open(HOME + "/.config/todoterm/todoconfig.toml", "r") as configs:
    parsed_configs = parse(configs.read())
    db_url = HOME + parsed_configs["database"]["url"]

engine = create_engine("sqlite:///" + db_url, echo=True)


def create_todo(task, folder, todo_type):
    with Session(engine) as session:
        folder = find_folder(folder)
        todo_type = find_todo_type(todo_type)
        print(folder)
        print(todo_type)
        new_todo = Todo(task=task, folder=folder.id, todo_type=todo_type.id)
        session.add(new_todo)
        session.commit()


def create_folder(description):
    with Session(engine) as session:
        new_folder = Folder(description=description)
        session.add(new_folder)
        session.commit()


def create_todo_type(description):
    with Session(engine) as session:
        new_type = TodoType(description=description)
        session.add(new_type)
        session.commit()


def find_todo(id):
    with Session(engine) as session:
        stmt = select(Todo).where(Todo.id == id)
        todo = session.execute(stmt)
        return todo.fetchone()[0]


def find_folder(description):
    with Session(engine) as session:
        stmt = select(Folder).where(Folder.description == description)
        folder = session.execute(stmt)
        return folder.fetchone()[0]


def find_todo_type(description):
    with Session(engine) as session:
        stmt = select(TodoType).where(TodoType.description == description)
        todo_type = session.execute(stmt)
        return todo_type.fetchone()[0]


#def find_all_folder(id):
#
#
#
#def find_all_todo_from(folder_description):
#    with Session(engine) as session:
#        stmt = select(Todo).where(Todo.folder == folder_description)
#        todo_list = session.execute(stmt)
#
#    return todo_list


if __name__ == "__main__":
    new_todo = create_todo(task="teste todo", folder="teste folder", 
                           todo_type="teste urgente")
    # finded_todo = find_todo(1)
    # print(finded_todo)
    # print(new_todo)
    # new_folder = create_folder("teste folder")
    # new_type = create_todo_type("teste urgente")
