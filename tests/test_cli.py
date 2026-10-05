from typer.testing import CliRunner
from agent_risk.cli import app

runner = CliRunner()


def test_check_runs():
    result = runner.invoke(app, ["check"])
    assert result.exit_code == 0
    assert "no checks implemented yet" in result.output
