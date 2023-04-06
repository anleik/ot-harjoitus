from invoke import task
import sys



@task
def foo(ctx):
    print("bar")

@task
def start(ctx):
    if sys.platform == "win32":
        ctx.run("python src/main.py")
    else:
        ctx.run("python src/main.py", pty=True)


@task
def test(ctx):
    if sys.platform == "win32":
        ctx.run("pytest src")
    else:
        ctx.run("pytest src", pty=True)

@task
def coverage(ctx):
    if sys.platform == "win32":
        ctx.run("coverage run --branch -m pytest src")
    else:
        ctx.run("coverage run --branch -m pytest src", pty=True)


@task(coverage)
def coverage_report(ctx):
    if sys.platform == "win32":
        ctx.run("coverage html")
    else:
        ctx.run("coverage html", pty=True)

@task
def lint(ctx):
    if sys.platform == "win32":
        ctx.run("pylint src")
    else:
        ctx.run("pylint src", pty=True)
