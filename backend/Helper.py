from PyQt5.QtCore import QTimer, QSize
from PyQt5.QtWidgets import QMessageBox


class WindowSizeHandler:
    minimum_size: QSize
    maximum_size: QSize

    @staticmethod
    def set_sizes(minimum_size: QSize, maximum_size: QSize):
        WindowSizeHandler.minimum_size = minimum_size
        WindowSizeHandler.maximum_size = maximum_size

    @staticmethod
    def get_minimum_size():
        return WindowSizeHandler.minimum_size

    @staticmethod
    def get_maximum_size():
        return WindowSizeHandler.maximum_size


def update_main_window_size(main_window):
    main_window.setMinimumSize(WindowSizeHandler.get_minimum_size())
    main_window.setMaximumSize(WindowSizeHandler.get_maximum_size())


class UserHandler:
    current_user: str

    @staticmethod
    def get_current_user():
        return UserHandler.current_user

    def set_current_user(self: str):
        UserHandler.current_user = self


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
