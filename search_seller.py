import json,argparse,time
import requests

parser = argparse.ArgumentParser(description="Get_items_for_seller_id + LOG | args: token,seller_id")
parser.add_argument('-t', '--token', type=str, required=True, help='Token de conexion')
parser.add_argument('-i', '--seller_id', type=str,required=True, help='id de vendedor/ra')

args = parser.parse_args()

token = args.token
seller_id = args.seller_id
info = {'access_token':token}


url = f"https://api.mercadolibre.com/sites/MLA/search?seller_id="+seller_id
headers = {
    'Accept: application/json'
}
params = {
    'access_token':info['access_token']
}
data = {
    'seller_id':seller_id
}

response = requests.get(url, params=params)

if(response.status_code == 200 ):
    try:
        with open('response.json', 'w') as access_json:
            json.dump(response.json(), access_json)
        
        with open('response.json') as file:
            read_content = json.load(file)

        save_data = []
        def get_items_data():
            items_seller = read_content['results']
            for item in items_seller:
                item_id = item['id']
                item_title = item['title']
                save_data.append({"id":item_id,"title":item_title})
            return save_data
        
        def get_categorie():
            items_seller = read_content['filters']
            for categoria in items_seller:
                categories_access = categoria['values']
                for data in categories_access:
                    category_id = data['id']
                    category_name = data['name']
                    save_data.append({"id":category_id,"name":category_name})
            return save_data

        get_categorie()
        get_items_data()
        print("Status--> wait,exporting data en LOG...")
        time.sleep(5)
        
        with open('log_seller_items.json', 'w') as file:
            json.dump(save_data, file, indent=4,ensure_ascii=False)
        print("Status--> export finished")
    except Exception as e:
        print("Errores en la Lectura/Escritura del archivo ",e)
else:
    print("Request failed, resource not found or expired token")
