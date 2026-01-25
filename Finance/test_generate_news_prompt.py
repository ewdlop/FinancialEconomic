import unittest
import sys
import os

# Add the parent directory to sys.path to import the module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Finance.generate_news_prompt import generate_prompt, PROMPT_TEMPLATE

class TestGenerateNewsPrompt(unittest.TestCase):

    def test_default_arguments(self):
        keyword = "Apple"
        expected_output = PROMPT_TEMPLATE.format(
            keyword=keyword,
            time_range="7 天",
            region="全球",
            focus="宏觀經濟"
        )
        self.assertEqual(generate_prompt(keyword), expected_output)

    def test_custom_arguments(self):
        keyword = "Bitcoin"
        time_range = "過去 24 小時"
        region = "亞洲"
        focus = "市場波動"

        expected_output = PROMPT_TEMPLATE.format(
            keyword=keyword,
            time_range=time_range,
            region=region,
            focus=focus
        )

        result = generate_prompt(keyword, time_range, region, focus)
        self.assertEqual(result, expected_output)

    def test_content_presence(self):
        keyword = "Tesla"
        result = generate_prompt(keyword)

        self.assertIn(f"* 查詢關鍵字：`{keyword}`", result)
        self.assertIn("* 時間範圍：`7 天`", result)
        self.assertIn("* 地區（可選）：`全球`", result)
        self.assertIn("* 關注面向：`宏觀經濟`", result)

if __name__ == '__main__':
    unittest.main()
