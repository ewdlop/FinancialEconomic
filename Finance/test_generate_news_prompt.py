import subprocess
import os

def test_generate_news_prompt():
    script_path = os.path.join(os.path.dirname(__file__), 'generate_news_prompt.py')

    # Test case 1: All arguments provided
    cmd = [
        "python3", script_path,
        "--keyword", "Tesla",
        "--time_range", "7 days",
        "--region", "US",
        "--focus", "Earnings"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    assert result.returncode == 0
    assert "Tesla" in result.stdout
    assert "7 days" in result.stdout
    assert "US" in result.stdout
    assert "Earnings" in result.stdout

    # Test case 2: Optional region missing
    cmd = [
        "python3", script_path,
        "--keyword", "NVDA",
        "--time_range", "24h",
        "--focus", "Risk"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    assert result.returncode == 0
    assert "NVDA" in result.stdout
    assert "24h" in result.stdout
    assert "全球" in result.stdout # Default value
    assert "Risk" in result.stdout

if __name__ == "__main__":
    try:
        test_generate_news_prompt()
        print("All tests passed!")
    except AssertionError as e:
        print("Test failed!")
        raise e
