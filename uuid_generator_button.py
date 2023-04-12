#!/Users/Julian/Desktop/Development/Projekte/uuid generator/env/Scripts/python

import uuid
import pyperclip
import os

file_path = os.path.join(os.getcwd(), "generated_uuids.txt")


with open(file_path, "r") as file:
    existing_uuids = set(line.strip() for line in file.readlines())


# UUID generieren
random_uuid = uuid.uuid4()
    
if random_uuid not in existing_uuids:
    existing_uuids.add(random_uuid)
    with open(file_path, "a") as file:
        file.write(str(random_uuid) + "\n")

    # UUID in die Zwischenablage kopieren
    pyperclip.copy(str(random_uuid))
