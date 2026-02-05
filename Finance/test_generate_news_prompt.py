import unittest
import sys
import os

# Ensure we can import the module from the current directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from generate_news_prompt import generate_prompt

class TestGenerateNewsPrompt(unittest.TestCase):
    def test_default_arguments(self):
        keyword = "Apple"
        prompt = generate_prompt(keyword)
        self.assertIn("查詢關鍵字：`Apple`", prompt)
        self.assertIn("時間範圍：`7 天`", prompt)
        self.assertIn("地區（可選）：`全球`", prompt)
        self.assertIn("關注面向：`宏觀經濟`", prompt)

    def test_custom_arguments(self):
        keyword = "Tesla"
        time_range = "30 天"
        region = "美國"
        focus = "公司財報"
        prompt = generate_prompt(keyword, time_range, region, focus)
        self.assertIn("查詢關鍵字：`Tesla`", prompt)
        self.assertIn("時間範圍：`30 天`", prompt)
        self.assertIn("地區（可選）：`美國`", prompt)
        self.assertIn("關注面向：`公司財報`", prompt)

    def test_prompt_structure(self):
        keyword = "Test"
        prompt = generate_prompt(keyword)
        self.assertIn("## 📌 Google 財經新聞分析 Prompt（專業版）", prompt)
        self.assertIn("## 📊 輸出結構（必須遵守）", prompt)
        self.assertIn("### 5️⃣ 結論摘要（Neutral Takeaway）", prompt)

if __name__ == '__main__':
    unittest.main()
