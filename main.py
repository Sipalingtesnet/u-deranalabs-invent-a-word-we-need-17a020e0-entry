"""This entry defines 'Chatgloom', the quiet emptiness that follows a group chat when everyone stops typing."""

import os

ENTRY_TEXT = "Chatgloom — the quiet emptiness that follows a group chat when everyone stops typing."

output_dir = "/output"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "entry.txt")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(ENTRY_TEXT)
