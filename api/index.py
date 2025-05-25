from fastapi import FastAPI, Request
import json

app = FastAPI ()

@app.get("/")
def index ():
    return {
                "message": "Welcome to the First FastAPI App!"
            }

json_data = '[{"name":"0","marks":85},{"name":"YISaLDs","marks":59},{"name":"ALk","marks":69},{"name":"rlS","marks":95},{"name":"TVOkFD","marks":90},{"name":"kl5EA","marks":7},{"name":"DaNi","marks":89},{"name":"Lb","marks":31},{"name":"6YC","marks":23},{"name":"AZr","marks":17},{"name":"yvj7TkF2","marks":2},{"name":"qdz","marks":37},{"name":"VQkx","marks":76},{"name":"OvDjQi","marks":24},{"name":"uvjXa","marks":82},{"name":"dl70Cuo","marks":23},{"name":"KKIuBRGyrq","marks":30},{"name":"v8EjvA","marks":20},{"name":"l","marks":62},{"name":"y9dNSY","marks":1},{"name":"KLMjveQ9fV","marks":46},{"name":"V","marks":5},{"name":"6mwsFXbt","marks":38},{"name":"glBA","marks":50},{"name":"f","marks":77},{"name":"bAP","marks":78},{"name":"t91l","marks":72},{"name":"z","marks":87},{"name":"N","marks":33},{"name":"U1Raeb15","marks":45},{"name":"im9a","marks":55},{"name":"bCN2","marks":30},{"name":"cJkOL1aV4","marks":13},{"name":"sd8UZA8d","marks":86},{"name":"xiqBatKYa","marks":95},{"name":"dPz","marks":34},{"name":"WJLzxyft0K","marks":83},{"name":"3aU6H2kz7Y","marks":10},{"name":"r5hX","marks":29},{"name":"s","marks":54},{"name":"wE5GOZ1C","marks":57},{"name":"WlutP9","marks":51},{"name":"Pripps6N","marks":97},{"name":"eU","marks":0},{"name":"fbxPQKpD","marks":67},{"name":"JJVVoqPGZK","marks":45},{"name":"kFTlL0W","marks":21},{"name":"aLFm0unZ","marks":53},{"name":"8OK","marks":67},{"name":"3tD","marks":91},{"name":"bxDFVHm","marks":57},{"name":"QTtwMZ","marks":68},{"name":"BwaO","marks":75},{"name":"gQRw","marks":24},{"name":"2OQ683kb2W","marks":32},{"name":"CFO","marks":78},{"name":"xYy7L0SgjI","marks":76},{"name":"ERM8c","marks":2},{"name":"z7Zp","marks":48},{"name":"ykzOMJaGn","marks":44},{"name":"E79ClmtK","marks":5},{"name":"PG","marks":86},{"name":"OUO4a1","marks":15},{"name":"Xu4fkmaDxw","marks":59},{"name":"oj","marks":78},{"name":"GZn19c0z8u","marks":54},{"name":"hhw5NjLJba","marks":99},{"name":"sfHD2mZFAu","marks":25},{"name":"03YDE","marks":95},{"name":"9uXD","marks":7},{"name":"lUt14a","marks":44},{"name":"yH6O","marks":84},{"name":"HAllwo2Yb","marks":45},{"name":"Rc6JrC","marks":22},{"name":"L9zdS","marks":1},{"name":"10eOm6dShf","marks":12},{"name":"S","marks":60},{"name":"KJCiS","marks":7},{"name":"d7Dxn","marks":5},{"name":"4j8ovH","marks":50},{"name":"xx4IqUYYb","marks":98},{"name":"HspiIxN","marks":43},{"name":"P","marks":31},{"name":"dQLIiW","marks":85},{"name":"45H7","marks":84},{"name":"yeTyfUS","marks":6},{"name":"4PCgRe","marks":27},{"name":"aZIUrD","marks":13},{"name":"FYpVk3","marks":6},{"name":"9A","marks":54},{"name":"tu1UJgHO9F","marks":75},{"name":"jLAGx4RV","marks":52},{"name":"m3w","marks":33},{"name":"pVb","marks":36},{"name":"u5O","marks":21},{"name":"SwWxG2j","marks":71},{"name":"e6v1mMKB","marks":94},{"name":"fkrVLn0a","marks":2},{"name":"ojwGx4L9my","marks":77},{"name":"XQnD","marks":15}]'
data = json.loads(json_data)

@app.get("/api/params")
def api (request: Request):
    params = request.query_params
    name = params.get("name", None)
    marks = params.get("marks", None)

    if name is not None and marks is not None:
        try:
            marks = int(marks)
        except ValueError:
            return {"error": "Marks must be an integer."}

        data.append({"name": name, "marks": marks})
        return {"message": "Data added successfully."}
    
    return {"marks": marks}