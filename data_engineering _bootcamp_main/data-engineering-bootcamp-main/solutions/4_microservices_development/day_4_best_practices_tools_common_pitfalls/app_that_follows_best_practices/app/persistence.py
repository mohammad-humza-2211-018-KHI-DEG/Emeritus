from typing import List

from sqlalchemy import Column, Integer, String, create_engine, select
from sqlalchemy.orm import declarative_base, Session

import config

Base = declarative_base()

engine = create_engine(config.DB_URL)


class TODOItem(Base):  # type: ignore
    __tablename__ = "todo_item"

    id = Column(Integer, primary_key=True)
    content = Column(String(3000))

    def __repr__(self):
        return f"TODOItem(id={self.id}, content={self.content})"


Base.metadata.create_all(engine)


def add_todo_item(content: str) -> None:
    with Session(engine) as session:
        todo_item = TODOItem(content=content)
        session.add(todo_item)
        session.commit()


def list_todo_items() -> List[str]:
    result = []

    with Session(engine) as session:
        todo_items = select(TODOItem)
        for todo_item in session.scalars(todo_items):
            result.append(todo_item.content)

    return result
