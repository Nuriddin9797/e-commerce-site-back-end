import os
from fastapi import FastAPI, HTTPException
from starlette.responses import FileResponse
from routes.laptops import laptops_router
from routes.telephones import telephones_router
from routes.categories import categories_router
from routes.planshets import planshets_router
from routes.users_router import users_router
from routes.likes import likes_router
from routes.login import login_router
from routes.files import files_router
from routes.cart import cart_router
from routes.order import order_router
from routes.income import income_router
from routes.purchase import purchase_router

app = FastAPI(docs_url='/')


app.include_router(login_router)
app.include_router(users_router)
app.include_router(categories_router)
app.include_router(laptops_router)
app.include_router(planshets_router)
app.include_router(telephones_router)
app.include_router(likes_router)
app.include_router(cart_router)
app.include_router(order_router)
app.include_router(income_router)
app.include_router(purchase_router)
app.include_router(files_router)


@app.get('/files/{fileName}')
async def get_file(fileName: str):
    path = f"./files/{fileName}"
    if os.path.isfile(path):
        return FileResponse(path)
    else:
        raise HTTPException(400, "Not Found")