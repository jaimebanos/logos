from config import  API_LOGO
import requests
import os
import json

def get_logos(logo_name:str, name:str):
    url = f'https://img.logo.dev/{logo_name}?token={API_LOGO}'
    response = requests.get(url)

    if response.status_code == 200:
        with open(os.path.join('logos', f'{name}.png'), 'wb') as f:
            f.write(response.content)

        return True
    
  
    return False



def check(new_records:str, record):
    news = []
    f = open(new_records)
    new_records_json = json.load(f)

    
    for t in new_records_json:
        new = True
        for n in record:
            if t["ISIN"] == n["ISIN"]:
                
                new = False
                break
        if new:
            news.append(t)
    
    print(f"Se han detectado {len(news)} nuevas empresas")
    return news

def read_json(path:str):
    try:
        f = open(path)
        return json.load(f)
    except Exception:
        return []
def main():
    record = read_json("record.json")
    num_errores = 0
    descargados = 0
    content_json = check('content.json', record)
    new_json = []
    for t in content_json:
        print(t)
        wensite_clean = t["website"].replace("https://", "").replace("http://", "").replace("www.", "")

        logo_name = wensite_clean.split('.')[0]
        if get_logos(wensite_clean, logo_name):
            new_json.append({
                "logo":f"{logo_name}.png",
                **t, 
            })
            descargados += 1
        else:
            num_errores += 1
            
        
    new_json.extend(record)
    
    print(f"Terminado. Se han descargado {descargados} logos. Se han detectado {num_errores} errores.")

  

    with open("record.json", 'w') as f:
        
        json.dump(new_json, f)
        



if __name__ == '__main__':
    main()


