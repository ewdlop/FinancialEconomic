import argparse
import os

def load_template(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def generate_prompt(template, keyword, time_range, region, focus):
    prompt = template
    prompt = prompt.replace('{公司 / 產業 / 國家 / 商品 / 主題}', keyword)
    prompt = prompt.replace('{過去 24 小時 / 7 天 / 30 天}', time_range)
    prompt = prompt.replace('{全球 / 美國 / 歐洲 / 亞洲}', region)
    prompt = prompt.replace('{宏觀經濟 / 公司財報 / 政策 / 市場波動 / 風險事件}', focus)
    return prompt

def main():
    parser = argparse.ArgumentParser(description='Generate Google Financial News Analysis Prompt')
    parser.add_argument('keyword', help='Query keyword (Company, Industry, Country, etc.)')
    parser.add_argument('--time_range', default='過去 24 小時', help='Time range (default: 過去 24 小時)')
    parser.add_argument('--region', default='全球', help='Region (default: 全球)')
    parser.add_argument('--focus', default='宏觀經濟', help='Focus area (default: 宏觀經濟)')
    parser.add_argument('--template_path', default=os.path.join(os.path.dirname(__file__), 'financial_news_prompt.md'), help='Path to the template file')

    args = parser.parse_args()

    try:
        template = load_template(args.template_path)
        prompt = generate_prompt(template, args.keyword, args.time_range, args.region, args.focus)
        print(prompt)
    except FileNotFoundError:
        print(f"Error: Template file not found at {args.template_path}")
        exit(1)

if __name__ == '__main__':
    main()
