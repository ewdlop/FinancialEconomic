import unittest
import os
import sys

# Add the directory containing the module to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from generate_news_prompt import generate_prompt

class TestGenerateNewsPrompt(unittest.TestCase):
    def test_generate_prompt_basic(self):
        keyword = "TSMC"
        time_range = "过去 24 小时"
        focus = "市场波动"
        region = "亚洲"

        prompt = generate_prompt(keyword, time_range, focus, region)

        self.assertIsNotNone(prompt)
        self.assertIn(f"* 查詢關鍵字：`{keyword}`", prompt)
        self.assertIn(f"* 時間範圍：`{time_range}`", prompt)
        self.assertIn(f"* 地區（可選）：`{region}`", prompt)
        self.assertIn(f"* 關注面向：`{focus}`", prompt)

    def test_generate_prompt_default_region(self):
        keyword = "Apple"
        time_range = "7 天"
        focus = "公司财报"

        # region should default to '全球'
        prompt = generate_prompt(keyword, time_range, focus)

        self.assertIsNotNone(prompt)
        self.assertIn(f"* 查詢關鍵字：`{keyword}`", prompt)
        self.assertIn(f"* 時間範圍：`{time_range}`", prompt)
        self.assertIn(f"* 地區（可選）：`全球`", prompt)
        self.assertIn(f"* 關注面向：`{focus}`", prompt)

    def test_placeholders_removed(self):
        keyword = "Gold"
        time_range = "30 Days"
        focus = "Risk"

        prompt = generate_prompt(keyword, time_range, focus)

        # Ensure original placeholders are gone
        self.assertNotIn("{公司 / 產業 / 國家 / 商品 / 主題}", prompt)
        self.assertNotIn("{過去 24 小時 / 7 天 / 30 天}", prompt)
        self.assertNotIn("{全球 / 美國 / 歐洲 / 亞洲}", prompt)
        self.assertNotIn("{宏觀經濟 / 公司財報 / 政策 / 市場波動 / 風險事件}", prompt)

if __name__ == '__main__':
    unittest.main()
