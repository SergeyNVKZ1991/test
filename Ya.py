import requests


def get_folder_in_path(path, token):
    url_upload = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {token}'
            }
    params = {'path': path}
    respons = requests.get(url_upload, headers=headers, params=params)
    return respons

def create_folder(file_path, token):
    url_upload = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {token}'
            }
    params = {'path': file_path, 'overwrite': 'true'}
    respons = requests.put(url_upload, headers=headers, params=params)
    return respons

def delete_folder(folder_path, token):
    url_upload = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {token}'
            }
    params = {'path': folder_path}
    respons = requests.delete(url_upload, headers=headers, params=params)
    return respons