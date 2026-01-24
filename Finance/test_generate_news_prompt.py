import unittest
from generate_news_prompt import generate_prompt, PROMPT_TEMPLATE

class TestGenerateNewsPrompt(unittest.TestCase):
    def test_generate_prompt_basic(self):
        keyword = "Apple"
        time_range = "7 天"
        region = "全球"
        focus = "宏觀經濟"

        prompt = generate_prompt(keyword, time_range, region, focus)

        self.assertIn("查詢關鍵字：Apple", prompt)
        self.assertIn("時間範圍：7 天", prompt)
        self.assertIn("地區（可選）：全球", prompt)
        self.assertIn("關注面向：宏觀經濟", prompt)

    def test_generate_prompt_custom(self):
        keyword = "Tesla"
        time_range = "過去 24 小時"
        region = "美國"
        focus = "市場波動"

        prompt = generate_prompt(keyword, time_range, region, focus)

        self.assertIn("查詢關鍵字：Tesla", prompt)
        self.assertIn("時間範圍：過去 24 小時", prompt)
        self.assertIn("地區（可選）：美國", prompt)
        self.assertIn("關注面向：市場波動", prompt)

    def test_prompt_integrity(self):
        # Verify that the template itself is roughly what we expect
        self.assertIn("Google 財經新聞（Google Financial News）Prompt", PROMPT_TEMPLATE)
        self.assertIn("{keyword}", PROMPT_TEMPLATE)

if __name__ == '__main__':
    unittest.main()
