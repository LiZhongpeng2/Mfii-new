import json
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMenuBar, QMenu

class MenuView(QMenuBar):
    def __init__(self, config_path):
        super().__init__()
        self.config_path = config_path
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

        return menu
