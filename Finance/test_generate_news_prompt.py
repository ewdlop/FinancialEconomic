import unittest
import sys
import os

# Append the current directory (repo root) to sys.path so we can import Finance.generate_news_prompt
sys.path.append(os.getcwd())

from Finance.generate_news_prompt import generate_prompt

class TestGenerateNewsPrompt(unittest.TestCase):

    def test_default_values(self):
        # Test with just keyword, defaults should be used
        keyword = "NVDA"
        prompt = generate_prompt(keyword, "7 天", "全球", "宏觀經濟")

        self.assertIn(f"* 查詢關鍵字：`{keyword}`", prompt)
        self.assertIn("* 時間範圍：`7 天`", prompt)
        self.assertIn("* 地區（可選）：`全球`", prompt)
        self.assertIn("* 關注面向：`宏觀經濟`", prompt)

    def test_custom_values(self):
        # Test with all custom values
        keyword = "Bitcoin"
        time_range = "24 hours"
        region = "US"
        focus = "Crypto Market"

        prompt = generate_prompt(keyword, time_range, region, focus)

        self.assertIn(f"* 查詢關鍵字：`{keyword}`", prompt)
        self.assertIn(f"* 時間範圍：`{time_range}`", prompt)
        self.assertIn(f"* 地區（可選）：`{region}`", prompt)
        self.assertIn(f"* 關注面向：`{focus}`", prompt)

    def test_template_structure(self):
        # Test if key sections exist
        keyword = "Test"
        prompt = generate_prompt(keyword, "7 天", "全球", "宏觀經濟")

        self.assertIn("## 📌 Google 財經新聞分析 Prompt（專業版）", prompt)
        self.assertIn("### 1️⃣ 新聞總覽（News Overview）", prompt)
        self.assertIn("### 5️⃣ 結論摘要（Neutral Takeaway）", prompt)

if __name__ == '__main__':
    unittest.main()
