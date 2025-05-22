from pathlib import Path

file_path = Path("example.txt")

# Write
file_path.write_text("Using pathlib to write to a file.")

# Read
content = file_path.read_text()
print(content)