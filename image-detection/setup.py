def resolve_dependencies():
    import os

    os.system("python -m pip install -r image-detection/requirements.txt")


def setup():
    print("Setting up image detector...")
    resolve_dependencies()