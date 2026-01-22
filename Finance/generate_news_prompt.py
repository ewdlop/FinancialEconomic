import os
import argparse
import sys

def generate_prompt(keyword, time_range, region, focus):
    # relative path to the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(script_dir, 'financial_news_prompt.md')

    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template file 'financial_news_prompt.md' not found in {script_dir}.")

    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace placeholders
    content = content.replace('{公司 / 產業 / 國家 / 商品 / 主題}', keyword)
    content = content.replace('{過去 24 小時 / 7 天 / 30 天}', time_range)
    content = content.replace('{全球 / 美國 / 歐洲 / 亞洲}', region)
    content = content.replace('{宏觀經濟 / 公司財報 / 政策 / 市場波動 / 風險事件}', focus)

    return content

def main():
    parser = argparse.ArgumentParser(description='Generate Financial News Prompt')
    parser.add_argument('--keyword', required=True, help='Search keyword')
    parser.add_argument('--time_range', required=True, help='Time range (e.g., 過去 24 小時)')
    parser.add_argument('--region', default='全球', help='Region (default: 全球)')
    parser.add_argument('--focus', required=True, help='Focus area')

    args = parser.parse_args()

    try:
        prompt = generate_prompt(args.keyword, args.time_range, args.region, args.focus)
        print(prompt)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
