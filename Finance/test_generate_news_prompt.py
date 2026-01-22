import unittest
import os
import sys
from unittest.mock import patch

# Add the directory containing the script to sys.path
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)

import generate_news_prompt

class TestGenerateNewsPrompt(unittest.TestCase):
    def test_generate_prompt_success(self):
        keyword = "TSMC"
        time_range = "7 Days"
        region = "Asia"
        focus = "Earnings"

        prompt = generate_news_prompt.generate_prompt(keyword, time_range, region, focus)

        # The template has backticks around the placeholders, e.g. `{...}`
        # Our replacement logic replaces the content inside the backticks (the brace part).
        # So we expect `TSMC` to appear.
        self.assertIn(f"查詢關鍵字：`{keyword}`", prompt)
        self.assertIn(f"時間範圍：`{time_range}`", prompt)
        self.assertIn(f"地區（可選）：`{region}`", prompt)
        self.assertIn(f"關注面向：`{focus}`", prompt)

        # Ensure the original placeholders are gone
        self.assertNotIn("{公司 / 產業 / 國家 / 商品 / 主題}", prompt)
        self.assertNotIn("{過去 24 小時 / 7 天 / 30 天}", prompt)

    def test_generate_prompt_missing_file(self):
        # Mock os.path.exists to return False
        with patch('os.path.exists', return_value=False):
            with self.assertRaises(FileNotFoundError):
                generate_news_prompt.generate_prompt("k", "t", "r", "f")

if __name__ == '__main__':
    unittest.main()
