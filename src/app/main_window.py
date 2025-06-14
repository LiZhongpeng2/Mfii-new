from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QApplication, QHBoxLayout
from src.app.components.camera_view import CameraView
from src.app.components.menu_view import MenuView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #初始化
        self.center_widget = None
        self.main_layout = None
        self.top_layout = None
        self.camera_view_widget = None

        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Miff")
        self.setGeometry(50, 50, 600, 600)

        self.center_widget = QWidget()
        self.setCentralWidget(self.center_widget)

        self.main_layout = QVBoxLayout(self.center_widget)

        self.init_layout()

    def init_layout(self):

        #菜单栏
        menu_view = MenuView()
        self.setMenuBar(menu_view)

        #顶部水平布局：摄像头画面 图表
        self.top_layout = QHBoxLayout()
        self.camera_view_widget = CameraView()
        self.top_layout.addWidget(self.camera_view_widget)

        #添加到main_layout
        self.main_layout.addLayout(self.top_layout)

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()







