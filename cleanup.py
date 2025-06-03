import os
import datetime

backup_dir = "/backup"
days_to_keep = 7
now = datetime.datetime.now()

for filename in os.listdir(backup_dir):
    filepath = os.path.join(backup_dir, filename)
    if os.path.isfile(filepath):
        file_time = datetime.datetime.fromtimestamp(os.path.getmtime(filepath))
        if (now - file_time).days > days_to_keep:
            os.remove(filepath)
            print(f"Deleted old backup: {filename}")
