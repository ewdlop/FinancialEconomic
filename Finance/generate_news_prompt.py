import argparse
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Generate a customized Google Financial News Analysis Prompt.")
    parser.add_argument("--keyword", required=True, help="Query keyword (Company / Industry / Country / Commodity / Topic)")
    parser.add_argument("--time_range", default="過去 24 小時", help="Time range (e.g., '過去 24 小時', '7 天', '30 天')")
    parser.add_argument("--region", default="全球", help="Region (e.g., '全球', '美國', '歐洲', '亞洲')")
    parser.add_argument("--focus", default="宏觀經濟", help="Focus area (e.g., '宏觀經濟', '公司財報', '政策', '市場波動', '風險事件')")

    args = parser.parse_args()

    # Determine the path to the prompt file
    script_dir = Path(__file__).parent
    prompt_file = script_dir / "financial_news_prompt.md"

    if not prompt_file.exists():
        print(f"Error: Prompt file not found at {prompt_file}")
        sys.exit(1)

    with open(prompt_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Perform replacements
    content = content.replace("{公司 / 產業 / 國家 / 商品 / 主題}", args.keyword)
    content = content.replace("{過去 24 小時 / 7 天 / 30 天}", args.time_range)
    content = content.replace("{全球 / 美國 / 歐洲 / 亞洲}", args.region)
    content = content.replace("{宏觀經濟 / 公司財報 / 政策 / 市場波動 / 風險事件}", args.focus)

    print(content)

if __name__ == "__main__":
    main()
