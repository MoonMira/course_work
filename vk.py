import requests

class VK:

    def __init__(self, access_token, user_id, version='5.131'):
       self.token = access_token
       self.id = user_id
       self.version = version
       self.params = {'access_token': self.token, 'v': self.version}

#Получаем ссылки и значения фотографий(размеры,комментарии и прочее)
    def save_photo(self):
       url = 'https://api.vk.com/method/photos.get'
       params = {'owner_id': self.id,
                 'album_id': 'profile',
                 'rev': 0,
                 'extended': 1,
                 'photo_sizes': 1
                 }
       response = requests.get(url, params={**self.params, **params})
       return response.json()['response']['items']

    def max_size(self):
        sizes = {}
        max_size = ''
        for info_photo in response['response']['items']:
            for size in info_photo['sizes']:
                sizes[size['type']] = (size['width'] + size['height'])
                max_sizes = max(sizes)
                return


access_token = '---'
user_id = '-'
vk = VK(access_token, user_id)
user_photo = vk.save_photo()
max_photo = user_photo.max_size()
#print(vk.save_photo())
print(max_photo)