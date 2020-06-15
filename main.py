from fastapi import FastAPI
from pydantic import BaseModel
import sys, os

sys.path.insert(0, '/src')
sys.path.append('/src')

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.get("/", summary="Home dir")
async def root():
    """
    Function to return data on home dir
    """
    return {"message": "Hello User"}


@app.get("/password", summary="Get a randomly generated password")
async def read_item(pwd_length: int, use_symbols: bool):
    """
    Requires Params:<br>
    - pwd_length: (int) Length of password to be generated.
    - use_symbols: (bool) Whether or not to use symbols in pwd generation

    Returns:<br>
    - randomly generated password

    """
    print(os.getcwd())
    from PasswordGenerator import pwdg as file
    pwd = file.PasswordGenerator().generate_password(p_length=pwd_length, use_symbols=use_symbols)
    return {"password": pwd}


#optional parameters
@app.get("/pass/{p_length}{use_symbol}")
async def read_item(p_length: int = None, use_symbols: bool = None):

    from PasswordGenerator import pwdg as file

    if p_length:
        pwd = file.PasswordGenerator().generate_password(p_length=p_length,use_symbols=use_symbols)
    else:
        pwd = file.PasswordGenerator().generate_password()

    #test
    print(pwd)
    return {"password": pwd}

# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(
#     user_id: int, item_id: str, q: str = None, short: bool = False
# ):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item