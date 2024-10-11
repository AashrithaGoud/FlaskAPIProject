#This script sends a POST request to the Flask API with data from the local JSON file.
#
# import json
# import requests
#
# json_file='./Data/products_data_2024-10-10_13-21-24.json'
# with open(json_file,'r') as f:
#     data=json.load(f)
#
# url='http://127.0.0.1:5000/products'
#
# response=requests.post(url,json=data)
#
# print(response.json())