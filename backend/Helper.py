from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox


class UserHandler:
    current_user = ""

    @staticmethod
    def set_current_user(username):
        UserHandler.current_user = username

    @staticmethod
    def get_current_user():
        return UserHandler.current_user


def show_toast(message, icon, button):
    toast = QMessageBox()
    toast.setIcon(icon)
    toast.setText(message)
    toast.setWindowTitle("Notification")
    toast.setStandardButtons(button)

    timer = QTimer(toast)
    # https://youtrack.jetbrains.com/issue/PY-24183/PyQt5-cannot-find-refernece-connect-in-funciton
    # https://stackoverflow.com/questions/64505166/cannot-find-reference-connect-in-function
    # noinspection PyUnresolvedReferences
    timer.timeout.connect(toast.close)
    timer.start(1750)

    toast.exec_()
