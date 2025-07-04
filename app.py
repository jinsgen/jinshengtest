from flask import Flask, render_template_string

app = Flask(__name__)

HEADER_HOME = """
<header class="main-header">
  <div class="header-content">
    <div class="logo-area">
      <img src="/static/logo_transparent.png" alt="LOGO" class="logo">
      <div class="brand">溍慎有限公司<br>鈦吉有限公司</div>
    </div>
    <input type="checkbox" id="nav-toggle" hidden>
    <label for="nav-toggle" class="nav-toggle-label">
      <span></span>
      <span></span>
      <span></span>
    </label>
    <nav>
      <a href="/"           class="nav-link">首頁</a>
      <a href="/about"      class="nav-link">關於溍慎</a>
      <a href="/#services"  class="nav-link">服務項目</a>
      <a href="/process"    class="nav-link">加工流程</a>
      <a href="#contact"    class="nav-link">聯絡我們</a>
    </nav>
  </div>
</header>
"""

HEADER_SOLID = HEADER_HOME.replace("main-header", "main-header solid", 1)

FOOTER_HTML = """
<footer id="contact" style="
  background: #f2f7fb;
  padding: 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  line-height: 1.8;
  margin-top: 40px;
">
  <h2 style="color: #6d8ec7; border-bottom: 2px solid #6d8ec7; padding-bottom:8px; margin-top:0;">
    聯絡資訊
  </h2>
  地址：<a href="https://maps.app.goo.gl/8dkFhGhkzxeEaBYaA" target="_blank">台南市仁德區義林路148巷16號</a><br>
  Tel：06-2708989<br>
  Fax：06-2707878<br>
  Mobile：0975124624（鄭先生）<br>
  Email：<a href="mailto:js42915245@gmail.com">js42915245@gmail.com</a>
</footer>
"""

HOME_HTML = f"""
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>溍慎/鈦吉有限公司</title>
  <link rel="icon" href="/static/favicon.ico" type="image/x-icon">
  <link href="https://unpkg.com/aos@2.3.4/dist/aos.css" rel="stylesheet">
  <script src="https://unpkg.com/aos@2.3.4/dist/aos.js"></script>
  <script>document.addEventListener('DOMContentLoaded',()=>AOS.init({{duration:800,once:true}}));</script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700&family=Noto+Sans+TC:wght@700&display=swap');
    :root {{ --primary-blue: #6d8ec7; --accent-yellow: #FFD85A; }}
    html {{ scroll-behavior: smooth; }}
    body {{ margin:0; font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif; background: #fff; }}

    /* ===== HEADER ===== */
    .main-header {{
      width: 100vw;
      background: rgba(109, 142, 199, 0.62);
      color: white;
      position: sticky; top: 0; z-index: 10;
      box-shadow: 0 1px 6px rgba(90,110,140,.06);
      backdrop-filter: blur(4px);
      min-width: 320px;
      font-size: 16px;
      transition: background 0.25s;
    }}
    .main-header.solid {{
      background: #6d8ec7;
      backdrop-filter: none;
    }}
    /* ... (其餘 header, nav, banner, slogan, main, services-summary 等樣式維持不變) ... */

    /* ===== 服務項目：五格平均分配 & 放大 ===== */
    .services {{
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      grid-auto-rows: 250px;
      gap: 36px;
      margin: 44px auto 0 auto;
      max-width: 1200px;
      width: 100%;
      justify-items: center;
      align-items: center;
    }}
    .service-item {{
      width: 100%;
      height: 100%;
      font-size: 1.2em;
      /* 其餘行為保持原狀：背景圖、圓角、陰影、hover 效果等 */
    }}

    /* ===== 其餘原有樣式保持不變 ===== */
  </style>
</head>
<body>
  {HEADER_HOME}
  <div class="banner-bg"></div>
  <div class="banner-content" data-aos="fade-in">
    <!-- slogan-group 如前 -->
  </div>
  <main>
    <!-- 主要業務區塊如前 -->

    <section id="services">
      <h2 data-aos="fade-up">服務項目</h2>
      <div class="services">
        <a href="/vibration" class="service-item" style="background-image:url('/static/vibration.jpg');" data-aos="zoom-in">
          <div class="service-item-content">
            <h3>振動研磨</h3>
            <p>去除毛邊、拋光與表面均化。</p>
          </div>
        </a>
        <a href="/sealing" class="service-item" style="background-image:url('/static/sealing.jpg');" data-aos="zoom-in">
          <div class="service-item-content">
            <h3>含浸封孔</h3>
            <p>提高氣密性與耐用性。</p>
          </div>
        </a>
        <a href="/coating" class="service-item" style="background-image:url('/static/coating.jpg');" data-aos="zoom-in">
          <div class="service-item-content">
            <h3>皮膜化成</h3>
            <p>耐蝕塗裝處理，自動化產線。</p>
          </div>
        </a>
        <a href="/robotic" class="service-item" style="background-image:url('/static/robotic.jpg');" data-aos="zoom-in">
          <div class="service-item-content">
            <h3>自動化機械手臂</h3>
            <p>搭配工具快速作業。</p>
          </div>
        </a>
        <a href="/wastewater" class="service-item" style="background-image:url('/static/wastewater.jpg');" data-aos="zoom-in">
          <div class="service-item-content">
            <h3>廢水處理</h3>
            <p>淨化廢水、達標排放。</p>
          </div>
        </a>
      </div>
    </section>

    {FOOTER_HTML}
  </main>
</body>
</html>
"""

def render_subpage(title, content_html, aos_effect="fade-up"):
    return render_template_string(f"""
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>{title}</title>
  <link rel="icon" href="/static/favicon.ico" type="image/x-icon">
  <link href="https://unpkg.com/aos@2.3.4/dist/aos.css" rel="stylesheet">
  <script src="https://unpkg.com/aos@2.3.4/dist/aos.js"></script>
  <script>document.addEventListener('DOMContentLoaded',()=>AOS.init({{duration:800,once:true}}));</script>
  <style>
    /* ===== 保持共用 header/footer 樣式不變 ===== */

    /* ===== 淺色流程圖 ===== */
    .flow-horizontal {{
      display: flex;
      align-items: flex-end;
      gap: 36px;
      overflow-x: auto;
      padding: 22px 6px;
      margin: 38px auto 34px auto;
      max-width: 98vw;
      scroll-behavior: smooth;
      scrollbar-width: thin;
      cursor: grab;
      user-select: none;
    }}
    .flow-step {{
      background: #dbe7f4;   /* 淡藍色 */
      border-radius: 16px;
      box-shadow: 0 2px 12px rgba(90,110,180,0.06);
      min-width: 175px;
      width: 15vw;
      padding: 18px 12px 10px 12px;
      display: flex;
      flex-direction: column;
      align-items: center;
      color: #284052;
      text-align: center;
      position: relative;
      cursor: pointer;
      transition: transform .22s, box-shadow .16s;
      flex-shrink: 0;
    }}
    .flow-step:hover, .flow-step:focus {{
      transform: translateY(-4px) scale(1.06);
      box-shadow: 0 4px 28px rgba(70,100,180,0.12);
      z-index: 2;
    }}

    /* ===== 箭頭上顯示流程編號 ===== */
    .flow-arrow {{
      position: relative;
      font-size: 2.2em;
      color: rgba(109,142,199,0.7);
      font-weight: 900;
      margin: 0 6px;
      user-select: none;
    }}
    .arrow-num {{
      position: absolute;
      top: -20px;
      left: 50%;
      transform: translateX(-50%);
      background: var(--accent-yellow);
      color: #284052;
      border-radius: 50%;
      width: 24px;
      height: 24px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.9em;
      font-weight: 700;
      box-shadow: 0 1px 4px rgba(0,0,0,0.2);
    }}

    .flow-step-img {{
      width: 95px;
      height: 64px;
      object-fit: cover;
      border-radius: 8px;
      margin-bottom: 12px;
      background: #eee;
      box-shadow: 0 2px 6px #2222;
      transition: filter .22s;
      filter: brightness(0.93) grayscale(0.05);
    }}
    .flow-step h3 {{
      font-size: 1.07em;
      font-weight: 900;
      margin: 7px 0 2px 0;
      color: #284052;
    }}
    .flow-step p {{
      font-size: .97em;
      margin: 0 0 2px 0;
      color: #455674;
      line-height: 1.7;
    }}

    /* ===== 其餘原有樣式保持不變 ===== */
  </style>
</head>
<body>
  {HEADER_SOLID}
  <main data-aos="{aos_effect}">
    <h2 data-aos="fade-up">{title}</h2>
    {content_html}
    {FOOTER_HTML}
  </main>
  <script>
    // 滑鼠拖曳橫向流程圖
    const el = document.querySelector('.flow-horizontal');
    if (el) {{
      let isDown = false;
      let startX, scrollLeft;
      el.addEventListener('mousedown', e => {{
        isDown = true;
        el.classList.add('active');
        startX = e.pageX - el.offsetLeft;
        scrollLeft = el.scrollLeft;
      }});
      el.addEventListener('mouseleave', e => {{ isDown = false; el.classList.remove('active'); }});
      el.addEventListener('mouseup', e => {{ isDown = false; el.classList.remove('active'); }});
      el.addEventListener('mousemove', e => {{
        if (!isDown) return;
        e.preventDefault();
        const x = e.pageX - el.offsetLeft;
        el.scrollLeft = scrollLeft - (x - startX);
      }});
    }}
  </script>
</body>
</html>
""")

@app.route("/")
def home():
    return render_template_string(HOME_HTML)

@app.route("/about")
def about():
    # (保持 about 頁面內容不變)
    ...

@app.route("/process")
def process():
    steps = [
        {{ "num": "1", "img": "/static/robotic.jpg", "title": "自動化機械手臂", "desc": "可搭配工具快速作業", "route": "robotic" }},
        {{ "num": "2", "img": "/static/vibration.jpg", "title": "振動研磨", "desc": "表面均化處理", "route": "vibration" }},
        {{ "num": "3", "img": "/static/sealing.jpg", "title": "含浸封孔", "desc": "提升氣密性與耐用性", "route": "sealing" }},
        {{ "num": "4", "img": "/static/coating.jpg", "title": "皮膜化成", "desc": "依需求選擇性進行", "route": "coating" }},
        {{ "num": "5", "img": "/static/wastewater.jpg", "title": "廢水處理", "desc": "淨化廢水、達標排放", "route": "wastewater" }}
    ]
    flow_html = '<div class="flow-horizontal" tabindex="0" data-aos="fade-in">'
    for i, s in enumerate(steps):
        flow_html += f'''
        <a href="/{s['route']}" class="flow-step" tabindex="0">
            <img src="{s['img']}" class="flow-step-img" alt="{s['title']}">
            <h3>{s['title']}</h3>
            <p>{s['desc']}</p>
        </a>
        '''
        if i < len(steps) - 1:
            # 在箭頭上顯示下一步的編號
            next_num = steps[i+1]['num']
            flow_html += f'''
            <div class="flow-arrow"><span class="arrow-num">{next_num}</span>→</div>
            '''
    flow_html += "</div>"

    desc_html = """
    <!-- 加工流程補充說明保持不變 -->
    """
    return render_subpage("加工流程", flow_html + desc_html, aos_effect="fade-down")

# 其它子頁面 route 保持不變...

if __name__ == "__main__":
    app.run(debug=True)
