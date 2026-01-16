import argparse
import os

def load_template(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Template file not found at {filepath}")
        return None

def fill_template(template, keyword, time_range, region, focus):
    # Replace placeholders
    # The placeholders in the markdown are descriptive, not standard python format keys.
    # We will replace the entire line or the specific pattern based on the text structure.

    # Placeholder patterns from the file:
    # * 查詢關鍵字：`{公司 / 產業 / 國家 / 商品 / 主題}`
    # * 時間範圍：`{過去 24 小時 / 7 天 / 30 天}`
    # * 地區（可選）：`{全球 / 美國 / 歐洲 / 亞洲}`
    # * 關注面向：`{宏觀經濟 / 公司財報 / 政策 / 市場波動 / 風險事件}`

    filled_template = template

    # We use simple string replacement for the specific placeholder patterns found in the file
    filled_template = filled_template.replace("{公司 / 產業 / 國家 / 商品 / 主題}", keyword)
    filled_template = filled_template.replace("{過去 24 小時 / 7 天 / 30 天}", time_range)

    # Region is optional in the prompt description, but we can default or fill it.
    if region:
        filled_template = filled_template.replace("{全球 / 美國 / 歐洲 / 亞洲}", region)
    else:
        # If not provided, maybe keep it generic or remove the placeholder?
        # Let's keep the placeholder or replace with "Global" as a default if desired,
        # but for now let's assume the user might provide it.
        # If not provided, let's replace with "不限" or just leave it?
        # The prompt says "地區（可選）", so replacing with a default like "全球" seems safe if not specified.
        filled_template = filled_template.replace("{全球 / 美國 / 歐洲 / 亞洲}", "全球")

    filled_template = filled_template.replace("{宏觀經濟 / 公司財報 / 政策 / 市場波動 / 風險事件}", focus)

    return filled_template

def main():
    parser = argparse.ArgumentParser(description="Generate Financial News Prompt")
    parser.add_argument("keyword", help="Search keyword (Company/Industry/Country/etc)")
    parser.add_argument("--time_range", default="過去 24 小時", help="Time range (default: 過去 24 小時)")
    parser.add_argument("--region", default="全球", help="Region (default: 全球)")
    parser.add_argument("--focus", default="宏觀經濟", help="Focus area (default: 宏觀經濟)")
    parser.add_argument("--template_path", default="financial_news_prompt.md", help="Path to the template file")

    args = parser.parse_args()

    # Resolve template path relative to script location if not absolute
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(script_dir, args.template_path)

    template = load_template(template_path)
    if template:
        prompt = fill_template(template, args.keyword, args.time_range, args.region, args.focus)
        print(prompt)

if __name__ == "__main__":
    main()
