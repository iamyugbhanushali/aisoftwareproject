from pathlib import Path

def read_file(path):
    return Path(path).read_text(
        encoding="utf-8"
    )

def list_files(root):

    return [
        str(p)
        for p in Path(root).rglob("*")
        if p.is_file()
    ]

def write_file(path, content):

    path = Path(path)

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    path.write_text(
        content,
        encoding="utf-8"
    )