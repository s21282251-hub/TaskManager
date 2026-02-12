import unittest
from unittest.mock import patch
from app.main import get_weather_data


class TestWeather(unittest.TestCase):

    @patch("app.main.requests.get")
    def test_get_weather_data_success(self, mock_get):
        # Мокируем ответ API
        mock_get.return_value.json.return_value = {
            "location": {"name": "Moscow"},
            "current": {"temp_c": 5}
        }

        result = get_weather_data("fake_key", "Moscow")

        self.assertIn("location", result)
        self.assertIn("current", result)
        self.assertEqual(result["location"]["name"], "Moscow")


if __name__ == "__main__":
    unittest.main()
