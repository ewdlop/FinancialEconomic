import unittest
import sys
import os
import subprocess

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Finance import generate_news_prompt

class TestGenerateNewsPrompt(unittest.TestCase):
    def test_generate_prompt_content(self):
        prompt = generate_news_prompt.generate_prompt(
            keyword="Apple",
            time_range="30 天",
            region="美國",
            focus="公司財報"
        )
        self.assertIn("* 查詢關鍵字：`Apple`", prompt)
        self.assertIn("* 時間範圍：`30 天`", prompt)
        self.assertIn("* 地區（可選）：`美國`", prompt)
        self.assertIn("* 關注面向：`公司財報`", prompt)
        self.assertIn("## 📌 Google 財經新聞分析 Prompt（專業版）", prompt)

    def test_cli_execution(self):
        # Test running the script as a subprocess
        script_path = os.path.join(os.path.dirname(__file__), 'generate_news_prompt.py')
        result = subprocess.run(
            [sys.executable, script_path, "Tesla", "--time_range", "24 小時"],
            capture_output=True,
            text=True
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("* 查詢關鍵字：`Tesla`", result.stdout)
        self.assertIn("* 時間範圍：`24 小時`", result.stdout)
        # Default values
        self.assertIn("* 地區（可選）：`全球`", result.stdout)
        self.assertIn("* 關注面向：`宏觀經濟`", result.stdout)

if __name__ == '__main__':
    unittest.main()
