import unittest
import sys
import os

# Add the directory containing the script to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from generate_news_prompt import generate_prompt

class TestGenerateNewsPrompt(unittest.TestCase):
    def test_generate_prompt_defaults(self):
        prompt = generate_prompt(keyword="Apple")
        self.assertIn("查詢關鍵字：`Apple`", prompt)
        self.assertIn("時間範圍：`7 天`", prompt)
        self.assertIn("地區（可選）：`全球`", prompt)
        self.assertIn("關注面向：`宏觀經濟`", prompt)

    def test_generate_prompt_custom(self):
        prompt = generate_prompt(keyword="TSMC", time_range="30 天", region="亞洲", focus="公司財報")
        self.assertIn("查詢關鍵字：`TSMC`", prompt)
        self.assertIn("時間範圍：`30 天`", prompt)
        self.assertIn("地區（可選）：`亞洲`", prompt)
        self.assertIn("關注面向：`公司財報`", prompt)

if __name__ == '__main__':
    unittest.main()
