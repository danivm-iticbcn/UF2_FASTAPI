from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field


app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="Descripcion del item", max_length=5
    )
    price: float = Field(gt=0, description="El precio tiene que ser mayor que 0")
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results