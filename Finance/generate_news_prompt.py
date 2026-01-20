import argparse
import os

def load_template(filepath):
    """Reads the content of the template file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Template file not found: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def generate_prompt(template, keyword, time_range, region, focus):
    """Replaces placeholders in the template with provided values."""
    prompt = template
    prompt = prompt.replace("{公司 / 產業 / 國家 / 商品 / 主題}", keyword)
    prompt = prompt.replace("{過去 24 小時 / 7 天 / 30 天}", time_range)

    # Region is optional in the prompt text: "* 地區（可選）：{全球 / 美國 / 歐洲 / 亞洲}"
    # If region is provided, replace the placeholder.
    # If not provided, we might want to default to something or leave it as is?
    # But usually automation implies filling it in.
    # If the user passes None or empty string, we might default to "全球" (Global)
    # or if the user wants to leave it blank?
    # Let's assume the user provides a value or we default to "全球".
    if region:
        prompt = prompt.replace("{全球 / 美國 / 歐洲 / 亞洲}", region)
    else:
        prompt = prompt.replace("{全球 / 美國 / 歐洲 / 亞洲}", "全球")

    prompt = prompt.replace("{宏觀經濟 / 公司財報 / 政策 / 市場波動 / 風險事件}", focus)

    return prompt

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    default_template_path = os.path.join(script_dir, "financial_news_prompt.md")

    parser = argparse.ArgumentParser(description="Generate Financial News Analysis Prompt")
    parser.add_argument("keyword", help="查詢關鍵字 (e.g., TSLA, 半導體)")
    parser.add_argument("time_range", help="時間範圍 (e.g., 過去 24 小時)")
    parser.add_argument("--region", help="地區 (e.g., 美國)", default="全球")
    parser.add_argument("focus", help="關注面向 (e.g., 公司財報)")
    parser.add_argument("--template_path", help="Path to the template file", default=default_template_path)

    args = parser.parse_args()

    try:
        template = load_template(args.template_path)
        final_prompt = generate_prompt(template, args.keyword, args.time_range, args.region, args.focus)
        print(final_prompt)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
