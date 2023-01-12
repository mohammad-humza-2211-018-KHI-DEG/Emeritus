from typing import List

from sqlalchemy.orm import Session
from sqlalchemy import select, or_

from db import InspiringQuote, engine


def add_quote(author: str, content: str) -> None:
    with Session(engine) as session:
        quote = InspiringQuote(author=author, content=content)
        session.add(quote)
        session.commit()


def list_quotes() -> List[InspiringQuote]:
    with Session(engine) as session:
        return list(session.scalars(select(InspiringQuote)))


def search_quotes(query: str) -> List[InspiringQuote]:
    with Session(engine) as session:
        return list(
            session.scalars(
                select(InspiringQuote).where(
                    or_(
                        InspiringQuote.author.like("%" + query + "%"),
                        InspiringQuote.content.like("%" + query + "%"),
                    )
                )
            )
        )
