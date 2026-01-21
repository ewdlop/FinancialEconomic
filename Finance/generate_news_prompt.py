import argparse
import os
import sys

def load_template(template_path):
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Template file not found at {template_path}")
        sys.exit(1)

def generate_prompt(template, keyword, time_range, region, focus):
    prompt = template.replace("{公司 / 產業 / 國家 / 商品 / 主題}", keyword)
    prompt = prompt.replace("{過去 24 小時 / 7 天 / 30 天}", time_range)
    prompt = prompt.replace("{全球 / 美國 / 歐洲 / 亞洲}", region)
    prompt = prompt.replace("{宏觀經濟 / 公司財報 / 政策 / 市場波動 / 風險事件}", focus)

    return prompt

def main():
    parser = argparse.ArgumentParser(description="Generate Financial News Analysis Prompt")
    parser.add_argument("keyword", help="Query keyword (Company/Industry/Country/Commodity/Topic)")
    parser.add_argument("--time_range", default="過去 24 小時", help="Time range (e.g., 過去 24 小時, 7 天, 30 天)")
    parser.add_argument("--region", default="全球", help="Region (Optional, e.g., 全球, 美國, 歐洲, 亞洲)")
    parser.add_argument("--focus", default="市場波動", help="Focus area (e.g., 宏觀經濟, 公司財報, 政策, 市場波動, 風險事件)")

    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(script_dir, "financial_news_prompt.md")

    template = load_template(template_path)
    prompt = generate_prompt(template, args.keyword, args.time_range, args.region, args.focus)

    print(prompt)

if __name__ == "__main__":
    main()
