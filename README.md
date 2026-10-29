# Case Notes — Week 1 starter

Build the Northstar handoff workbench from the client brief supplied with this starter.
Continue your completed application in Week 2; there is no second starting application.

## Start

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then run these commands
from this directory. uv selects Python 3.13 using .python-version.

```sh
uv sync --locked
uv run --locked uvicorn app:app --host 127.0.0.1 --port 8000 --reload
```

Open http://127.0.0.1:8000. The initial page confirms only that the starter runs.
The API documentation is at /docs; /health returns a small health response.
Stop the server with Ctrl+C.

To use a local environment file, copy .env.example to .env once, keeping any existing settings,
and use the following command instead:

```sh
uv run --locked --env-file .env uvicorn app:app --host 127.0.0.1 --port 8000 --reload
```

APP_TITLE changes the title in the API documentation. No model credentials are required to boot.
Ask the trainer for approved model access before implementing live calls. Keep credentials on
the server, never in browser code or a committed file. Extend the safe example to match the
settings you introduce; it intentionally does not select a model or provider for you.

## What is here

| Location | Purpose |
|---|---|
| app.py | FastAPI entry point, page/static-file routes and health response |
| static/ | A plain page and stylesheet you can replace or extend |
| data/notes.json | Twenty fictional development notes |
| data/follow-up-notes.json | More notes for a second handoff batch |
| data/evaluation.json | Public development expectations; never model input |
| data/README.md | File format, examples and evaluation boundaries |
| tests/test_smoke.py | Bootstrap checks only |
| pyproject.toml, uv.lock, .python-version | Dependency and Python setup |
| .env.example, .gitignore | Safe starter settings and local-file exclusions |

You implement all five client features, storage, model integration, evaluator and application
checks. There is no finished data model, AI response schema, domain route, CI workflow or
static-analysis setup. Choose a frontend and storage appropriate for the task; plain HTML is
fine. You may reorganize the skeleton. The starter does not call external services or create
application data on startup.

The supplied bootstrap, static page, environment example, ignore rules and smoke tests are
trainer work, not your assessed contribution. Maintain them as your implementation grows.
The client brief defines the requested product; the learner guide defines essays and submission.

## Check your setup

```sh
uv run --locked pytest
```

These checks confirm the bootstrap and that project files are not exposed as page routes.
Passing them does not mean note saving, extraction, searches or exports work. Add checks for
what you build. Keep evaluation labels out of model requests and production extraction.

Use `uv add <package>` or `uv add --dev <package>` for dependency changes, then commit the
updated pyproject.toml and uv.lock. Add appropriate static analysis yourself. Put local runtime
data in an ignored location; runtime/ is already ignored if you choose to use it. Keep reusable
synthetic input fixtures in data/.
