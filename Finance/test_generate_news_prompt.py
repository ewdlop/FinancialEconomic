import unittest
import sys
import os

# Ensure we can import the module from the same directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import generate_news_prompt

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

    def test_replacement(self):
        keyword = "Apple"
        time_range = "過去 24 小時"
        region = "美國"
        focus = "市場波動"

        expected = """
> 📥【輸入參數】
>
> * 查詢關鍵字：`Apple`
> * 時間範圍：`過去 24 小時`
> * 地區（可選）：`美國`
> * 關注面向：`市場波動`
"""
        result = generate_news_prompt.generate_prompt(self.template, keyword, time_range, region, focus)
        self.assertEqual(result.strip(), expected.strip())

    def test_default_region_logic(self):
        # Even though the script sets default in main(), the function handles what is passed.
        # This test ensures if we pass a region, it is used.
        keyword = "Oil"
        time_range = "過去 30 天"
        region = "全球"
        focus = "宏觀經濟"

        expected = """
> 📥【輸入參數】
>
> * 查詢關鍵字：`Oil`
> * 時間範圍：`過去 30 天`
> * 地區（可選）：`全球`
> * 關注面向：`宏觀經濟`
"""
        result = generate_news_prompt.generate_prompt(self.template, keyword, time_range, region, focus)
        self.assertEqual(result.strip(), expected.strip())

if __name__ == '__main__':
    unittest.main()
