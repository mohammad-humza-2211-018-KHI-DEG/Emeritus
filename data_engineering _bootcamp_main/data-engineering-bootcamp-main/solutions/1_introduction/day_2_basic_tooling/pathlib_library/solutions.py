from pathlib import Path

# get parent directory of /an/example/path
print(Path("/an/example/path").parents[0])
# find all files under /etc
print([item for item in Path("/etc").rglob("*") if item.is_file()])
# join /an/example/directory and filename.txt to get the path of filename.txt if it would reside /an/example/directory
print(Path("/an/example/directory") / "filename.txt")
# query whether /etc exists,
print(Path("/etc").exists())
# query whether /etc is a directory.
print(Path("/etc").is_dir())
