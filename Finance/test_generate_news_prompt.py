import unittest
import sys
import os

# Add the directory containing the script to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from generate_news_prompt import generate_prompt

class TestGenerateNewsPrompt(unittest.TestCase):
    def test_generate_prompt_defaults(self):
        # Test with just the keyword, mimicking default args for others
        prompt = generate_prompt("Apple", "7 天", "全球", "宏觀經濟")
        self.assertIn("* 查詢關鍵字：`Apple`", prompt)
        self.assertIn("* 時間範圍：`7 天`", prompt)
        self.assertIn("* 地區（可選）：`全球`", prompt)
        self.assertIn("* 關注面向：`宏觀經濟`", prompt)

    def test_generate_prompt_custom(self):
        # Test with custom arguments
        prompt = generate_prompt("Tesla", "24 小時", "美國", "市場波動")
        self.assertIn("* 查詢關鍵字：`Tesla`", prompt)
        self.assertIn("* 時間範圍：`24 小時`", prompt)
        self.assertIn("* 地區（可選）：`美國`", prompt)
        self.assertIn("* 關注面向：`市場波動`", prompt)

    def test_prompt_content(self):
        # Verify some static content exists
        prompt = generate_prompt("Test", "Test", "Test", "Test")
        self.assertIn("角色設定（Role）", prompt)
        self.assertIn("Google 財經新聞分析 Prompt（專業版）", prompt)
        self.assertIn("## 📊 輸出結構（必須遵守）", prompt)

if __name__ == '__main__':
    unittest.main()
