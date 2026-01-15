import argparse
import os
import sys

def load_template(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    parser = argparse.ArgumentParser(description="Generate Financial News Prompt")
    parser.add_argument("--keyword", required=True, help="Query keyword (Company, Industry, Country, etc.)")
    parser.add_argument("--time_range", required=True, help="Time range (e.g., '過去 24 小時', '7 天', '30 天')")
    parser.add_argument("--region", help="Region (e.g., '全球', '美國', '歐洲', '亞洲')")
    parser.add_argument("--focus", required=True, help="Focus area (e.g., '宏觀經濟', '公司財報', '政策', '市場波動', '風險事件')")

    args = parser.parse_args()

    template_path = os.path.join(os.path.dirname(__file__), 'financial_news_prompt.md')
    if not os.path.exists(template_path):
        print(f"Error: Template file not found at {template_path}")
        sys.exit(1)

    content = load_template(template_path)

    # Replace placeholders
    content = content.replace("{公司 / 產業 / 國家 / 商品 / 主題}", args.keyword)
    content = content.replace("{過去 24 小時 / 7 天 / 30 天}", args.time_range)

    if args.region:
        content = content.replace("{全球 / 美國 / 歐洲 / 亞洲}", args.region)
    else:
        # Default to Global if not specified, or just remove the placeholder text
        content = content.replace("{全球 / 美國 / 歐洲 / 亞洲}", "全球")

    content = content.replace("{宏觀經濟 / 公司財報 / 政策 / 市場波動 / 風險事件}", args.focus)

    print(content)

if __name__ == "__main__":
    main()
