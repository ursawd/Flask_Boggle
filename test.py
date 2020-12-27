from unittest import TestCase
from app import app
from flask import session, jsonify, json
from boggle import Boggle

app.config["TESTING"] = True
app.config["DEBUG_TB-HOSTS"] = ["dont_shoe_debug_toolbar"]


class FlaskTests(TestCase):
    def test_index(self):
        with app.test_client() as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("<title>Boggle Game</title>", html)
            self.assertEqual(session["highscore"], 0)
            self.assertEqual(session["gamesplayed"], 0)

    def test_check_word(self):
        with app.test_client() as client:
            resp = client.post("/check_word", json={"word": "asdf"})
            data = json.loads(resp.get_data(as_text=True))
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(data["result"], "not-word")

    def test_check_word2(self):
        with app.test_client() as client:
            resp = client.post("/check_word", json={"word": "passymeasure"})
            data = json.loads(resp.get_data(as_text=True))
            self.assertEqual(data["result"], "not-on-board")

    def test_scores(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session["highscore"] = 0
            resp = client.post("/scores", json={"score": 10})
            data = json.loads(resp.get_data(as_text=True))
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(data["gamesplayed"], 1)
            self.assertEqual(data["highscore"], 10)
