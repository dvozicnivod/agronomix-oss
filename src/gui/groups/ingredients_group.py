from PyQt6.QtWidgets import (  
    QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem,  
    QHeaderView, QPushButton, QMessageBox  
)  
from PyQt6.QtCore import Qt  
from ..widgets.form_dialog import FormDialog  
import pandas as pd  
import os  

class IngredientsGroup(QWidget):  
    def __init__(self):  
        super().__init__()  
        self.data_path = "data/sample_ingredients.csv"  
        self.init_ui()  
        self.load_data()  

    def init_ui(self):  
        layout = QVBoxLayout()  

        # Buttons  
        btn_layout = QHBoxLayout()  
        self.add_btn = QPushButton("Add Ingredient")  
        self.edit_btn = QPushButton("Edit")  
        self.delete_btn = QPushButton("Delete")  
        btn_layout.addWidget(self.add_btn)  
        btn_layout.addWidget(self.edit_btn)  
        btn_layout.addWidget(self.delete_btn)  

        # Table  
        self.table = QTableWidget()  
        self.table.setColumnCount(9)  
        self.table.setHorizontalHeaderLabels([  
            "Code", "Name", "Scientific Name", "Volume", "Group",  
            "Type", "Charged By", "Charged On", "Active"  
        ])  
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)  
        self.table.setSortingEnabled(True)  

        # Connect buttons  
        self.add_btn.clicked.connect(self.add_entry)  
        self.edit_btn.clicked.connect(self.edit_entry)  
        self.delete_btn.clicked.connect(self.delete_entry)  

        layout.addLayout(btn_layout)  
        layout.addWidget(self.table)  
        self.setLayout(layout)  

    def load_data(self)-> None:  
        """Loads ingredient data from CSV or initializes sample data."""
        os.makedirs(os.path.dirname(self.data_path), exist_ok=True)
        
        if not os.path.exists(self.data_path):
            # Create file with headers
            df = pd.DataFrame(columns=[
                "Code", "Name", "Scientific Name", "Volume", 
                "Group", "Type", "Charged By", "Charged On", "Active"
            ])
            df.to_csv(self.data_path, index=False)
        
        try:
            df = pd.read_csv(self.data_path)
            if df.empty:
                raise ValueError("Empty CSV")
        except (pd.errors.EmptyDataError, ValueError):
            df = self._create_sample_data()
            df.to_csv(self.data_path, index=False)

        self._populate_table(df)

    def _populate_table(self, df):
        """Populate the table widget with DataFrame data."""
        self.table.setRowCount(len(df))
        for row_idx, row in df.iterrows():
            for col_idx, col in enumerate(df.columns):
                value = str(row[col]) if not pd.isna(row[col]) else ""
                item = QTableWidgetItem(value)
                item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
                self.table.setItem(row_idx, col_idx, item)

    def _create_sample_data(self):
        return pd.DataFrame([{
            "Code": "1001258",
            "Name": "Conova Oil Coat",
            "Scientific Name": "Additives",
            "Group": "pycnova",
            "Charged On": "2017-10-29 14:56:37",
            "Active": "✅"
        }])  

    def _validate_entry(self, data: dict) -> bool:  
        """Check for mandatory fields (Code, Name)."""  
        if not data.get("Code") or not data.get("Name"):  
            QMessageBox.warning(self, "Error", "Code and Name are required!")  
            return False  
        return True 

    def add_entry(self) -> None:
        fields = ["Code", "Name", "Scientific Name", "Volume", "Group", "Type", "Charged By", "Charged On", "Active"]  
        dialog = FormDialog(fields)  
        if dialog.exec() and self._validate_entry(new_data): 
            new_data = {field: dialog.inputs[field].text() for field in fields}  
            self._save_to_csv(new_data)  
            self.load_data()  

    def _save_to_csv(self, data):  
        df = pd.DataFrame([data])  
        if os.path.exists(self.data_path):  
            df.to_csv(self.data_path, mode='a', header=False, index=False)  
        else:  
            df.to_csv(self.data_path, index=False)  

    def edit_entry(self):  
        selected = self.table.currentRow()  
        if selected == -1:  
            QMessageBox.warning(self, "Error", "Select an entry to edit!")  
            return  

        # Get current data  
        data = {  
            "Code": self.table.item(selected, 0).text(),  
            "Name": self.table.item(selected, 1).text(),  
            "Scientific Name": self.table.item(selected, 2).text(),
            "Volume": self.table.item(selected, 3).text(),
            "Group": self.table.item(selected, 4).text(),
            "Type": self.table.item(selected, 5).text(),
            "Charged By": self.table.item(selected, 6).text(),
            "Charged On": self.table.item(selected, 7).text(),
            "Active": self.table.item(selected, 8).text()
        }  

        dialog = FormDialog(data.keys())  
        for field, value in data.items():  
            dialog.inputs[field].setText(value)  
        if dialog.exec():  
            # Update logic here  
            self.load_data()  

    def delete_entry(self):  
        selected = self.table.currentRow()  
        if selected == -1:  
            QMessageBox.warning(self, "Error", "Select an entry to delete!")  
            return  

        # Logic to delete the entry from CSV  
        df = pd.read_csv(self.data_path)  
        df.drop(selected, inplace=True)  
        df.to_csv(self.data_path, index=False)  
        self.load_data()
        QMessageBox.information(self, "Success", "Entry deleted successfully!")