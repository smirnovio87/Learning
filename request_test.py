import requests
url="https://petstore.swagger.io/v2/pet/1"
url_2="https://petstore.swagger.io/v2/tag"

response=requests.get(url_2)
# if response.status_code==200:
#     pet=response.json()
#     print("Информация о питомце:", pet["id"], pet["name"])
# else:
#     print ("Ошибка:", response.status_code)

if response.status_code==200:
    tags=response.json()
    for tag in tags:
        print(tag["id"], tag["name"])
else:
    print("Ошибка:", response.status_code)

    
