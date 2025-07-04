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
    .header-content {{
      max-width: 1100px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 56px;
      padding: 0 16px;
      position:relative;
    }}
    .logo-area {{
      display: flex;
      align-items: center;
      gap: 14px;
      min-width:0;
    }}
    .logo {{
      height: 42px; width: 42px; min-width:38px; object-fit: contain; display: block;
      transition: all 0.2s;
    }}
    .brand {{
      font-size: 1.11rem; line-height: 1.19;
      font-weight: 700; letter-spacing: 1.1px;
      white-space: pre-line;
      text-shadow: 0 2px 6px rgba(30,55,110,0.11);
      margin-top: 1px;
      transition: all 0.2s;
    }}
    nav {{
      display: flex;
      gap: 12px;
      align-items: center;
      flex-wrap: wrap;
      font-size: 1em;
      transition: all 0.2s;
    }}
    .nav-link {{
      color:white; text-decoration:none; font-weight:600;
      padding:6px 15px; border-radius:4px; transition: background .2s, transform .1s;
      font-size: 1em;
      letter-spacing: 0.5px;
    }}
    .nav-link:hover {{
      background: rgba(255,255,255,0.22);
    }}
    .nav-link:active {{
      background: rgba(255,255,255,0.32); transform: translateY(2px);
    }}

    .nav-toggle-label {{
      display: none;
      flex-direction: column;
      justify-content: center;
      height: 36px;
      width: 36px;
      cursor: pointer;
      margin-left: 8px;
      z-index:12;
    }}
    .nav-toggle-label span {{
      display: block;
      height: 4px;
      width: 28px;
      background: #fff;
      margin: 4px 0;
      border-radius: 2px;
      transition: all .28s cubic-bezier(.4,2,.6,1);
    }}
    #nav-toggle:checked + .nav-toggle-label span:nth-child(1) {{
      transform: translateY(8px) rotate(45deg);
    }}
    #nav-toggle:checked + .nav-toggle-label span:nth-child(2) {{
      opacity: 0;
    }}
    #nav-toggle:checked + .nav-toggle-label span:nth-child(3) {{
      transform: translateY(-8px) rotate(-45deg);
    }}

    @media(max-width:820px){{
      .header-content{{
        padding: 0 2vw;
        height:44px;
      }}
      .brand{{font-size:10.2px;}}
      .logo{{height:26px;width:26px;}}
      nav{{
        position: fixed;
        top:56px; right:0; left:0;
        background:rgba(109, 142, 199, 0.95);
        flex-direction: column;
        align-items: flex-end;
        gap:0;
        box-shadow: 0 4px 12px rgba(80,80,120,0.13);
        padding: 0;
        display: none;
        z-index:99;
        width:100vw;
      }}
      #nav-toggle:checked ~ nav {{
        display: flex;
      }}
      .nav-link{{
        padding:14px 22px 14px 18px;
        font-size:1.06em;
        width:100vw;
        text-align:right;
        border-radius:0;
        border-bottom:1px solid rgba(255,255,255,0.07);
      }}
      .nav-toggle-label {{
        display: flex;
      }}
    }}
    @media(max-width:500px){{
      .header-content{{
        height:34px;
      }}
      .logo{{height:18px;width:18px;}}
      .brand{{font-size:8px;}}
      .nav-link{{font-size:0.91em;}}
    }}

    .banner-bg {{
      position: absolute; top: 0; left: 0;
      width: 100vw; height: 350px;
      background: url('/static/banner_new.jpg') center center/cover no-repeat;
      z-index: 0;
      min-height: 200px;
      pointer-events: none;
    }}
    .banner-content {{
      position: absolute;
      top: 0; left: 0; right: 0;
      width: 100vw;
      height: 350px;
      z-index: 1;
      display: flex;
      align-items: center;
      justify-content: flex-end;
      pointer-events: none;
    }}
    .slogan-group {{
      margin-right: 10vw;
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      justify-content: center;
      height: 100%;
      pointer-events: none;
    }}
    .slogan-line {{
      font-size: 54px;
      font-family: 'Montserrat', 'Noto Sans TC', sans-serif;
      font-weight: 700;
      color: #fff;
      letter-spacing: 1.2px;
      margin: 0 0 16px 0;
      line-height: 1.15;
      text-shadow: 0 3px 12px rgba(40,60,90,0.32), 0 2px 8px rgba(0,0,0,0.18);
      background: none;
      border: none;
      padding: 0;
      white-space: nowrap;
    }}
    .slogan-line:last-child{{margin-bottom:0;}}

    main {{ max-width:1200px; margin:400px auto 0 auto; padding:0 20px; position:relative; z-index:2; }}
    h2 {{ color:var(--primary-blue); border-bottom:2px solid var(--primary-blue); padding-bottom:8px; }}

    /* ===== 主要業務分類樣式 ===== */
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
    @media(max-width:900px){{
      .main-services-summary {{
        padding: 20px 4vw;
      }}
      .main-services-list {{
        flex-direction: column;
        gap: 22px;
      }}
      .main-services-list .biz-item {{
        min-width: 0;
        max-width: unset;
        padding: 15px 10px;
        font-size: 1em;
      }}
    }}

    /* ===== 服務項目新排版：三上二下，下排分開置中 ===== */
    .services {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      grid-template-rows: 210px 210px;
      gap: 32px;
      margin: 38px auto 0 auto;
      max-width: 900px;
      width:100%;
      justify-items: center;
      align-items: center;
    }}
    .service-item {{
      position: relative;
      background-size: cover;
      background-position: center;
      border-radius: 18px;
      box-shadow: 0 2px 16px rgba(90,110,180,0.11);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      align-items: flex-start;
      cursor: pointer;
      transition: transform .25s, box-shadow .19s, filter .18s;
      width: 96%;
      height: 100%;
      color: #fff;
    }}
    .service-item::before {{
      content:'';
      display:block;
      position:absolute;inset:0;
      background:rgba(30,32,45,0.36); /* 淡黑色 */
      transition: background .18s;
      z-index:1;
    }}
    .service-item:hover, .service-item:focus {{
      transform: scale(1.045) translateY(-2px);
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
      padding: 20px 20px 18px 22px;
      width:100%;
      color:#fff;
      text-shadow: 0 2px 8px rgba(20,20,20,0.36),0 2px 14px #222;
      font-weight: 700;
    }}
    .service-item h3 {{
      font-size:1.28em;
      font-family:'Montserrat','Noto Sans TC',sans-serif;
      font-weight:900;
      letter-spacing:1.2px;
      margin:0 0 10px 0;
      color:#fff;
      text-shadow: 0 4px 12px #1a1a1a;
    }}
    .service-item p {{
      font-size:1.09em;
      font-weight:600;
      margin:0;
      color:#fff;
      line-height:1.6;
      text-shadow:0 3px 12px #181818;
    }}
    /* 三上二下配置，下排分開左右，左右間距一致 */
    .services .service-item:nth-child(4) {{
      grid-column: 1 / 2;
      grid-row: 2 / 3;
      justify-self: end;
    }}
    .services .service-item:nth-child(5) {{
      grid-column: 3 / 4;
      grid-row: 2 / 3;
      justify-self: start;
    }}
    @media (max-width:900px){{
      .services {{
        grid-template-columns: 1fr;
        grid-template-rows: none;
        gap:22px;
        justify-items:center;
      }}
      .service-item {{
        min-width:0;width:97vw;max-width:500px;min-height:130px;height:34vw;max-height:230px;
      }}
      .services .service-item:nth-child(4),
      .services .service-item:nth-child(5) {{
        grid-column:1; justify-self:center; width:97vw; max-width:500px;
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

# 其餘路由內容不變，與之前一致（略）

def render_subpage(title, content_html, aos_effect="fade-up"):
    # ...（與之前一樣）
    # 這裡省略，如要完整版再貼一次

@app.route("/")
def home():
    return render_template_string(HOME_HTML)

# ...其餘 /about, /process, /vibration, /sealing, /coating, /robotic, /wastewater 路由同前

if __name__ == "__main__":
    app.run(debug=True)
