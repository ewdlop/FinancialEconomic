import unittest
import sys
import os
import subprocess

# Add the directory containing the module to the Python path
# Assuming this test file is in Finance/ and we want to import from Finance/
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Finance.generate_news_prompt import generate_prompt

class TestGenerateNewsPrompt(unittest.TestCase):
    def test_generate_prompt_function(self):
        prompt = generate_prompt("NVDA", "30 天", "全球", "市場波動")
        self.assertIn("查詢關鍵字：`NVDA`", prompt)
        self.assertIn("時間範圍：`30 天`", prompt)
        self.assertIn("地區（可選）：`全球`", prompt)
        self.assertIn("關注面向：`市場波動`", prompt)
        self.assertIn("角色設定（Role）", prompt)

    def test_cli_execution(self):
        # Test running the script via subprocess
        result = subprocess.run(
            [sys.executable, "Finance/generate_news_prompt.py", "Google", "--time_range", "24 Hours"],
            capture_output=True,
            text=True
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("查詢關鍵字：`Google`", result.stdout)
        self.assertIn("時間範圍：`24 Hours`", result.stdout)
        # Check defaults
        self.assertIn("地區（可選）：`全球`", result.stdout)
        self.assertIn("關注面向：`宏觀經濟`", result.stdout)

if __name__ == "__main__":
    unittest.main()
