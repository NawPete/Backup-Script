
# Backup Script

This Python script is designed to create a backup of a specified directory by archiving it into a ZIP file. The script generates a backup file with a name that includes the current date and time, ensuring unique backups. This is a simple solution to automate file backups for directories that need regular archiving.

## Features

- **Creates a ZIP archive**: The script compresses the entire source directory into a `.zip` file.
- **Timestamp in backup name**: The backup file is named with the current date and time to avoid overwriting previous backups.
- **Customizable paths**: You can easily adjust the source directory and backup destination paths to fit your needs.

## Use Case

This script can be useful for system administrators, developers, or anyone who needs to automate regular backups of important directories. It can be scheduled to run periodically (e.g., using `cron` on Linux) to ensure that critical data is always backed up.

## Prerequisites

- Python 3.x must be installed on your machine.
- Ensure you have sufficient permissions to read from the source directory and write to the backup directory.

## How to Run the Script

1. **Clone the Repository**

   First, clone this GitHub repository to your local machine:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```

2. **Navigate to the Directory**

   Move into the directory containing the script:

   ```bash
   cd your-repo-name
   ```

3. **Modify the Source and Backup Paths**

   Open the script file and modify the `source` and `backup_dir` variables to point to the directories you want to back up and where you want to store the backups.

   ```python
   source = "/path/to/source_directory"
   backup_dir = "/path/to/backup_directory"
   ```

4. **Run the Script**

   To create a backup, execute the following command:

   ```bash
   python3 backup_script.py
   ```

5. **Output**

   After running the script, you will see a message confirming the creation of the backup, along with the path to the generated ZIP file:

   ```
   Backup created successfully: /path/to/backup_directory/backup_2024-10-20_12-00-00.zip
   ```

## Example Usage

- **Automated Backups**: Integrate this script with task schedulers like `cron` on Linux or `Task Scheduler` on Windows to automate daily, weekly, or monthly backups.
- **Backup Multiple Directories**: Modify the script to create backups for multiple directories by running the script multiple times with different paths.

## Customization

- You can modify the script to include additional logging or email notifications after successful backups.
- You can also adjust the backup format by changing the archive format in the `shutil.make_archive` function, such as using `'tar'` instead of `'zip'` for different compression types.

## Automating the Backup with Cron (Linux/macOS)

To automate the script using **cron** on Linux or macOS, follow these steps:

1. **Edit the crontab file**

   Open the crontab file by running the following command in your terminal:

   ```bash
   crontab -e
   ```

   This will open your user's crontab file for editing. If it's the first time, you might be prompted to choose an editor (e.g., nano or vim).

2. **Add a cron job**

   To schedule the backup script to run at a specific time (e.g., daily at 2:00 AM), add the following line to the crontab file:

   ```bash
   0 2 * * * /usr/bin/python3 /path/to/your-repo-name/backup_script.py
   ```

   Here's a breakdown of the cron schedule:

   - `0 2 * * *` – This means the script will run at 2:00 AM every day.
   - `/usr/bin/python3` – This is the path to your Python 3 interpreter. You can verify the correct path by running `which python3` in your terminal.
   - `/path/to/your-repo-name/backup_script.py` – This should be the full path to your backup script.

3. **Save and exit**

   Save the changes to the crontab file and exit the editor. Now, the script will run automatically every day at 2:00 AM.

4. **Check Cron Logs**

   If you want to check whether the cron job is running successfully, you can view the system's cron logs by running the following command:

   ```bash
   grep CRON /var/log/syslog
   ```

   This will display logs related to cron jobs, including any errors or successful executions of your script.

## Automating the Backup on Windows with Task Scheduler

1. Open **Task Scheduler** on your Windows machine.
2. Create a new task by clicking on "Create Basic Task."
3. Set the trigger to run daily at the desired time (e.g., 2:00 AM).
4. Set the action to start a program, and choose `python.exe` as the program.
5. In the arguments field, provide the path to your `backup_script.py` file.

Now, your backup script will run automatically based on the specified schedule.

