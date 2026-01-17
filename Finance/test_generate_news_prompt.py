import unittest
import os
import sys
from io import StringIO
from generate_news_prompt import generate_prompt, load_template

# Add the directory containing the script to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__)))

class TestGenerateNewsPrompt(unittest.TestCase):

    def setUp(self):
        self.template_content = """
> 📥【輸入參數】
>
> * 查詢關鍵字：`{公司 / 產業 / 國家 / 商品 / 主題}`
> * 時間範圍：`{過去 24 小時 / 7 天 / 30 天}`
> * 地區（可選）：`{全球 / 美國 / 歐洲 / 亞洲}`
> * 關注面向：`{宏觀經濟 / 公司財報 / 政策 / 市場波動 / 風險事件}`
"""
        self.test_template_path = "test_template.md"
        with open(self.test_template_path, "w", encoding="utf-8") as f:
            f.write(self.template_content)

    def tearDown(self):
        if os.path.exists(self.test_template_path):
            os.remove(self.test_template_path)

    def test_load_template(self):
        content = load_template(self.test_template_path)
        self.assertEqual(content, self.template_content)

    def test_load_template_not_found(self):
        with self.assertRaises(FileNotFoundError):
            load_template("non_existent_file.md")

    def test_generate_prompt_replacement(self):
        keyword = "Apple"
        time_range = "30 天"
        region = "亞洲"
        focus = "風險事件"

        expected_output = """
> 📥【輸入參數】
>
> * 查詢關鍵字：`Apple`
> * 時間範圍：`30 天`
> * 地區（可選）：`亞洲`
> * 關注面向：`風險事件`
"""
        generated_prompt = generate_prompt(self.template_content, keyword, time_range, region, focus)
        self.assertEqual(generated_prompt.strip(), expected_output.strip())

    def test_generate_prompt_partial_defaults(self):
        # Even if we pass empty strings or defaults, it should just replace literally
        keyword = "Gold"
        time_range = "default_time"
        region = "default_region"
        focus = "default_focus"

        expected_output = """
> 📥【輸入參數】
>
> * 查詢關鍵字：`Gold`
> * 時間範圍：`default_time`
> * 地區（可選）：`default_region`
> * 關注面向：`default_focus`
"""
        generated_prompt = generate_prompt(self.template_content, keyword, time_range, region, focus)
        self.assertEqual(generated_prompt.strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()
