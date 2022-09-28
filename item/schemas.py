from pydantic import BaseModel
from typing import List

 
class Item(BaseModel):
    id : int
    item_descp:str
    supplier:str
    class Config():
        orm_mode = True


class CPMRP(BaseModel):
    cpmrp_item : int
    item : str
    city : str
    cost : str
    class Config():
        orm_mode = True




class ShowItem(BaseModel):
    item_descp:str
    supplier:str
    owner : List[CPMRP] = []
    


    class Config():
        orm_mode = True



class Show_cpmrp(BaseModel):
    cpmrp_item : int
    item : str
    city : str
    cost : str
    items_table : Item
    class Config():
        orm_mode = True