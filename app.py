from flask import Flask,request,jsonify

app=Flask(__name__)

items=[
    {
        "name":" Green apple mojito",
        "price":200
    },
    {
        "name":"Momos",
        "price":60
    }
]
         #get all items of cafe http://127.0.0.1:5000/grt-items

@app.get('/get-items')
def get_all_items():
    return {"items":items}

         #get a single item from cafe items http://127.0.0.1:5000/items/___

@app.get('/get-item/<string:name>')
def get_item(name):
    for item in items:
        if item['name']==name:
           return item
    return {"massage":"item doen't found"}

         #create single item in items of  menu
@app.post('/get-items')
def create_item():
    body_data=request.get_json()
    items.append(body_data)
    return {"massage":"item created successfully"}
#update the item in menu by using put methods http://127.0.0.1:5000/______
@app.put('/update-item')
def update_item():
    request_data=request.get_json()
    for item in items:
        if  item['name']==request_data['name']:
            item['price']=request_data['price']
            return {"massage":"item updated successfully"}
    return {"massage":"doesn't update"}

#delete the item from menu
@app.delete('/delet-item/<string:name>')
def delete_item(name):
    for item in items :
        if name==item['name']:
            items.remove(item)
            return {"massage":"item is deleted successfully"}
    return {"item doen't exit "}


app.run(port=5000)