from PyQt6.QtWidgets import QWidget, QVBoxLayout
from src.gui.widgets.data_table import DataTable

class SetupGroup(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        
        self.table = DataTable(
            headers=["Unit", "Type", "Description"],
            data_path="data/setup_units.csv"
        )
        
        layout.addWidget(self.table)
        self.setLayout(layout)