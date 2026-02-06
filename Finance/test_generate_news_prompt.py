import unittest
import sys
import os

# Append the current directory to sys.path to import the module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import generate_news_prompt

class TestGenerateNewsPrompt(unittest.TestCase):
    def test_generate_prompt(self):
        keyword = "Tesla"
        time_range = "7 天"
        region = "全球"
        focus = "市場波動"

        prompt = generate_news_prompt.generate_prompt(keyword, time_range, region, focus)

        self.assertIn(f"查詢關鍵字：{keyword}", prompt)
        self.assertIn(f"時間範圍：{time_range}", prompt)
        self.assertIn(f"地區（可選）：{region}", prompt)
        self.assertIn(f"關注面向：{focus}", prompt)

        self.assertIn("Google 財經新聞分析 Prompt（專業版）", prompt)

if __name__ == '__main__':
    unittest.main()
