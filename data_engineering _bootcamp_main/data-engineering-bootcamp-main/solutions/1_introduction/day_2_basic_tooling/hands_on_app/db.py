from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class InspiringQuote(Base):  # type: ignore
    __tablename__ = "inspiring_quote"

    id = Column(Integer, primary_key=True)
    author = Column(String(300))
    content = Column(String(3000))

    def __repr__(self) -> str:
        return f"InspiringQuote(id={self.id}, author={self.author}, content={self.content})"


engine = create_engine("sqlite:///db.sqlite3")
Base.metadata.create_all(engine)
