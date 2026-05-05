<!-- 顶部动态标题 -->
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=24&pause=1000&color=FF69B4&center=true&vCenter=true&width=520&lines=%F0%9F%90%BE+Hi%2C+I'm+%E4%BA%91%E6%B1%80+%7C+%E4%BD%A0%E5%A5%BD%EF%BC%8C%E6%88%91%E6%98%AF%E4%BA%91%E6%B1%80+%F0%9F%92%96;Full+Stack+Developer+%7C+%E5%85%A8%E6%A0%88%E5%BC%80%E5%8F%91%E8%80%85;Cute+Catgirl+%26+Shota+%7C+%E5%8F%AF%E7%88%B1%E7%8C%AB%E5%A8%98%E4%B8%8E%E6%AD%A3%E5%A4%AA;Open+Source+Lover+%7C+%E5%BC%80%E6%BA%90%E7%88%B1%E5%A5%BD%E8%80%85" alt="Typing SVG" />
</p>

---

## 🐾 关于我 | About Me

> 喵喵喵 ~ | Meow ~

---

## 🛠️ 技术栈 | Tech Stack

<p align="center">
  <img src="https://img.shields.io/badge/Node.js-52%25-FF69B4?style=for-the-badge&logo=nodedotjs&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-30%25-FFB6C1?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-18%25-FFC0CB?style=for-the-badge&logo=javascript&logoColor=black" />
  <img src="https://img.shields.io/badge/Tailwind_CSS-100%25-FF69B4?style=for-the-badge&logo=tailwindcss&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub-100%25-FF1493?style=for-the-badge&logo=github&logoColor=white" />
</p>

---

## 🌸 萌图 | Cute Pics

<!-- MOE_IMG_START -->
<p align="center">
  <img src="https://t.alcy.cc/moez?r=fcc4c103" width="400" alt="萌图" />
</p>
<!-- MOE_IMG_END -->

<p align="center"><b>喵喵喵 ~ 好萌啊！| Meow ~ So cute!</b></p>
<p align="center"><sub>✨ 来源于 <a href="https://t.alcy.cc">举个栗子 API</a> ✨</sub></p>

---

## 🦊 小狐狸 | Little Fox

<!-- FOX_IMG_START -->
<p align="center">
  <img src="https://t.alcy.cc/xhl?r=33ad" width="400" alt="小狐狸" />
</p>
<!-- FOX_IMG_END -->

<p align="center"><b>嘤嘤嘤 ~ 狐狸好软！| Yip yip ~ So fluffy!</b></p>
<p align="center"><sub>✨ 来源于 <a href="https://t.alcy.cc">举个栗子 API</a> ✨</sub></p>

---

## 💬 每日一言 | Daily Quote

<!-- DAILY_QUOTE_START -->
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=3000&color=FF69B4&center=true&vCenter=true&width=700&lines=%E4%B8%80%E4%BB%A5%E8%B4%AF%E4%B9%8B%E7%9A%84%E5%8A%AA%E5%8A%9B%EF%BC%8C%E4%B8%8D%E5%BE%97%E6%87%88%E6%80%A0%E7%9A%84%E4%BA%BA%E7%94%9F%E3%80%82;Consistent%2Befforts%2Bshall%2Bnot%2Bbe%2Bslackened%2Bin%2Blife." alt="Daily Quote" />
</p>

<p align="center"><b>🎯 中文：</b>一以贯之的努力，不得懈怠的人生。</p>
<p align="center"><b>🎯 English：</b>Consistent efforts shall not be slackened in life.</p>
<p align="center"><sub>— 天才基本法</sub></p>
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
</p>
<!-- MOE_IMG_END -->"
          
          echo "$README" | sed -n '1,/<!-- MOE_IMG_START -->
<p align="center">
  <img src="https://t.alcy.cc/moez?r=fcc4c103" width="400" alt="萌图" />
</p>
<!-- MOE_IMG_END -->/,$p' | tail -n +2 >> temp.md
          
          mv temp.md README.md

      - name: Update Fox Image
        run: |
          README=$(cat README.md)
          
          NEW_FOX="<!-- FOX_IMG_START -->
<p align="center">
  <img src="https://t.alcy.cc/xhl?r=33ad" width="400" alt="小狐狸" />
</p>
<!-- FOX_IMG_END -->"
          
          echo "$README" | sed -n '1,/<!-- FOX_IMG_START -->
<p align="center">
  <img src="https://t.alcy.cc/xhl?r=33ad" width="400" alt="小狐狸" />
</p>
<!-- FOX_IMG_END -->/,$p' | tail -n +2 >> temp.md
          
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
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=3000&color=FF69B4&center=true&vCenter=true&width=700&lines=%E4%B8%80%E4%BB%A5%E8%B4%AF%E4%B9%8B%E7%9A%84%E5%8A%AA%E5%8A%9B%EF%BC%8C%E4%B8%8D%E5%BE%97%E6%87%88%E6%80%A0%E7%9A%84%E4%BA%BA%E7%94%9F%E3%80%82;Consistent%2Befforts%2Bshall%2Bnot%2Bbe%2Bslackened%2Bin%2Blife." alt="Daily Quote" />
</p>

<p align="center"><b>🎯 中文：</b>一以贯之的努力，不得懈怠的人生。</p>
<p align="center"><b>🎯 English：</b>Consistent efforts shall not be slackened in life.</p>
<p align="center"><sub>— 天才基本法</sub></p>
<!-- DAILY_QUOTE_END -->"
          
          echo "$README" | sed -n '1,/<!-- DAILY_QUOTE_START -->
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=3000&color=FF69B4&center=true&vCenter=true&width=700&lines=%E4%B8%80%E4%BB%A5%E8%B4%AF%E4%B9%8B%E7%9A%84%E5%8A%AA%E5%8A%9B%EF%BC%8C%E4%B8%8D%E5%BE%97%E6%87%88%E6%80%A0%E7%9A%84%E4%BA%BA%E7%94%9F%E3%80%82;Consistent%2Befforts%2Bshall%2Bnot%2Bbe%2Bslackened%2Bin%2Blife." alt="Daily Quote" />
</p>

<p align="center"><b>🎯 中文：</b>一以贯之的努力，不得懈怠的人生。</p>
<p align="center"><b>🎯 English：</b>Consistent efforts shall not be slackened in life.</p>
<p align="center"><sub>— 天才基本法</sub></p>
<!-- DAILY_QUOTE_END -->/,$p' | tail -n +2 >> temp.md
          
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
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=3000&color=FF69B4&center=true&vCenter=true&width=700&lines=%E4%B8%80%E4%BB%A5%E8%B4%AF%E4%B9%8B%E7%9A%84%E5%8A%AA%E5%8A%9B%EF%BC%8C%E4%B8%8D%E5%BE%97%E6%87%88%E6%80%A0%E7%9A%84%E4%BA%BA%E7%94%9F%E3%80%82;Consistent%2Befforts%2Bshall%2Bnot%2Bbe%2Bslackened%2Bin%2Blife." alt="Daily Quote" />
</p>

<p align="center"><b>🎯 中文：</b>一以贯之的努力，不得懈怠的人生。</p>
<p align="center"><b>🎯 English：</b>Consistent efforts shall not be slackened in life.</p>
<p align="center"><sub>— 天才基本法</sub></p>
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
