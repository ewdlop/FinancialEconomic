import argparse
import os

def load_template(filepath):
    """Loads the prompt template from the given file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Template file not found: {filepath}")

    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def generate_prompt(template, keyword, time_range, region, focus):
    """Replaces placeholders in the template with provided values."""

    # Define the placeholders as they appear in the markdown file
    placeholders = {
        '{公司 / 產業 / 國家 / 商品 / 主題}': keyword,
        '{過去 24 小時 / 7 天 / 30 天}': time_range,
        '{全球 / 美國 / 歐洲 / 亞洲}': region,
        '{宏觀經濟 / 公司財報 / 政策 / 市場波動 / 風險事件}': focus
    }

    prompt = template
    for placeholder, value in placeholders.items():
        if value:
             prompt = prompt.replace(placeholder, value)
        else:
            # specific handling if value is None/Empty?
            # For now, let's assume we want to keep the placeholder or replace with "Unspecified"
            # Based on the user request, it seems they are parameters.
            # If region is optional (as per prompt text "地區（可選）"), maybe we can leave it or replace with "Global" default?
            # But let's just replace with the provided value or keep placeholder if not provided?
            # The prompt structure implies these are input parameters.
            # Let's replace with "N/A" or similar if not provided, but argparse will handle required ones.
            pass

    return prompt

def main():
    parser = argparse.ArgumentParser(description='Generate Financial News Analysis Prompt')
    parser.add_argument('--keyword', required=True, help='Query keyword (Company/Industry/Country/Product/Topic)')
    parser.add_argument('--time', required=True, help='Time range (e.g., "Last 24 hours", "7 days")')
    parser.add_argument('--region', default='全球', help='Region (Optional, default: Global/全球)')
    parser.add_argument('--focus', required=True, help='Focus area (Macroeconomy, Earnings, Policy, etc.)')

    args = parser.parse_args()

    # Path to the template file relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(script_dir, 'financial_news_prompt.md')

    try:
        template = load_template(template_path)
        prompt = generate_prompt(template, args.keyword, args.time, args.region, args.focus)
        print(prompt)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
