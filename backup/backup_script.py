import shutil
import os
from datetime import datetime

source = "/path/to/source_directory"
backup_dir = "/path/to/backup_directory"

backup_name = f"backup_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.zip"
backup_path = os.path.join(backup_dir, backup_name)

shutil.make_archive(backup_path.replace('.zip', ''), 'zip', source)

print(f"Backup created successfully: {backup_path}")
