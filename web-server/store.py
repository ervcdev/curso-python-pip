import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code) #ver el estado
    print(r.text) #ver la respuesta o retorno
    print(type(r.text))
    
    #transformacion en formato python
    categories = r.json() #transformacion en formato diccionarios
    for category in categories:
        print(category['name'] )



