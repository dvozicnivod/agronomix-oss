# reports_group.py  
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton  
from ..widgets.data_table import DataTable  

class ReportsGroup(QWidget):  
    def __init__(self):  
        super().__init__()  
        layout = QVBoxLayout()  
        self.export_btn = QPushButton("Export to Excel")  
        self.export_btn.clicked.connect(self.export_data)  
        layout.addWidget(self.export_btn)  
        self.setLayout(layout)  

    def export_data(self) -> None:  
        pass