import unittest
import sys
import os

# Ensure we can import the module from the current directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from generate_news_prompt import generate_prompt

class TestGenerateNewsPrompt(unittest.TestCase):

    def test_generate_prompt_defaults(self):
        prompt = generate_prompt(keyword="Tesla")
        self.assertIn("查詢關鍵字：`Tesla`", prompt)
        self.assertIn("時間範圍：`7 天`", prompt)
        self.assertIn("地區（可選）：`全球`", prompt)
        self.assertIn("關注面向：`宏觀經濟`", prompt)

    def test_generate_prompt_custom(self):
        prompt = generate_prompt(
            keyword="Apple",
            time_range="30 天",
            region="美國",
            focus="公司財報"
        )
        self.assertIn("查詢關鍵字：`Apple`", prompt)
        self.assertIn("時間範圍：`30 天`", prompt)
        self.assertIn("地區（可選）：`美國`", prompt)
        self.assertIn("關注面向：`公司財報`", prompt)

    def test_prompt_structure(self):
        prompt = generate_prompt("Test")
        self.assertIn("角色設定（Role）", prompt)
        self.assertIn("任務（Task）", prompt)
        self.assertIn("新聞總覽（News Overview）", prompt)
        self.assertIn("關鍵資訊整理（Key Facts）", prompt)
        self.assertIn("市場影響分析（Market Impact）", prompt)
        self.assertIn("風險與不確定性（Risks & Uncertainty）", prompt)
        self.assertIn("結論摘要（Neutral Takeaway）", prompt)

if __name__ == '__main__':
    unittest.main()
