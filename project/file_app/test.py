
from rest_framework import status
from rest_framework.test import APITestCase

from .models import File

URL = 'http://127.0.0.1:8000/api/'


class File_app_tests(APITestCase):
    def setUp(self) -> None:
        File.objects.create(file='./files/Интернет.rtf')

    def test_get_files_list(self):
        response = self.client.get(f'{URL}files')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(File.objects.count(), 1)
        print(response.data)

    def test_upload_file(self):
        with open('./files/lopatin.jpg', 'rb') as f:
            headers = {
                'Content-Type': 'multipart/form-data',
                'Content-Disposition': 'attachment; filename=lopatin.jpg',
            }
            response = self.client.post('http://127.0.0.1:8000/api/upload', file='./files/lopatin.jpg', headers=headers)
            print(response.status_code, headers)

