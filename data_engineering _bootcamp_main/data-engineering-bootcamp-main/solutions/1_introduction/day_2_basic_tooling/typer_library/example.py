import typer


def main(name: str = typer.Option("John"), surname: str = typer.Option(...)):
    print(f"Hello {name} {surname}")


if __name__ == "__main__":
    typer.run(main)
