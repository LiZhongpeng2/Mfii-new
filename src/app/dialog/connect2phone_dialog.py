from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QDialogButtonBox, QMessageBox
)
from src.log.logger import logger

class Connect2PhoneDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("DroidCamIP配置")
        self.setFixedSize(400, 200)
        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout(self)

        layout.addLayout(self._build_input_row("Device IP:", "请输入Device IP：", "ip_input"))
        layout.addLayout(self._build_input_row("DroidCam Port:", "请输入端口号：", "port_input", default="4747"))
        layout.addLayout(self._build_tips_block())
        layout.addStretch()
        layout.addWidget(self._build_button_box())

    def _build_input_row(self, label_text, placeholder, attr_name, default=""):
        row = QHBoxLayout()
        label = QLabel(label_text)
        input_field = QLineEdit()
        input_field.setPlaceholderText(placeholder)
        if default:
            input_field.setText(default)
        row.addWidget(label)
        row.addWidget(input_field)
        setattr(self, attr_name, input_field)  # 动态绑定属性，如 self.ip_input
        return row

    def _build_tips_block(self):
        layout = QVBoxLayout()
        layout.addLayout(self._tip_row("Tips:"))
        layout.addLayout(self._tip_row('<a href="https://droidcam.app/">入门与下载DroidCam</a>', is_link=True))
        layout.addLayout(self._tip_row("请在手机端DroidCam查看Device IP"))
        layout.addLayout(self._tip_row("默认端口号(DroidCam Port): 4747"))
        return layout

    def _tip_row(self, text, is_link=False):
        row = QHBoxLayout()
        label = QLabel()
        if is_link:
            label.setText(text)
            label.setOpenExternalLinks(True)
        else:
            label.setText(text)
        row.addWidget(label)
        row.addStretch()
        return row

    def _build_button_box(self):
        button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        button_box.button(QDialogButtonBox.StandardButton.Ok).setText("保存")
        button_box.button(QDialogButtonBox.StandardButton.Cancel).setText("取消")
        button_box.accepted.connect(self._save_config)
        button_box.rejected.connect(self.reject)
        return button_box

    def _save_config(self):
        ip = self.ip_input.text().strip()
        port = self.port_input.text().strip()
        if ip and port:
            self.saved_ip = ip
            self.saved_port = port
            self.accept()
        else:
            QMessageBox.warning(self, "输入有误", "设备IP或端口均不能为空，请重试！")
            logger.warning("输入IP或端口号为空")

    def get_camera_config(self):
        return getattr(self, "saved_ip", ""), getattr(self, "saved_port", "")
