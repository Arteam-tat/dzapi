import requests
import json
from setting import TOKEN

class YaUploader:
    def __init__(self, token: str):
        self.token = TOKEN


    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        uri = 'v1/disk/resources/upload'
        url = self.HOST + uri
        pparam = {path_to_file.split('\\')[-1]}
        params = {'path': f'{pparam},"overwrite":"true"'}
        response = requests.get(url, headers=get_headers, params=params)
        upload_link = response.json()['href']
        print(upload_link)
        resp = requests.put(upload_link, headers=self.get_headers(), data=open(path_to_file))
        if resp.status_code == 200 or 201:
            print("ok")



if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    host = 'https://cloud-api.yandex.net/'
    get_headers = {'Content_Type': 'application/json', 'Authorization': f'OAuth {TOKEN}'}
    uri = 'v1/disk/recources/upload'
    url = host + uri
    name_file = 'data.json'
    params = {'path': f'/{name_file}'}
    response = requests.get(url, headers=get_headers, params=params)
    path_to_file = '/Users/artem/Desktop/on git/dz'
    print(response.json())
    print(response.status_code)
