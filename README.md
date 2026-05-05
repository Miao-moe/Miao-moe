name: Daily Update

on:
  schedule:
    - cron: "0 0 * * *"  # 每天 UTC 0 点更新（北京时间 8 点）
  workflow_dispatch:      # 支持手动触发

jobs:
  update-all:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Generate Random Params
        id: random
        run: |
          RAND_MOE=$(date +%s%N | md5sum | head -c 8)
          RAND_FOX=$(date +%s%N | md5sum | head -c 8 | tail -c 4)
          echo "rand_moe=$RAND_MOE" >> $GITHUB_OUTPUT
          echo "rand_fox=$RAND_FOX" >> $GITHUB_OUTPUT

      - name: Update Moe Image
        run: |
          README=$(cat README.md)
          
          NEW_MOE="<!-- MOE_IMG_START -->
<p align=\"center\">
  <img src=\"https://t.alcy.cc/moez?r=${{ steps.random.outputs.rand_moe }}\" width=\"400\" alt=\"萌图\" />
</p>
<!-- MOE_IMG_END -->"
          
          echo "$README" | sed -n '1,/<!-- MOE_IMG_START -->/p' > temp.md
          echo "$NEW_MOE" >> temp.md
          echo "$README" | sed -n '/<!-- MOE_IMG_END -->/,$p' | tail -n +2 >> temp.md
          
          mv temp.md README.md

      - name: Update Fox Image
        run: |
          README=$(cat README.md)
          
          NEW_FOX="<!-- FOX_IMG_START -->
<p align=\"center\">
  <img src=\"https://t.alcy.cc/xhl?r=${{ steps.random.outputs.rand_fox }}\" width=\"400\" alt=\"小狐狸\" />
</p>
<!-- FOX_IMG_END -->"
          
          echo "$README" | sed -n '1,/<!-- FOX_IMG_START -->/p' > temp.md
          echo "$NEW_FOX" >> temp.md
          echo "$README" | sed -n '/<!-- FOX_IMG_END -->/,$p' | tail -n +2 >> temp.md
          
          mv temp.md README.md

      - name: Fetch Daily Quote
        id: quote
        run: |
          RESPONSE=$(curl -s "https://v1.hitokoto.cn/?c=d&encode=json")
          QUOTE_CN=$(echo $RESPONSE | jq -r '.hitokoto')
          FROM=$(echo $RESPONSE | jq -r '.from')
          
          if [ "$QUOTE_CN" = "null" ] || [ -z "$QUOTE_CN" ]; then
            echo "quote_cn=喵喵喵好像出错了 ~nya" >> $GITHUB_OUTPUT
            echo "quote_en=Meow something went wrong ~nya" >> $GITHUB_OUTPUT
            echo "from=云汀" >> $GITHUB_OUTPUT
            exit 0
          fi
          
          if [ "$FROM" = "null" ] || [ -z "$FROM" ]; then
            FROM="Unknown"
          fi
          
          QUOTE_ENCODED=$(echo "$QUOTE_CN" | jq -sRr @uri)
          TRANS_RESPONSE=$(curl -s "https://api.mymemory.translated.net/get?q=${QUOTE_ENCODED}&langpair=zh-CN|en")
          QUOTE_EN=$(echo $TRANS_RESPONSE | jq -r '.responseData.translatedText')
          
          if [ "$QUOTE_EN" = "null" ] || [ -z "$QUOTE_EN" ] || [ "$QUOTE_EN" = "" ]; then
            QUOTE_EN="Meow something went wrong ~nya"
          fi
          
          echo "quote_cn=$QUOTE_CN" >> $GITHUB_OUTPUT
          echo "quote_en=$QUOTE_EN" >> $GITHUB_OUTPUT
          echo "from=$FROM" >> $GITHUB_OUTPUT

      - name: Update Daily Quote
        run: |
          README=$(cat README.md)
          
          url_encode() {
            echo "$1" | sed 's/ /+/g' | sed 's/"/%22/g' | sed 's/#/%23/g' | sed 's/&/%26/g' | sed 's/?/%3F/g'
          }
          
          QUOTE_CN_ENCODED=$(url_encode "${{ steps.quote.outputs.quote_cn }}")
          QUOTE_EN_ENCODED=$(url_encode "${{ steps.quote.outputs.quote_en }}")
          
          NEW_QUOTE="<!-- DAILY_QUOTE_START -->
<p align=\"center\">
  <img src=\"https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=3000&color=FF69B4&center=true&vCenter=true&width=700&lines=${QUOTE_CN_ENCODED};${QUOTE_EN_ENCODED}\" alt=\"Daily Quote\" />
</p>

<p align=\"center\"><b>🎯 中文：</b>${{ steps.quote.outputs.quote_cn }}</p>
<p align=\"center\"><b>🎯 English：</b>${{ steps.quote.outputs.quote_en }}</p>
<p align=\"center\"><sub>— ${{ steps.quote.outputs.from }}</sub></p>
<!-- DAILY_QUOTE_END -->"
          
          echo "$README" | sed -n '1,/<!-- DAILY_QUOTE_START -->/p' > temp.md
          echo "$NEW_QUOTE" >> temp.md
          echo "$README" | sed -n '/<!-- DAILY_QUOTE_END -->/,$p' | tail -n +2 >> temp.md
          
          mv temp.md README.md

      - name: Commit and Push
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add README.md
          git diff --cached --quiet || (git commit -m "🔄 Daily update: $(date +%Y-%m-%d)" && git push)
  <img src="https://img.shields.io/badge/Python-30%25-FFB6C1?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-18%25-FFC0CB?style=for-the-badge&logo=javascript&logoColor=black" />
  <img src="https://img.shields.io/badge/Tailwind_CSS-100%25-FF69B4?style=for-the-badge&logo=tailwindcss&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub-100%25-FF1493?style=for-the-badge&logo=github&logoColor=white" />
</p>

---

## 🌸 萌图 | Cute Pics

<p align="center">
  <img src="https://t.alcy.cc/moez" width="400" alt="萌图" />
</p>

<p align="center"><b>喵喵喵 ~ 好萌啊！| Meow ~ So cute!</b></p>
<p align="center"><sub>✨ 来源于 <a href="https://t.alcy.cc">举个栗子 API</a> ✨</sub></p>

---

## 🦊 小狐狸 | Little Fox

<p align="center">
  <img src="https://t.alcy.cc/xhl" width="400" alt="小狐狸" />
</p>

<p align="center"><b>嘤嘤嘤 ~ 狐狸好软！| Yip yip ~ So fluffy!</b></p>
<p align="center"><sub>✨ 来源于 <a href="https://t.alcy.cc">举个栗子 API</a> ✨</sub></p>

---

## 💬 每日一言 | Daily Quote

<!-- DAILY_QUOTE_START -->
<p align="center">✨ 每日一言加载中... | Daily quote loading... ✨</p>
<!-- DAILY_QUOTE_END -->

<p align="center"><sub>✨ 来源于 <a href="https://hitokoto.cn">一言 API</a> ✨</sub></p>

---

## 🐱 贡献图 | Contribution

<p align="center">
  <img src="https://ghchart.rshah.org/ff69b4/miao-moe" alt="GitHub Contribution Chart" />
</p>

---

## 👀 访客统计 | Visitors

<p align="center">
  <img src="https://count.getloli.com/get/@miao-moe?theme=rule34" alt="Visitors" />
</p>

---

## 💌 联系我 | Contact Me

<p align="center">
  <a href="https://github.com/MistAperio"><img src="https://img.shields.io/badge/GitHub-MistAperio-FF69B4?style=for-the-badge&logo=github&logoColor=white" /></a>
  <a href="mailto:536164245@qq.com"><img src="https://img.shields.io/badge/Email-536164245@qq.com-FFB6C1?style=for-the-badge&logo=gmail&logoColor=white" /></a>
</p>

<p align="center">
  <b>QQ：</b>536164245 | <b>微信 | WeChat：</b>ycswjgq
</p>

---

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=miao-moe&color=ff69b4&style=flat-square" alt="Profile views" />
</p>

<p align="center">
  <sub>🐾 喵喵喵 ~ | Meow ~ 🐾</sub>
</p>
