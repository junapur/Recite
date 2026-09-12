import cyclopts

app = cyclopts.App(
    name="recite",
    help="Lightweight text-to-speech for your terminal",
    help_epilogue="See the [Github](https://github.com/junapur/Recite) for more!",
    version_flags=["--version", "-v"],
    exit_on_error=True,
)

@app.default()
def main() -> None:
    msg = "Oops, not ready yet! :["
    raise NotImplementedError(msg)
