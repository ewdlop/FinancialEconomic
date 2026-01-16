import unittest
import sys
import os

# Add the directory containing the script to the path so we can import it
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from generate_news_prompt import fill_template

class TestGenerateNewsPrompt(unittest.TestCase):

    def test_fill_template(self):
        # Define a mock template with the known placeholders
        mock_template = """
        Key: `{公司 / 產業 / 國家 / 商品 / 主題}`
        Time: `{過去 24 小時 / 7 天 / 30 天}`
        Region: `{全球 / 美國 / 歐洲 / 亞洲}`
        Focus: `{宏觀經濟 / 公司財報 / 政策 / 市場波動 / 風險事件}`
        """

        keyword = "Apple"
        time_range = "過去 30 天"
        region = "美國"
        focus = "公司財報"

        expected_output = """
        Key: `Apple`
        Time: `過去 30 天`
        Region: `美國`
        Focus: `公司財報`
        """

        result = fill_template(mock_template, keyword, time_range, region, focus)

        # Normalize whitespace for comparison to avoid indentation issues
        self.assertEqual(result.strip(), expected_output.strip())

    def test_fill_template_default_region(self):
        # Test that region defaults to "全球" if provided as None (logic in script)
        # Note: In the script, if region arg is passed as None, it defaults to "全球".
        # But here we are testing the function. Let's see how I implemented it.
        # "if region: replace... else: replace with '全球'"

        mock_template = "Region: `{全球 / 美國 / 歐洲 / 亞洲}`"
        result = fill_template(mock_template, "K", "T", None, "F")
        self.assertEqual(result, "Region: `全球`")

if __name__ == '__main__':
    unittest.main()
