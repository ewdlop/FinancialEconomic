import unittest
import os
import sys
from io import StringIO
from unittest.mock import patch

# Add the directory containing generate_news_prompt.py to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import generate_news_prompt

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
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.template_path = os.path.join(self.script_dir, 'financial_news_prompt.md')

    def test_generate_prompt_logic(self):
        """Test the string replacement logic."""
        keyword = "Apple"
        time_range = "Last 30 days"
        region = "USA"
        focus = "Product Launch"

        expected_output = """
> 📥【輸入參數】
>
> * 查詢關鍵字：`Apple`
> * 時間範圍：`Last 30 days`
> * 地區（可選）：`USA`
> * 關注面向：`Product Launch`
"""
        result = generate_news_prompt.generate_prompt(self.template_content, keyword, time_range, region, focus)
        self.assertEqual(result.strip(), expected_output.strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_integration_with_real_file(self, mock_stdout):
        """Test running the main function with arguments, reading the real file."""

        test_args = [
            'generate_news_prompt.py',
            '--keyword', 'Tesla',
            '--time', '過去 24 小時',
            '--region', '美國',
            '--focus', '風險事件'
        ]

        with patch.object(sys, 'argv', test_args):
            generate_news_prompt.main()

        output = mock_stdout.getvalue()

        # Check if the output contains the replaced values
        self.assertIn("查詢關鍵字：`Tesla`", output)
        self.assertIn("時間範圍：`過去 24 小時`", output)
        self.assertIn("地區（可選）：`美國`", output)
        self.assertIn("關注面向：`風險事件`", output)

        # Check if some static part of the prompt is also present
        self.assertIn("你是一名中立的財經新聞分析師", output.replace("**", "").replace(" ", ""))

    @patch('sys.stdout', new_callable=StringIO)
    def test_default_region(self, mock_stdout):
        """Test that region defaults to '全球' if not provided."""
        test_args = [
            'generate_news_prompt.py',
            '--keyword', 'Gold',
            '--time', '7 days',
            '--focus', 'Macro'
        ]

        with patch.object(sys, 'argv', test_args):
            generate_news_prompt.main()

        output = mock_stdout.getvalue()
        self.assertIn("地區（可選）：`全球`", output)

if __name__ == '__main__':
    unittest.main()
