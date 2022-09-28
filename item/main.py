from fastapi import FastAPI, Depends, status , Response, HTTPException
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session 
from typing import List



app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
          db.close()

models.Base.metadata.create_all(engine)

@app.post('/item',status_code=status.HTTP_201_CREATED,tags=['items'])
def create(request: schemas.Item, db:Session = Depends(get_db)):
    new_item = models.Item(id=request.id, item_descp=request.item_descp , supplier=request.supplier)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


@app.delete('/item/{id}', status_code=status.HTTP_204_NO_CONTENT,tags=['items'])
def destroy(id, db:Session = Depends(get_db)):
    db.query(models.Item).filter(models.Item.id == id).delete(synchronize_session=False)
    db.commit()
    return 'done'

@app.put('/item/{id}',status_code=status.HTTP_202_ACCEPTED,tags=['items'])
def update(id, request: schemas.Item, db:Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == id)
    item.update(request)    
    
    db.commit()
    return 'updated'

@app.get('/item',response_model=List[schemas.ShowItem],tags=['items'])
def all(db:Session = Depends(get_db)):
    items = db.query(models.Item).all()
    return  items



@app.get('/item/{id}', status_code=200, response_model=schemas.ShowItem ,tags=['items'])
def SHOW(id,response : Response,db:Session = Depends(get_db)):
    items = db.query(models.Item).filter(models.Item.id == id).first() 
    if not items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Item with the id {id} is not available")
        # response.status_code = status.HTTP_404_NOT_FOUND  
        # return {'detail' : f"Item with the id {id} is not available"}
    return items 



@app.post('/cpmrp',response_model=schemas.Show_cpmrp,tags=['cpmrp'])
def create_cpmrp(request: schemas.CPMRP, db:Session = Depends(get_db)):
    new_cpmrp = models.CPMRP(cpmrp_item=request.cpmrp_item,item = request.item, city = request.city, cost = request.cost)
    db.add(new_cpmrp)
    db.commit()
    db.refresh(new_cpmrp)
    return new_cpmrp



@app.get('/cpmrp/{cpmrp_item}', status_code=200, response_model=schemas.Show_cpmrp,tags=['cpmrp'] )
def get_cpmrp(cpmrp_item:int, db:Session = Depends(get_db)):
    cpmrp = db.query(models.CPMRP).filter(models.CPMRP.cpmrp_item == cpmrp_item).first() 
    if not cpmrp:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Item with the id {cpmrp_item} is not available")
        # response.status_code = status.HTTP_404_NOT_FOUND  
        # return {'detail' : f"Item with the id {id} is not available"}
    return cpmrp


# @app.get('/join',)
# def joins(Session = Depends(get_db)):
#     q = Session.query(models.Item).join(models.CPMRP, models.Item.id==models.CPMRP.cpmrp_item)
#     return q

    