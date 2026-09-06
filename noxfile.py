import nox
import nox_uv

nox.options.default_venv_backend = "uv"
nox.options.sessions = ["typecheck", "lint"]
nox.options.error_on_external_run = True


@nox_uv.session(venv_backend="none")
def typecheck(session: nox.Session) -> None:
    session.run("pyrefly", "check")


@nox_uv.session(venv_backend="none")
@nox.parametrize(
    "command",
    [
        nox.param(["ruff", "format", "--check"], id="format"),
        nox.param(["ruff", "check", "--no-fix"], id="rules"),
    ],
)
def lint(session: nox.Session, command: list[str]) -> None:
    session.run(*command)


@nox_uv.session(venv_backend="none")
@nox.parametrize(
    "command",
    [
        nox.param(["ruff", "format"], id="format"),
        nox.param(["ruff", "check", "--fix", "--unsafe-fixes"], id="rules"),
    ],
)
def tidy(session: nox.Session, command: list[str]) -> None:
    session.run(*command)
