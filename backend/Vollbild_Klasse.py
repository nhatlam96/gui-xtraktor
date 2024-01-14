from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QLabel, QSizePolicy, QScrollArea
from PyQt5.QtCore import Qt


class FullScreenImage(QMainWindow):
    def __init__(self, image_path):
        super().__init__()
        self.setWindowTitle("Full Screen Image")
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.resize(1000, 700)
        self.zoom_wert = 1.0

        content_widget = QWidget(self)
        self.setCentralWidget(content_widget)

        layout = QHBoxLayout(content_widget)
        layout.setAlignment(Qt.AlignCenter)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        layout.addWidget(scroll_area)

        scroll_content = QWidget()
        scroll_layout = QHBoxLayout(scroll_content)
        scroll_layout.setAlignment(Qt.AlignCenter)

        self.pixmap = QPixmap(image_path)
        self.label = QLabel()
        self.label.setPixmap(self.pixmap)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setScaledContents(True)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        scroll_layout.addWidget(self.label)
        scroll_area.setWidget(scroll_content)

        self.label.mousePressEvent = self.handle_mouse_event

    def handle_mouse_event(self, event):
        if event.button() == Qt.LeftButton:
            self.zoom_wert += 0.3
            self.zoom()
        elif event.button() == Qt.RightButton:
            self.zoom_wert = self.zoom_wert - 0.3 if self.zoom_wert - 0.3 >= 1.0 else 1.0
            self.zoom()

    def zoom(self):
        pic_zoomed = self.pixmap.transformed(QTransform().scale(self.zoom_wert, self.zoom_wert))
        self.label.setPixmap(pic_zoomed)

    @staticmethod
    def show_fullscreen(event, pixmap):
        if event.button() == Qt.LeftButton:
            fullscreen_window = FullScreenImage(pixmap)
            fullscreen_window.show()
