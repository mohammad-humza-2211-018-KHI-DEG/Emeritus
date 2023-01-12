import typer

import quote_library

app = typer.Typer()


@app.command()
def add_quote(author: str, content: str) -> None:
    quote_library.add_quote(author, content)
    print("Quote added successfully")


@app.command()
def list_quotes() -> None:
    for quote in quote_library.list_quotes():
        print("Author:", quote.author)
        print("Content:", quote.content)
        print()


@app.command()
def search_quotes(query: str) -> None:
    for quote in quote_library.search_quotes(query):
        print("Author:", quote.author)
        print("Content:", quote.content)
        print()


if __name__ == "__main__":
    app()
