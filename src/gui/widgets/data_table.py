from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
from PyQt6.QtCore import Qt
import pandas as pd

class DataTable(QTableWidget):
    def __init__(self, headers, data_path=None):
        super().__init__()
        self.headers = headers
        self.data_path = data_path
        self.init_table()
        
    def init_table(self):
        self.setColumnCount(len(self.headers))
        self.setHorizontalHeaderLabels(self.headers)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        if self.data_path:
            self.load_data()

    def load_data(self) -> None:  
        """Populates table from CSV. Silently fails if file is missing."""
        try:
            df = pd.read_csv(self.data_path)
            self.setRowCount(len(df))
            for row_idx, row in df.iterrows():
                for col_idx, value in enumerate(row):
                    item = QTableWidgetItem(str(value))
                    item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
                    self.setItem(row_idx, col_idx, item)
        except FileNotFoundError:
            pass
    
    def add_search_bar(self) -> None:  
        self.search_bar = QLineEdit()  
        self.search_bar.setPlaceholderText("Search...")  
        self.search_bar.textChanged.connect(self.filter_rows)  

    def filter_rows(self, text: str) -> None:  
        for row in range(self.rowCount()):  
            match = any(  
                text.lower() in self.item(row, col).text().lower()  
                for col in range(self.columnCount())  
            )  
            self.setRowHidden(row, not match) 