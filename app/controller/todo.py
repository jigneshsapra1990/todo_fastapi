from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.database.schema.todo_schema import TodoSchema
from app.models.todo import CreateTodo


def get_all_todos(db: Session):
    todos = db.query(TodoSchema).all()
    return {"message": "List of TODO items", "data": todos}


def get_todo_by_id(id: int, db: Session):
    todo = db.query(TodoSchema).filter(TodoSchema.id == id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo item", "data": todo}


def create_todo(item: CreateTodo, db: Session):
    todo = TodoSchema(
        title=item.title,
        description=item.description,
        completed=item.isCompleted
    )
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {"message": "Todo created successfully", "data": todo}


def update_todo(id: int, item: CreateTodo, db: Session):
    todo = db.query(TodoSchema).filter(TodoSchema.id == id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo.title = item.title
    todo.description = item.description
    todo.completed = item.isCompleted
    db.commit()
    db.refresh(todo)
    return {"message": "Todo updated successfully", "data": todo}


def delete_todo(id: int, db: Session):
    todo = db.query(TodoSchema).filter(TodoSchema.id == id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return {"message": "Todo deleted successfully"}
