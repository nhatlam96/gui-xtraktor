from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QLabel, QSizePolicy
from PyQt5.QtCore import Qt


class FullScreenImage(QMainWindow):
    def __init__(self, image_path):
        super().__init__()
        self.setWindowTitle("Full Screen Image")

        content_widget = QWidget(self)
        self.setCentralWidget(content_widget)

        layout = QHBoxLayout(content_widget)
        layout.setAlignment(Qt.AlignCenter)

        label = QLabel()
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        pixmap = QPixmap(image_path)
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignCenter)
        label.setScaledContents(True)

        layout.addWidget(label)

        label.mousePressEvent = self.close_fullscreen

    @staticmethod
    def show_fullscreen(event, pixmap):
        if event.button() == Qt.LeftButton:
            fullscreen_window = FullScreenImage(pixmap)
            fullscreen_window.show()

    def close_fullscreen(self, event):
        self.close()


