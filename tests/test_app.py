# tests/test_app.py

import unittest
import os
os.environ['TESTING'] = 'true'

from app import app, TimelinePost, mydb

class AppTestCase(unittest.TestCase):
    @classmethod
    def tearDownClass(cls):
        mydb.close()

    def setUp(self):
        self.client = app.test_client()
        TimelinePost.delete().execute()

        self.user1 = {"name": "John Doe", "email": "john@example.com", "content": "hello"}

    def _create_post(self, content = dict):
        return self.client.post("/api/timeline_post", data=content)
    
    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Caly Zheng</title>" in html
        # TODO Add more tests relating to the home page

    def test_get_empty_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0
    
    def test_get_nonempty_timeline(self):
        self._create_post(self.user1)

        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 1
        assert json["timeline_posts"][0]["name"] == self.user1["name"]

    def test_successful_post(self):
        response = self._create_post(self.user1)
        assert response.status_code == 200
        
    def test_missing_name_post(self):
        # POST request missing name
        data = self.user1.copy()
        del data["name"]
        response = self.client.post("/api/timeline_post", data=data)
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

    def test_empty_content_post(self):
        # POST request with empty content
        data = self.user1.copy()
        data["content"] = ""
        response = self. client. post("/api/timeline_post", data=data)
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html
    
    def test_invalid_email_post(self):
        # POST request with malformed email
        data = self.user1.copy()
        data["email"] = "not-an-email"
        response = self.client.post("/api/timeline_post", data=data)
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html

