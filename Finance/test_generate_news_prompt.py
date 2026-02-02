import unittest
import sys
import os

# Add the directory containing the module to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from generate_news_prompt import generate_prompt, PROMPT_TEMPLATE

class TestGenerateNewsPrompt(unittest.TestCase):
    def test_default_arguments(self):
        keyword = "Tesla"
        expected = PROMPT_TEMPLATE.format(
            keyword=keyword,
            time_range="7 天",
            region="全球",
            focus="宏觀經濟"
        )
        result = generate_prompt(keyword)
        self.assertEqual(result, expected)

    def test_custom_arguments(self):
        keyword = "Nvidia"
        time_range = "30 天"
        region = "美國"
        focus = "市場波動"

        expected = PROMPT_TEMPLATE.format(
            keyword=keyword,
            time_range=time_range,
            region=region,
            focus=focus
        )
        result = generate_prompt(keyword, time_range, region, focus)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
