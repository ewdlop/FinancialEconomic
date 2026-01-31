import unittest
import sys
import os

# Add the directory containing the script to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from generate_news_prompt import generate_prompt

class TestGenerateNewsPrompt(unittest.TestCase):
    def test_default_values(self):
        keyword = "TSLA"
        prompt = generate_prompt(keyword)
        self.assertIn(f"查詢關鍵字：{keyword}", prompt)
        self.assertIn("時間範圍：7 天", prompt)
        self.assertIn("地區（可選）：全球", prompt)
        self.assertIn("關注面向：宏觀經濟", prompt)

    def test_custom_values(self):
        keyword = "Apple"
        time_range = "30 天"
        region = "美國"
        focus = "公司財報"
        prompt = generate_prompt(keyword, time_range, region, focus)
        self.assertIn(f"查詢關鍵字：{keyword}", prompt)
        self.assertIn(f"時間範圍：{time_range}", prompt)
        self.assertIn(f"地區（可選）：{region}", prompt)
        self.assertIn(f"關注面向：{focus}", prompt)

    def test_prompt_structure(self):
        # Verify some key static parts of the prompt exist
        keyword = "Test"
        prompt = generate_prompt(keyword)
        self.assertIn("角色設定（Role）", prompt)
        self.assertIn("任務（Task）", prompt)
        self.assertIn("輸出結構（必須遵守）", prompt)
        self.assertIn("新聞總覽（News Overview）", prompt)

if __name__ == '__main__':
    unittest.main()
