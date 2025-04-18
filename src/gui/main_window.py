from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QListWidget, QStackedWidget  

class MainWindow(QMainWindow):  
    def __init__(self):  
        super().__init__()  
        self.setWindowTitle("Agronomix-OSS")  
        self.resize(1200, 800)  

        # Sidebar Navigation  
        self.sidebar = QListWidget()  
        self.sidebar.addItems(["Ingredients", "Setup", "Reports"])  
        self.sidebar.currentRowChanged.connect(self.change_view)  

        # Content Area (Stacked Widget)  
        self.stacked_widget = QStackedWidget()  

        # Layout  
        layout = QHBoxLayout()  
        layout.addWidget(self.sidebar, stretch=1)  
        layout.addWidget(self.stacked_widget, stretch=4)  

        container = QWidget()  
        container.setLayout(layout)  
        self.setCentralWidget(container)

        self._load_styles()

        from .groups.ingredients_group import IngredientsGroup  
        from .groups.setup_group import SetupGroup  

        self.stacked_widget.addWidget(IngredientsGroup())  
        #self.stacked_widget.addWidget(SetupGroup())  
        #self.stacked_widget.addWidget(ReportsGroup())  

    def change_view(self, index):  
        self.stacked_widget.setCurrentIndex(index)

    def _load_styles(self) -> None:  
        with open("src/styles.qss", "r") as f:  
            self.setStyleSheet(f.read()) 

if __name__ == "__main__":  
    import sys  
    from PyQt6.QtWidgets import QApplication  
    
    app = QApplication(sys.argv)  
    window = MainWindow()  
    window.show()  
    sys.exit(app.exec())