import unittest
import requests
import pytest
from django.test import Client


class TestManga(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_manga_by_title(self):
        url = '/api/manga/'
        data = {'title': 'Боевой континент 2'}
        response = self.client.get(url, data)
        res = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['results'][0]['title'], data['title'])

    def test_get_manga_by_id(self):
        url = '/api/manga/875/'
        response = self.client.get(url)
        res = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['id'], 875)

    def test_get_manga_chapters(self):
        chapters_id = 2
        chapters_manga = 'Test Chapter'
        url = '/api/manga/875/chapters/'
        response = self.client.get(url)
        res = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res[0]['title'], chapters_manga)
        self.assertEqual(res[0]['id'], chapters_id)

    def test_get_image_chapters(self):
        url = '/api/manga/2/images/'
        response = self.client.get(url)
        res = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(res['image']) > 0)


