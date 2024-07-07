from datetime import datetime
import asyncio                                              #Since all the methods should be async


# Creating instances for the ToDo items as instructed with parameters: (1. id 2. description 3. created_on 4. completed_on)

class Todo_Items: 
    def __init__(self, id: int, description: str, created_on: datetime, completed_on: datetime):
        self.id = id
        self.description = description
        self.created_on = datetime.now()
        self.completed_on = datetime.now()
        
    


class TodoApp:
    def __init__(self):
        self.todo: {Todo_Items}
        
    # 1. Method to create an item
    async def create(self, description: str) -> Todo_Items: # /*This async create method will create an item using the description as a parameter-
        un_id = int(len(self.todo ) + 1)                    # and a unique id for the item. after that it will parse those arguments into the todo dictionary*/
        todo_item = Todo_Items(un_id, description)
        self.todo[un_id] = todo_item
        return todo_item
        
    
    # 2. Method to update and make changes to the items
    async def update(self, todo_id: int, description: str): # The update method checks the todo dictionary to see if the todo_id to check if it exists within 
        for todo_item in self.todo:                         # the data structure and then is going to modify the description of the retrieved TodoItem
            if todo.id == todo_id:
                todo.description = description
                return todo
            else:
                raise ValueError('id not found!')
    
    # 3. Method to delete a todo item
    async def delete(self, todo_id: int, value: str):       # This delete method checks to see if todo dictionary has an item and the deletes if found
        value = "Empty item"
        if todo_id not in self.todo:
            return value
        del self.todo[todo_id]
        
    # 4. Method to set the todo  item as being complete
    async def complete(self, todo_id: int):
        for todo_item in self.todo:
            if todo_item.id == todo_id:
                todo_item.completed_on = Todo_Items.completed_on 
                return todo_item
            else:
                return ValueError('Not complete!')
            
    # 5. Method to filter the itema
    async def filter(self, part_text: str) -> Todo_Items:
        filter_list = []
        for todo in self.todo:
            if part_text is not filter_list:
                filter_list = Todo_Items.completed_on
            if filter_list.completed_on == Todo_Items.completed_on:
                filter_list.append(Todo_Items.completed_on)
            if part_text.lower() in Todo_Items.description.lower():
                filter_list.append(todo) 
        else:
            return ValueError('Not completed!')
                
    
    async def new():
        return TodoApp()
    