from PyQt6.QtWidgets import QLabel, QSizePolicy


class CameraView(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        #QLabel尺寸策略：跟随内容大小
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.setScaledContents(True)

        self.setText("等待摄像头连接...")





