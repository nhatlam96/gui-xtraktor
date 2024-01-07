import os
import time

import arrow

from backend.Helper import get_program_time

PROGRAM_TIME_FILE_PATH = os.path.join("..", "resources", "csv", "ProgramTime.csv")


def get_launch_time():
    with open(PROGRAM_TIME_FILE_PATH, 'r') as time_file:
        # Skip the header line
        time_file.readline().strip()
        launch_time_str, _ = time_file.readline().strip().split(',')
        return arrow.get(launch_time_str, "YYYY-MM-DD HH:mm:ss")


# get_program_time() moved to Helper.py

def save_program_time(program_time):
    program_time_formatted = program_time.format("YYYY-MM-DD HH:mm:ss")
    lines = []

    with open(PROGRAM_TIME_FILE_PATH, 'r') as time_file:
        # Read the header line
        header_line = time_file.readline().strip()
        lines.append(header_line)

        # Read the rest of the lines
        for line in time_file:
            lines.append(line.strip())

    # Update the program_time
    launch_time_extracted = lines[1].split(",")[0].strip()
    updated_line = f"{launch_time_extracted},{program_time_formatted}\n"
    lines[1] = updated_line

    # Write the updated lines back to the file
    with open(PROGRAM_TIME_FILE_PATH, 'w') as time_file:
        time_file.write("\n".join(lines))

    return program_time_formatted


def save_launch_time(program_time):
    # Currently, the launch_time is the same as the program_time
    launch_time_formatted = program_time.format("YYYY-MM-DD HH:mm:ss")
    lines = []

    with open(PROGRAM_TIME_FILE_PATH, 'r') as time_file:
        # Read the header line
        header_line = time_file.readline().strip()
        lines.append(header_line)

        # Read the rest of the lines
        for line in time_file:
            lines.append(line.strip())

    # Update the launch_time
    program_time_extracted = lines[1].split(",")[1].strip()
    updated_line = f"{launch_time_formatted},{program_time_extracted}\n"
    lines[1] = updated_line

    # Write the updated lines back to the file
    with open(PROGRAM_TIME_FILE_PATH, 'w') as time_file:
        time_file.write("\n".join(lines))

    return launch_time_formatted


def update_launch_time():
    saved_time = save_launch_time(get_program_time())
    return saved_time


def update_program_time(months):
    updated_time = get_program_time().shift(months=months)
    saved_time = save_program_time(updated_time)
    return saved_time


# get_time_difference_since_program_time() moved to Helper.py


# initialises the LaunchTime at every program launch
launch_time = save_launch_time(get_program_time())
while True:
    time.sleep(1000)
    update_program_time(2)
