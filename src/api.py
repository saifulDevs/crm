from fastapi import FastAPI

from src.todos.controller import router as todos_router
from src.auth.controller import router as auth_router
from src.users.controller import router as users_router
from src.agents.controller import router as agents_router
from src.tasks.controller import router as tasks_router
from src.tickets.controller import router as tickets_router
# You can keep adding more routers as your modules grow

def register_routes(app: FastAPI):
    app.include_router(auth_router, prefix="/auth", tags=["Auth"])
    app.include_router(users_router, prefix="/users", tags=["Users"])
    app.include_router(todos_router, prefix="/todos", tags=["Todos"])
    app.include_router(agents_router, prefix="/agents", tags=["Agents"])
    app.include_router(tasks_router, prefix="/tasks", tags=["Tasks"])
    app.include_router(tickets_router, prefix="/tickets", tags=["Tickets"])
