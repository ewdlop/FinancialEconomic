import unittest
import sys
import os

# Add the directory containing the module to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Finance.generate_news_prompt import generate_prompt

class TestGenerateNewsPrompt(unittest.TestCase):
    def setUp(self):
        self.template = """
        > 📥【輸入參數】
        >
        > * 查詢關鍵字：`{公司 / 產業 / 國家 / 商品 / 主題}`
        > * 時間範圍：`{過去 24 小時 / 7 天 / 30 天}`
        > * 地區（可選）：`{全球 / 美國 / 歐洲 / 亞洲}`
        > * 關注面向：`{宏觀經濟 / 公司財報 / 政策 / 市場波動 / 風險事件}`
        """

    def test_replacements(self):
        keyword = "Tesla"
        time_range = "過去 30 天"
        region = "全球"
        focus = "市場波動"

        result = generate_prompt(self.template, keyword, time_range, region, focus)

        self.assertIn(f"查詢關鍵字：`{keyword}`", result)
        self.assertIn(f"時間範圍：`{time_range}`", result)
        self.assertIn(f"地區（可選）：`{region}`", result)
        self.assertIn(f"關注面向：`{focus}`", result)

    def test_placeholders_removed(self):
        keyword = "Gold"
        time_range = "過去 24 小時"
        region = "亞洲"
        focus = "風險事件"

        result = generate_prompt(self.template, keyword, time_range, region, focus)

        self.assertNotIn("{公司 / 產業 / 國家 / 商品 / 主題}", result)
        self.assertNotIn("{過去 24 小時 / 7 天 / 30 天}", result)
        self.assertNotIn("{全球 / 美國 / 歐洲 / 亞洲}", result)
        self.assertNotIn("{宏觀經濟 / 公司財報 / 政策 / 市場波動 / 風險事件}", result)

    def test_file_integration(self):
        """Test that the actual template file can be read and processed."""
        template_path = os.path.join(os.path.dirname(__file__), 'financial_news_prompt.md')
        self.assertTrue(os.path.exists(template_path), "Template file does not exist")

        from Finance.generate_news_prompt import load_template
        template = load_template(template_path)
        self.assertIn("Google 財經新聞分析 Prompt", template)

        result = generate_prompt(template, "Test", "24h", "Global", "Macro")
        self.assertIn("查詢關鍵字：`Test`", result)

if __name__ == '__main__':
    unittest.main()
