
from pymongo import Connection

db = Connection()["wikilife_main_live"]

#todos los nodos con el nombre de la comida
for node in db.meta.find({"fields.parent": 511}):
    print node["fields"].get("food_type", "No Food Type")
    print node["fields"].get("brand_name", "No Brand Name")
    print node["fields"]["title"]
    #Nodo Size, no importa, solo sirve para obtener sus hijos
    size_node = db.meta.find_one({"fields.parent": node["_id"]})
    for serving_node in  db.meta.find({"fields.parent": size_node["_id"]}):
        print serving_node["fields"]["properties"]["serving_description"]
        