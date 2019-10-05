import nox

nox.options.stop_on_first_error = True
nox.options.keywords = "not docs_watch"

source_files = ("httpx", "tools", "tests", "setup.py", "noxfile.py")


@nox.session(reuse_venv=True)
def lint(session):
    session.install("autoflake", "black", "flake8", "isort", "seed-isort-config")

    session.run("autoflake", "--in-place", "--recursive", *source_files)
    session.run("seed-isort-config", "--application-directories=httpx")
    session.run("isort", "--project=httpx", "--recursive", "--apply", *source_files)
    session.run("black", "--target-version=py36", *source_files)

    check(session)


@nox.session(reuse_venv=True)
def check(session):
    session.install(
        "black",
        "flake8",
        "flake8-bugbear",
        "flake8-comprehensions",
        "flake8-pie",
        "isort",
        "mypy",
    )

    session.run("black", "--check", "--diff", "--target-version=py36", *source_files)
    session.run("flake8", *source_files)
    session.run("mypy", "httpx")
    session.run(
        "isort", "--check", "--diff", "--project=httpx", "--recursive", *source_files
    )


@nox.session(reuse_venv=True)
def docs(session):
    session.install("mkdocs", "mkdocs-material")

    session.run("mkdocs", "build")


@nox.session(reuse_venv=True)
def docs_watch(session):
    session.install("mkdocs", "mkdocs-material")

    session.run("mkdocs", "serve")


@nox.session(python=["3.6", "3.7", "3.8"])
def test(session):
    session.install("-r", "test-requirements.txt")
    session.run("python", "-m", "pytest", *session.posargs)
