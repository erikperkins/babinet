import unittest
from api.main import app

class TestMain(unittest.TestCase):
  def setUp(self):
    self.ctx = app.app_context()
    self.ctx.push()
    self.client = app.test_client()

  def tearDown(self):
    self.ctx.pop()

  def test_hello_world(self):
    response = self.client.get("/")
    self.assertEqual(200, response.status_code)
    self.assertEqual("Hello, Docker!\n", response.text)

  def test_echo(self):
    body = {'hello': 'world'}
    response = self.client.post("/echo", json = body)
    self.assertEqual(200, response.status_code)
    self.assertEqual(body, response.json)
