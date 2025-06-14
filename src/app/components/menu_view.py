import json
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMenuBar, QMenu
from src.app.dialog.connect2phone_dialog import Connect2PhoneDialog

class MenuView(QMenuBar):
    def __init__(self):
        super().__init__()

        self.config_path = "../config/menu_config.json"
        self.action_map = {
            "connect2phone": self.show_connect2phone_dialog
        }

        self.setup_ui()

    def setup_ui(self):
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)

            for menu_config in config.get("menus", []):
                menu = self._create_menu(menu_config)
                self.addMenu(menu)

        except Exception as e:
            print(f"菜单加载失败", {e})

    def _create_menu(self, menu_config):
        #创建单个菜单
        menu = QMenu(menu_config["title"], self)

        for item_config in menu_config.get("items", []):
            action = QAction(item_config["text"], self)
            menu.addAction(action)

            action_name = item_config.get("action")
            if action_name in self.action_map:
                action.triggered.connect(self.action_map[action_name])

        return menu

    def show_connect2phone_dialog(self):
        dialog = Connect2PhoneDialog()
        dialog.exec()
