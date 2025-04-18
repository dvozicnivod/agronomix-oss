import pytest  
from src.gui.groups.ingredients_group import IngredientsGroup  

@pytest.fixture  
def ingredients_group(qtbot):  
    widget = IngredientsGroup()  
    qtbot.addWidget(widget)  
    return widget  

def test_add_entry(ingredients_group):  
    initial_rows = ingredients_group.table.rowCount()  
    ingredients_group.add_entry()  # Mock dialog input  
    assert ingredients_group.table.rowCount() == initial_rows + 1  