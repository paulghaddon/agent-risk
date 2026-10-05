import typer

app = typer.Typer()


@app.callback()
def main():
    """agent-risk: adversarial pre-deployment validation for AI agents."""


@app.command()
def check():
    """Run the validation suite (placeholder until ticket 1.2)."""
    typer.echo("agent-risk: no checks implemented yet (ticket 1.2+)")


if __name__ == "__main__":
    app()
