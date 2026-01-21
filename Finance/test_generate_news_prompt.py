import unittest
import os
import sys

# Add the directory containing the script to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from generate_news_prompt import generate_prompt, load_template

class TestGenerateNewsPrompt(unittest.TestCase):
    def setUp(self):
        self.template = """
> * 查詢關鍵字：`{公司 / 產業 / 國家 / 商品 / 主題}`
> * 時間範圍：`{過去 24 小時 / 7 天 / 30 天}`
> * 地區（可選）：`{全球 / 美國 / 歐洲 / 亞洲}`
> * 關注面向：`{宏觀經濟 / 公司財報 / 政策 / 市場波動 / 風險事件}`
"""

    def test_generate_prompt_replacements(self):
        keyword = "Apple"
        time_range = "30 天"
        region = "全球"
        focus = "宏觀經濟"

        expected = """
> * 查詢關鍵字：`Apple`
> * 時間範圍：`30 天`
> * 地區（可選）：`全球`
> * 關注面向：`宏觀經濟`
"""
        result = generate_prompt(self.template, keyword, time_range, region, focus)
        self.assertEqual(result.strip(), expected.strip())

    def test_generate_prompt_defaults(self):
        # This function generates prompt, it doesn't handle defaults (argparse does that).
        # So we just test if it replaces whatever we pass.
        keyword = "Oil"
        time_range = "Any"
        region = "Nowhere"
        focus = "None"

        result = generate_prompt(self.template, keyword, time_range, region, focus)
        self.assertIn("Oil", result)
        self.assertIn("Any", result)
        self.assertIn("Nowhere", result)
        self.assertIn("None", result)

    def test_load_template(self):
        # We can test loading the actual file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        template_path = os.path.join(script_dir, "financial_news_prompt.md")
        content = load_template(template_path)
        self.assertIn("Google 財經新聞", content)

if __name__ == '__main__':
    unittest.main()
