import argparse
import os

def load_template(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Template file not found: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def generate_prompt(template, keyword, time_range, region, focus):
    prompt = template
    prompt = prompt.replace("{公司 / 產業 / 國家 / 商品 / 主題}", keyword)
    prompt = prompt.replace("{過去 24 小時 / 7 天 / 30 天}", time_range)
    prompt = prompt.replace("{全球 / 美國 / 歐洲 / 亞洲}", region)
    prompt = prompt.replace("{宏觀經濟 / 公司財報 / 政策 / 市場波動 / 風險事件}", focus)
    return prompt

def main():
    parser = argparse.ArgumentParser(description="Generate a Google Financial News Analysis Prompt")
    parser.add_argument("--keyword", required=True, help="Query keyword (Company, Industry, Country, etc.)")
    parser.add_argument("--time_range", default="過去 24 小時", help="Time range (e.g., 過去 24 小時, 7 天, 30 天)")
    parser.add_argument("--region", default="全球", help="Region (e.g., 全球, 美國, 歐洲, 亞洲)")
    parser.add_argument("--focus", default="宏觀經濟", help="Focus area (e.g., 宏觀經濟, 公司財報, 政策, 市場波動, 風險事件)")
    parser.add_argument("--template_path", default="Finance/financial_news_prompt.md", help="Path to the prompt template")

    args = parser.parse_args()

    try:
        template = load_template(args.template_path)
        final_prompt = generate_prompt(template, args.keyword, args.time_range, args.region, args.focus)
        print(final_prompt)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
