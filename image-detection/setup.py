def resolve_dependencies():
    import os

    os.system("python -m pip install -r webserver/requirements.txt")


def setup():
    print("Setting up image detector...")
    resolve_dependencies()