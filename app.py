from flask import Flask, render_template_string

app = Flask(__name__)

# 共用 HEADER 與 FOOTER
HEADER_HTML = """
<header class="main-header">
  <div class="header-content">
    <div class="logo-area">
      <img src="/static/logo_transparent.png" alt="LOGO" class="logo">
      <div class="brand">溍慎有限公司<br>鈦吉有限公司</div>
    </div>
    <input type="checkbox" id="nav-toggle" hidden>
    <label for="nav-toggle" class="nav-toggle-label">
      <span></span><span></span><span></span>
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

# 首頁模板
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
  <script>
    document.addEventListener('DOMContentLoaded',()=>AOS.init({{duration:800,once:true}}));
  </script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700&family=Noto+Sans+TC:wght@700&display=swap');
    :root {{ --primary-blue: #6d8ec7; --accent-yellow: #FFD85A; }}
    html {{ scroll-behavior: smooth; }}
    body {{ margin:0; font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif; background: #fff; }}

    /* ===== Header ===== */
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
    /* ... nav、banner 等樣式維持原樣 ... */

    /* ===== 首頁服務項目：五格平均 & 圖片放大 ===== */
    .services {{
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      grid-template-rows: 220px;
      gap: 36px 30px;
      margin: 44px auto 0 auto;
      max-width: 1000px;
      width: 100%;
      justify-items: center;
      align-items: center;
    }}
    .service-item {{
      width: 100%;
      height: 100%;
      background-size: cover;
      background-position: center;
      border-radius: 22px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      padding: 28px 20px 18px 26px;
      color: #fff;
      text-shadow: 0 2px 8px rgba(20,20,20,0.36);
      font-weight: 700;
    }}
    /* ... 其餘 service-item hover/active、媒體查詢等不變 ... */
  </style>
</head>
<body>
  {HEADER_HTML}
  <!-- banner, 主要業務等保持原有結構 -->
  <main>
    <!-- ... 主要業務 Section ... -->
    <section id="services">
      <h2 data-aos="fade-up">服務項目</h2>
      <div class="services">
        <a href="/vibration" class="service-item" style="background-image:url('/static/vibration.jpg');" data-aos="zoom-in">
          <h3>振動研磨</h3><p>去除毛邊、拋光與表面均化。</p>
        </a>
        <!-- 其餘四格同理 -->
      </div>
    </section>
    {FOOTER_HTML}
  </main>
</body>
</html>
"""

# 加工流程頁面模板（Process）
PROCESS_HTML = f"""
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>加工流程</title>
  <link rel="icon" href="/static/favicon.ico" type="image/x-icon">
  <link href="https://unpkg.com/aos@2.3.4/dist/aos.css" rel="stylesheet">
  <script src="https://unpkg.com/aos@2.3.4/dist/aos.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded',()=>AOS.init({{duration:800,once:true}}));
  </script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700&family=Noto+Sans+TC:wght@700&display=swap');
    :root {{ --primary-blue: #6d8ec7; }}
    html {{ scroll-behavior: smooth; }}
    body.process-page {{ margin:0; font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif; background: #fff; }}
    .main-header {{
      width: 100vw;
      background: #6d8ec7;
      color: white;
      position: sticky; top: 0; z-index: 10;
      min-width: 320px;
      font-size: 16px;
    }}
    /* nav、logo、footer 樣式皆同原本 */

    /* ===== 橫向流程圖：只在 process-page 下作用 ===== */
    .process-page .flow-horizontal {{
      display: flex;
      align-items: flex-end;
      gap: 36px;
      overflow-x: auto;
      padding: 22px 6px;
      margin: 38px auto 34px auto;
      max-width: 98vw;
      scrollbar-width: thin;
      cursor: grab;
      user-select: none;
    }}
    .process-page .flow-step {{
      background: #e3f2fd;      /* 淡色系背景 */
      border-radius: 16px;
      min-width: 175px;
      max-width: 210px;
      width: 15vw;
      padding: 18px 12px 10px 12px;
      text-align: center;
      flex-shrink: 0;
      transition: transform .22s, box-shadow .16s;
    }}
    .process-page .flow-step-img {{
      width: 120px;   /* 放大 */
      height: 80px;   /* 放大 */
      object-fit: cover;
      border-radius: 8px;
      margin-bottom: 12px;
    }}
    /* 保留原本 hover/focus 動畫 */
    .process-page .flow-step:hover, .process-page .flow-step:focus {{
      transform: translateY(-4px) scale(1.06);
      box-shadow: 0 4px 28px rgba(70,100,180,0.17);
      z-index: 2;
    }}
    /* 媒體查詢同原本，但加上 .process-page 前綴 */
    @media (max-width: 700px) {{
      .process-page .flow-step {{ width: 40vw; min-width:118px; max-width:148px; }}
      .process-page .flow-step-img {{ width: 90px; height:60px; }}
    }}
  </style>
</head>
<body class="process-page">
  {HEADER_HTML.replace('class="main-header"', 'class="main-header solid"')}
  <main data-aos="fade-down">
    <h2 data-aos="fade-up">加工流程</h2>
    <div class="flow-horizontal" tabindex="0" data-aos="fade-in">
      <!-- 流程步驟同原本 -->
      <a href="/robotic" class="flow-step" tabindex="0">
        <img src="/static/robotic.jpg" class="flow-step-img" alt="自動化機械手臂">
        <h3>1. 自動化機械手臂</h3>
      </a>
      <div class="flow-arrow">→</div>
      <!-- 其餘步驟同理 -->
    </div>
    <!-- 補充說明區塊同原本 -->
    {FOOTER_HTML}
  </main>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HOME_HTML)

@app.route("/about")
def about():
    # (沿用您原先的 about() 內容)
    ...

@app.route("/process")
def process():
    return render_template_string(PROCESS_HTML)

@app.route("/vibration")
def vibration():
    # (原本的振動研磨子頁)
    ...

@app.route("/sealing")
def sealing():
    # (原本的含浸封孔子頁)
    ...

@app.route("/coating")
def coating():
    # (原本的皮膜化成子頁)
    ...

@app.route("/robotic")
def robotic():
    # (原本的自動化機械手臂子頁)
    ...

@app.route("/wastewater")
def wastewater():
    # (原本的廢水處理子頁)
    ...

if __name__ == "__main__":
    app.run(debug=True)
