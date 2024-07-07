import pytest
from src.TodoApp import Todo_Items, TodoApp
import datetime

async def test_create_item():
    app = await TodoApp.new()
    todo_action = await app.create("Purchase car wheels")
    assert todo.id == 1
    assert todo.description == "Purchase car wheels"
    assert todo.completed_on is None
    
async def test_update_item():
    app = await TodoApp.new()
    todo_action1 = await app.create("Purchase model type")
    todo_action2 = await app.update(todo_action1.id, "Purchase car color")
    assert todo_action2.id == todo_action1.id
    assert todo_action2.description == "Purchase car color"
    
async def test_delete_item():
    app = await TodoApp.new()
    todo_action = await app.create("Purchase car seats")
    await app.delete(Todo_Items.id)
    assert Todo_Items.completed_on is not None
    with pytest.raises(ValueError):
        return app
    
async def test_completed_on():
    app = await TodoApp.new()
    todo = await app.create("Purchase car engine")
    
async def test_filter_text():
    app = await TodoApp.new()
    todo_action1 = await app.create("Purchase1")
    todo_action2 = await app.create("Purchase2")
    filter_result = await app.filter(test_completed_on=True)
    
    
    
    