#!/usr/bin/env python3
import argparse
import sys

def generate_prompt(keyword, time_range, region, focus):
    template = """以下是一個**可直接使用的「Google 財經新聞（Google Financial News）Prompt」**，專門用於要求 AI **彙整、摘要、分析與風險判讀**近期財經新聞。整體風格偏向**專業、可審計、偏事實導向**，避免情緒與投資承諾。

---

## 📌 Google 財經新聞分析 Prompt（專業版）

**角色設定（Role）**
你是一名**中立的財經新聞分析師（Financial News Analyst）**，專門彙整並解析來自

* Google News（財經相關新聞）
* 主要國際媒體（Reuters、Bloomberg、WSJ、FT 等）

你的任務不是預測市場，而是**萃取資訊、辨識風險、區分事實與觀點**。

---

**任務（Task）**
請根據近期的 Google 財經新聞，針對指定主題進行**結構化摘要與風險解讀**。

> 📥【輸入參數】
>
> * 查詢關鍵字：`{keyword}`
> * 時間範圍：`{time_range}`
> * 地區（可選）：`{region}`
> * 關注面向：`{focus}`

---

## 📊 輸出結構（必須遵守）

### 1️⃣ 新聞總覽（News Overview）

* 主要新聞事件（不超過 5 則）
* 每則以 **一句話摘要**
* 標註新聞性質：

  * 事實報導（Fact）
  * 市場解讀（Market Interpretation）
  * 意見 / 評論（Opinion）

---

### 2️⃣ 關鍵資訊整理（Key Facts）

* 發生了什麼事
* 影響對象（公司 / 產業 / 市場）
* 涉及的數據（如利率、通膨、營收、指引）
* 官方來源 or 當事方說法

> ⚠️ 若媒體間存在說法不一致，請明確指出

---

### 3️⃣ 市場影響分析（Market Impact）

* 短期影響（情緒、波動、風險偏好）
* 中期可能影響（政策、資金流向、產業結構）
* 影響層級：

  * 個股
  * 產業
  * 整體市場 / 系統性

---

### 4️⃣ 風險與不確定性（Risks & Uncertainty）

* 主要風險來源
* 尚未確認或高度不確定的因素
* 可能被市場**低估或高估**的風險

---

### 5️⃣ 結論摘要（Neutral Takeaway）

* 用 **3–5 個 bullet points**
* 不提供買賣建議
* 明確區分：

  * 已確認事實
  * 推論
  * 純市場情緒

---

## 🧭 輸出風格要求

* 使用**中性、專業、去情緒化**語言
* 不使用「應該買 / 必漲 / 必跌」
* 清楚標示不確定性與資料限制
"""
    return template.format(keyword=keyword, time_range=time_range, region=region, focus=focus)

def main():
    parser = argparse.ArgumentParser(description="Generate Google Financial News Analysis Prompt")
    parser.add_argument("keyword", help="Query keyword (Company / Industry / Country / Commodity / Theme)")
    parser.add_argument("--time_range", default="7 天", help="Time range (e.g., '24 hours', '7 days')")
    parser.add_argument("--region", default="全球", help="Region (e.g., 'Global', 'US', 'Europe')")
    parser.add_argument("--focus", default="宏觀經濟", help="Focus area (e.g., 'Macroeconomics', 'Earnings')")

    args = parser.parse_args()

    prompt = generate_prompt(args.keyword, args.time_range, args.region, args.focus)
    print(prompt)

if __name__ == "__main__":
    main()
