import unittest
import sys
import os
import subprocess

# Add the project root to sys.path to allow imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Finance.generate_news_prompt import generate_prompt

class TestGenerateNewsPrompt(unittest.TestCase):
    def test_generate_prompt_substitution(self):
        keyword = "TSMC"
        time_range = "30 天"
        region = "亞洲"
        focus = "公司財報"

        prompt = generate_prompt(keyword, time_range, region, focus)

        self.assertIn(f"* 查詢關鍵字：`{keyword}`", prompt)
        self.assertIn(f"* 時間範圍：`{time_range}`", prompt)
        self.assertIn(f"* 地區（可選）：`{region}`", prompt)
        self.assertIn(f"* 關注面向：`{focus}`", prompt)

    def test_cli_invocation(self):
        # Test running the script as a subprocess
        script_path = os.path.join(os.path.dirname(__file__), 'generate_news_prompt.py')
        result = subprocess.run(
            [sys.executable, script_path, "Google", "--time_range", "24 小時"],
            capture_output=True,
            text=True
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("* 查詢關鍵字：`Google`", result.stdout)
        self.assertIn("* 時間範圍：`24 小時`", result.stdout)
        # Check defaults
        self.assertIn("* 地區（可選）：`全球`", result.stdout)
        self.assertIn("* 關注面向：`宏觀經濟`", result.stdout)

if __name__ == '__main__':
    unittest.main()
