import unittest
import sys
import os
import subprocess

# Add parent directory to path to allow importing the script
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Finance.generate_news_prompt import generate_prompt, PROMPT_TEMPLATE

class TestGenerateNewsPrompt(unittest.TestCase):

    def test_generate_prompt_structure(self):
        """Test if the generated prompt contains the substituted values."""
        keyword = "Apple"
        time_range = "30 天"
        region = "美國"
        focus = "公司財報"

        prompt = generate_prompt(keyword, time_range, region, focus)

        self.assertIn(f"查詢關鍵字：`{keyword}`", prompt)
        self.assertIn(f"時間範圍：`{time_range}`", prompt)
        self.assertIn(f"地區（可選）：`{region}`", prompt)
        self.assertIn(f"關注面向：`{focus}`", prompt)
        self.assertIn("## 📌 Google 財經新聞分析 Prompt（專業版）", prompt)

    def test_cli_execution(self):
        """Test running the script via CLI."""
        script_path = os.path.join(os.path.dirname(__file__), "generate_news_prompt.py")

        # Test with required argument only
        result = subprocess.run(
            [sys.executable, script_path, "Tesla"],
            capture_output=True,
            text=True,
            check=True
        )
        self.assertIn("查詢關鍵字：`Tesla`", result.stdout)
        self.assertIn("時間範圍：`7 天`", result.stdout) # Default value
        self.assertIn("地區（可選）：`全球`", result.stdout) # Default value

        # Test with all arguments
        result = subprocess.run(
            [sys.executable, script_path, "NVIDIA", "--time_range", "24 小時", "--region", "亞洲", "--focus", "市場波動"],
            capture_output=True,
            text=True,
            check=True
        )
        self.assertIn("查詢關鍵字：`NVIDIA`", result.stdout)
        self.assertIn("時間範圍：`24 小時`", result.stdout)
        self.assertIn("地區（可選）：`亞洲`", result.stdout)
        self.assertIn("關注面向：`市場波動`", result.stdout)

if __name__ == "__main__":
    unittest.main()
