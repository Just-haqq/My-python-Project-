from pathlib import Path

path = Path()
for files in path.glob("*.py"):
    print(files)


path1 = Path()
for files in path1.glob("*"):
    print(files)