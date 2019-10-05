# Contributing

Thank you for being interested in contributing to HTTPX.
There are many ways you can contribute to the project:

- Try HTTPX and [report bugs/issues you find](https://github.com/encode/httpx/issues/new)
- [Implement new features](https://github.com/encode/httpx/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)
- [Review Pull Requests of others](https://github.com/encode/httpx/pulls)
- Write documentation
- Participate in discussions

## Reporting Bugs or Other Issues

Found something that HTTPX should support?
Stumbled upon some unexpected behavior?

Feel free to open an issue at the
[issue tracker](https://github.com/encode/httpx/issues).
Try to be more descriptive as you can and in case of a bug report,
provide as much information as possible like:

- OS platform
- Python version
- Installed dependencies and versions (`python -m pip freeze`)
- Code snippet
- Error traceback

## Development

To start developing HTTPX create a **fork** of the
[HTTPX repository](https://github.com/encode/httpx) on GitHub.

Then clone your fork with the following command replacing `YOUR-USERNAME` with
your GitHub username:

```shell
$ git clone https://github.com/YOUR-USERNAME/httpx
```

With the repository cloned you can access its folder, set up the
virtual environment, install the project requirements,
and then install HTTPX on edit mode:

```shell
$ cd httpx
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r test-requirements.txt
$ pip install -e .
```

!!! note
    Feel free to replace this step with your development environment setup
    (pyenv, pipenv, virtualenvwrapper, docker, etc).

## Testing and Linting

We use [nox](https://nox.thea.codes/en/stable/) to automate testing, linting,
and documentation building workflow. Make sure you have it installed
at your system before starting.

Install `nox` with:

```shell
$ python3 -m pip install --user nox
```

Alternatively, use [pipx](https://github.com/pipxproject/pipx) if you prefer
to keep it into an isolated environment:

```shell
$ pipx install nox
```

Now, with nox installed, run the complete pipeline with:

```shell
$ nox
```

!!! warning
    The test suite spawns a testing server at the port **8000**.
    Make sure this isn't being used, so the tests can run properly.

To run the code auto-formatting separately:

```shell
$ nox -s lint
```

Also, if you need to run the tests only:

```shell
$ nox -s test
```

You can also run a single test script like this:

```shell
$ nox -s test -- tests/test_multipart.py
```

## Documenting

Documentation pages are located under the `docs/` folder.

To run the documentation site locally (useful for previewing changes), use:

```shell
$ nox -s docs_watch
```

## Releasing

*This section is targeted at HTTPX maintainers.*

Before releasing a new version, create a pull request that includes:

- **An update to the changelog**:
    - We follow the format from [keepachangelog](https://keepachangelog.com/en/1.0.0/).
    - [Compare](https://github.com/encode/httpx/compare/) `master` with the tag of the latest release, and list all entries that are of interest to our users:
        - Things that **must** go in the changelog: added, changed, deprecated or removed features, and bug fixes.
        - Things that **should not** go in the changelog: changes to documentation, tests or tooling.
        - Try sorting entries in descending order of impact / importance.
        - Keep it concise and to-the-point. 🎯
- **A version bump**: see `__version__.py`.

For an example, see [#362](https://github.com/encode/httpx/pull/362).

Once the release PR is merged, run `$ scripts/publish` to publish the new release to PyPI.
