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
    /* … (其餘 header、nav、banner 等樣式不變) … */

    main {{ max-width:1200px; margin:400px auto 0 auto; padding:0 20px; position:relative; z-index:2; }}
    h2 {{ color:var(--primary-blue); border-bottom:2px solid var(--primary-blue); padding-bottom:8px; }}

    /* ===== 主要業務摘要 ===== */
    .main-services-summary {{
      margin: 54px auto 10px auto;
      max-width: 950px;
      background: #22283108;
      border-radius: 15px;
      box-shadow: 0 2px 16px rgba(80,110,180,0.06);
      padding: 36px 24px 26px 24px;
    }}
    .main-services-summary h2 {{
      color: #425e96;
      font-size: 2em;
      margin-top: 0;
      margin-bottom: 20px;
      border-bottom: 2px solid #6d8ec7;
      padding-bottom: 8px;
      letter-spacing: 2px;
    }}
    .main-services-list {{
      display: flex;
      flex-wrap: wrap;
      gap: 32px 4vw;
      justify-content: space-between;
    }}
    .main-services-list .biz-item {{
      flex: 1 1 220px;
      min-width: 220px;
      max-width: 360px;
      background: #f6f8fc;
      border-radius: 12px;
      box-shadow: 0 2px 8px rgba(110,130,180,0.07);
      padding: 18px 18px 14px 22px;
      font-size: 1.08em;
      color: #22344a;
      line-height: 1.85;
      font-weight: 500;
    }}
    .main-services-list .biz-item-title {{
      color: #254083;
      font-size: 1.17em;
      font-weight: 700;
      margin-bottom: 10px;
      letter-spacing: 1.1px;
    }}

    /* ===== 服務項目：五格平均分配 ===== */
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
      position: relative;
    }}
    .service-item {{
      position: relative;
      background-size: cover;
      background-position: center;
      border-radius: 22px;
      box-shadow: 0 2px 16px rgba(90,110,180,0.11);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      align-items: flex-start;
      cursor: pointer;
      transition: transform .25s, box-shadow .19s, filter .18s;
      width: 100%;
      height: 100%;
      color: #fff;
      font-size:1.14em;
      min-width: 0;
    }}
    .service-item::before {{
      content:'';
      display:block;
      position:absolute;inset:0;
      background:rgba(30,32,45,0.36);
      transition: background .18s;
      z-index:1;
    }}
    .service-item:hover, .service-item:focus {{
      transform: scale(1.055) translateY(-2px);
      box-shadow:0 6px 28px rgba(80,110,160,0.17);
      z-index:2;
    }}
    .service-item:active {{
      transform:scale(1.01) translateY(1px);
      box-shadow:0 2px 7px rgba(80,110,160,0.17);
    }}
    .service-item:hover::before {{
      background:rgba(30,32,45,0.22);
    }}
    .service-item-content {{
      position: relative;
      z-index:2;
      padding: 28px 20px 18px 26px;
      width:100%;
      color:#fff;
      text-shadow: 0 2px 8px rgba(20,20,20,0.36),0 2px 14px #222;
      font-weight: 700;
    }}
    .service-item h3 {{
      font-size:1.31em;
      font-family:'Montserrat','Noto Sans TC',sans-serif;
      font-weight:900;
      letter-spacing:1.2px;
      margin:0 0 10px 0;
      color:#fff;
      text-shadow: 0 4px 12px #1a1a1a;
    }}
    .service-item p {{
      font-size:1.13em;
      font-weight:600;
      margin:0;
      color:#fff;
      line-height:1.6;
      text-shadow:0 3px 12px #181818;
    }}

    /* ===== 媒體查詢（維持原有設定） ===== */
    @media(max-width:1000px){{
      .services {{
        grid-template-columns: 1fr 1fr;
        grid-template-rows: repeat(3, 170px);
        gap: 22px 10px;
        max-width: 99vw;
      }}
    }}
    @media(max-width:600px){{
      .services {{
        grid-template-columns: 1fr;
        grid-template-rows: none;
        gap: 18px;
      }}
      .service-item {{
        width: 96vw;
        min-width: 0;
        max-width: 400px;
        min-height: 90px;
        height: 27vw;
        max-height: 160px;
      }}
    }}

  </style>
</head>
<body>
  {HEADER_HOME}
  <div class="banner-bg"></div>
  <div class="banner-content" data-aos="fade-in">
    <div class="slogan-group" data-aos="fade-right" data-aos-delay="200">
      <div class="slogan-line">溍於專業，慎於品質</div>
      <div class="slogan-line">鈦造未來，吉刻成型</div>
    </div>
  </div>
  <main>
    <section class="main-services-summary" data-aos="fade-up">
      <h2>主要業務</h2>
      <div class="main-services-list">
        <div class="biz-item">
          <div class="biz-item-title">振動研磨</div>
          採用三次元震動研磨機，<b>精細處理產品邊角</b>，有效去除毛刺與尖角，實現鈍化效果。研磨後的產品邊角光滑圓潤，不僅提升後續製程的附著力，也確保組裝時的安全性。
        </div>
        <div class="biz-item">
          <div class="biz-item-title">含浸封孔</div>
           針對鑄造過程產生的沙孔，運用<b>專業含浸封孔技術</b>進行填補密封，有效防止液體或氣體因壓力而洩漏。含浸處理後，產品密封性與耐壓性大幅提升。
        </div>
        <div class="biz-item">
          <div class="biz-item-title">皮膜化成</div>
          於產品表面生成<b>均勻的金屬皮膜鍍層</b>，大幅提升表面硬度、耐磨性與抗腐蝕性，同時增強表面附著力，為後續工藝流程打下堅實基礎。
        </div>
      </div>
    </section>
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
    /* ===== 共用字體 & 佈局 ===== */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700&family=Noto+Sans+TC:wght@700&display=swap');
    :root {{ --primary-blue: #6d8ec7; }}
    html {{ scroll-behavior: smooth; }}
    body {{ margin:0; font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif; }}
    .main-header {{
      width: 100vw;
      background: #6d8ec7;
      color: white;
      position: sticky; top: 0; z-index: 10;
      min-width: 320px;
      font-size: 16px;
    }}
    /* … header nav 不變 … */
    main{{ max-width:1100px; margin:40px auto; padding:0 20px; position:relative; z-index:2; }}
    h2 {{ color:var(--primary-blue); border-bottom:2px solid var(--primary-blue); padding-bottom:8px; }}

    /* ===== 橫向流程圖：淡色系 & 圖片放大 ===== */
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
      background: #a2c9ef; /* 淡藍色系 */
      border-radius: 16px;
      box-shadow: 0 2px 12px rgba(90,110,180,0.12);
      min-width: 175px;
      max-width: 210px;
      width: 15vw;
      padding: 18px 12px 10px 12px;
      display: flex;
      flex-direction: column;
      align-items: center;
      color: #fff;
      text-align: center;
      position: relative;
      cursor: pointer;
      transition: transform .22s, box-shadow .16s;
      flex-shrink: 0;
    }}
    .flow-step:hover, .flow-step:focus {{
      transform: translateY(-4px) scale(1.06);
      box-shadow: 0 4px 28px rgba(70,100,180,0.17);
      z-index: 2;
    }}
    .flow-step-img {{
      width: 120px; /* 放大 */
      height: 80px; /* 放大 */
      object-fit: cover;
      border-radius: 8px;
      margin-bottom: 12px;
      background: #eee;
      box-shadow: 0 2px 6px #2222;
      transition: filter .22s;
      filter: brightness(0.93) grayscale(0.05);
    }}
    .flow-arrow {{ /* 箭頭不變 */ font-size: 2.2em; color: #6d8ec7; align-self: center; font-weight: 900; margin: 0 6px; user-select: none; }}

    @media (max-width: 700px) {{
      .flow-horizontal {{
        gap: 10px;
        padding: 10px 2vw;
      }}
      .flow-step {{
        min-width: 118px;
        max-width: 148px;
        width: 40vw;
        padding: 10px 4px;
      }}
      .flow-step-img {{
        width: 90px;
        height: 60px;
      }}
    }}

    /* ===== 補充說明（淡藍背景）===== */
    .dragon-desc-section {{
      background: #f2f7fb;
      border-radius: 12px;
      padding: 32px 24px 20px 26px;
      margin: 30px 0 20px 0;
      font-size: 1.07em;
      color: #284052;
      box-shadow: 0 2px 8px rgba(110,140,180,0.06);
      line-height: 2;
      max-width: 900px;
      margin-left: auto;
      margin-right: auto;
    }}
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
    // 滑鼠拖曳橫向流程圖（不變）
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
    # (關於頁面不變)
    ...

@app.route("/process")
def process():
    # (流程頁面不變，只套用新的 CSS)
    ...

# 其餘路由（/vibration, /sealing, /coating, /robotic, /wastewater）不變

if __name__ == "__main__":
    app.run(debug=True)
