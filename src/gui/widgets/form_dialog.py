from PyQt6.QtWidgets import QDialog, QFormLayout, QLineEdit, QDialogButtonBox  

class FormDialog(QDialog):  
    def __init__(self, fields):  
        super().__init__()  
        self.setWindowTitle("Add/Edit Entry")  
        layout = QFormLayout()  

        self.inputs = {}  
        for field in fields:  
            self.inputs[field] = QLineEdit()  
            layout.addRow(field, self.inputs[field])  

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)  
        buttons.accepted.connect(self.accept)  
        buttons.rejected.connect(self.reject)  
        layout.addWidget(buttons)  

        self.setLayout(layout)

    def get_validated_inputs(self) -> dict:  
        """Returns inputs only if all required fields are filled."""  
        required_fields = ["Code", "Name"]  
        return {  
            field: self.inputs[field].text().strip()  
            for field in self.inputs  
            if field not in required_fields or self.inputs[field].text().strip()  
        }  