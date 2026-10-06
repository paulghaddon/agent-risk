import typer

from agent_risk import __version__

app = typer.Typer()


@app.callback()
def main():
    """agent-risk: adversarial pre-deployment validation for AI agents."""


@app.command()
def check():
    """Run the validation suite (placeholder until ticket 1.2)."""
    typer.echo("agent-risk: no checks implemented yet (ticket 1.2+)")


@app.command()
def version():
    """Print the agent-risk version."""
    typer.echo(f"agent-risk v{__version__}")


if __name__ == "__main__":
    app()
