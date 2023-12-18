import os
import time
import arrow

PROGRAM_TIME_FILE_PATH = os.path.join("..", "resources", "csv", "ProgramTime.csv")


def get_program_time():
    with open(PROGRAM_TIME_FILE_PATH, 'r') as time_file:
        program_time_str = time_file.read().strip()
        return arrow.get(program_time_str, "YYYY-MM-DD HH:mm:ss")


def save_program_time(program_time):
    with open(PROGRAM_TIME_FILE_PATH, 'w') as time_file:
        time_file.write(program_time.format("YYYY-MM-DD HH:mm:ss"))


def update_program_time():
    updated_time = get_program_time().shift(months=2)
    save_program_time(updated_time)
    return updated_time


while True:
    time.sleep(10)
    print(update_program_time())
