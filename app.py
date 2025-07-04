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

    /* ... header/nav/banner/css同你上一版 ... */

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

    /* 五格三上二下，全部等大，二下居中 */
    .services {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      grid-template-rows: repeat(2, 1fr);
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
      height: 170px;
      color: #fff;
      font-size:1.14em;
      min-width: 0;
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
      padding: 24px 18px 15px 24px;
      width:100%;
      color:#fff;
      text-shadow: 0 2px 8px rgba(20,20,20,0.36),0 2px 14px #222;
      font-weight: 700;
    }}
    .service-item h3 {{
      font-size:1.21em;
      font-family:'Montserrat','Noto Sans TC',sans-serif;
      font-weight:900;
      letter-spacing:1.2px;
      margin:0 0 10px 0;
      color:#fff;
      text-shadow: 0 4px 12px #1a1a1a;
    }}
    .service-item p {{
      font-size:1.03em;
      font-weight:600;
      margin:0;
      color:#fff;
      line-height:1.6;
      text-shadow:0 3px 12px #181818;
    }}
    /* 關鍵：五格三上二下，二下置中，卡片等大不偏邊 */
    .services .service-item:nth-child(1) {{ grid-row: 1; grid-column: 1; }}
    .services .service-item:nth-child(2) {{ grid-row: 1; grid-column: 2; }}
    .services .service-item:nth-child(3) {{ grid-row: 1; grid-column: 3; }}
    .services .service-item:nth-child(4) {{ grid-row: 2; grid-column: 2; }}
    .services .service-item:nth-child(5) {{ grid-row: 2; grid-column: 3; }}
    @media (max-width:900px){{
      .services {{
        grid-template-columns: 1fr 1fr;
        grid-template-rows: repeat(3, 120px);
        gap:22px 10px;
        max-width:99vw;
      }}
      .service-item {{
        font-size:1em;
        min-width:0;
        height:120px;
      }}
      .services .service-item:nth-child(1) {{ grid-row: 1; grid-column: 1; }}
      .services .service-item:nth-child(2) {{ grid-row: 1; grid-column: 2; }}
      .services .service-item:nth-child(3) {{ grid-row: 2; grid-column: 1; }}
      .services .service-item:nth-child(4) {{ grid-row: 2; grid-column: 2; }}
      .services .service-item:nth-child(5) {{ grid-row: 3; grid-column: 1/span 2; justify-self:center; }}
    }}
    @media (max-width:600px){{
      .services {{
        grid-template-columns: 1fr;
        grid-template-rows: none;
        gap:18px;
      }}
      .service-item {{
        width:96vw;
        min-width:0;
        max-width:400px;
        min-height:90px;
        height:27vw;
        max-height:160px;
      }}
      .services .service-item:nth-child(n) {{
        grid-row: auto; grid-column: auto;
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
    .header-content {{
      max-width: 1100px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 56px;
      padding: 0 16px;
    }}
    .logo-area {{
      display: flex;
      align-items: center;
      gap: 14px;
      min-width:0;
    }}
    .logo {{
      height: 42px; width: 42px; min-width:38px; object-fit: contain; display: block;
    }}
    .brand {{
      font-size: 1.11rem; line-height: 1.19;
      font-weight: 700; letter-spacing: 1.1px;
      white-space: pre-line;
      text-shadow: 0 2px 6px rgba(30,55,110,0.11);
      margin-top: 1px;
    }}
    nav {{
      display: flex;
      gap: 12px;
      align-items: center;
      flex-wrap: wrap;
      font-size: 1em;
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
    main{{ max-width:1100px; margin:40px auto; padding:0 20px; position:relative; z-index:2; }}

    /* ===== flow-horizontal 淡色系流程圖 ===== */
    .flow-horizontal {{
      display: flex;
      align-items: flex-end;
      gap: 36px;
      overflow-x: auto;
      padding: 32px 6px 32px 6px;
      margin: 38px auto 34px auto;
      max-width: 98vw;
      scroll-behavior: smooth;
      scrollbar-width: thin;
      cursor: grab;
      user-select: none;
    }}
    .flow-horizontal:active {{
      cursor: grabbing;
    }}
    .flow-step {{
      background: linear-gradient(135deg, #eaf3fc 70%, #f7faff 100%);
      border-radius: 18px;
      box-shadow: 0 2px 12px rgba(90,110,180,0.10);
      min-width: 230px;
      max-width: 260px;
      width: 18vw;
      padding: 28px 14px 16px 14px;
      display: flex;
      flex-direction: column;
      align-items: center;
      color: #235;
      text-align: center;
      position: relative;
      cursor: pointer;
      transition: transform .22s, box-shadow .16s;
      flex-shrink: 0;
    }}
    .flow-step:hover, .flow-step:focus {{
      transform: translateY(-6px) scale(1.09);
      box-shadow: 0 8px 32px rgba(70,100,180,0.17);
      z-index: 2;
    }}
    .flow-step-img {{
      width: 150px;
      height: 110px;
      object-fit: cover;
      border-radius: 10px;
      margin-bottom: 17px;
      background: #eee;
      box-shadow: 0 2px 10px #8882;
      transition: filter .18s;
      filter: brightness(0.94) grayscale(0.05);
    }}
    .flow-step h3 {{
      font-size: 1.19em;
      font-weight: 900;
      margin: 7px 0 2px 0;
      color: #244a7d;
      letter-spacing: 1.2px;
    }}
    .flow-step p {{
      font-size: 1em;
      margin: 0 0 2px 0;
      color: #4074a1;
      line-height: 1.7;
    }}
    .flow-arrow-box {{
      display: flex;
      flex-direction: column;
      align-items: center;
      margin: 0 6px;
    }}
    .flow-arrow-num {{
      font-size: 1.17em;
      background: #6d8ec7;
      color: #fff;
      border-radius: 8px;
      width: 28px;
      height: 28px;
      line-height: 28px;
      font-weight: 900;
      margin-bottom: 0px;
      margin-top: 0px;
      box-shadow: 0 2px 6px #3e64a855;
      margin-left: 3px;
      margin-right: 3px;
      letter-spacing: 1px;
    }}
    .flow-arrow {{
      font-size: 2.0em;
      color: #90b4d6;
      align-self: center;
      font-weight: 900;
      user-select: none;
      margin-top: 2px;
    }}
    @media (max-width: 900px) {{
      .flow-horizontal {{
        gap: 16px;
        padding: 18px 2vw;
      }}
      .flow-step {{
        min-width: 160px;
        max-width: 185px;
        width: 40vw;
        padding: 10px 4px 10px 4px;
      }}
      .flow-step-img {{
        width: 80px;
        height: 58px;
      }}
    }}
    /* ===== 補充說明 淡藍背景 ===== */
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
      el.addEventListener('wheel', e => {{
        el.scrollLeft += e.deltaY + e.deltaX;
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
    # ... same as previous, omitted for brevity ...
    return render_subpage("關於溍慎", "...", aos_effect="fade-up")

@app.route("/process")
def process():
    steps = [
        {
            "num": "1",
            "img": "/static/robotic.jpg",
            "title": "自動化機械手臂",
            "desc": "可搭配工具快速作業",
            "route": "robotic"
        },
        {
            "num": "2",
            "img": "/static/vibration.jpg",
            "title": "振動研磨",
            "desc": "表面均化處理",
            "route": "vibration"
        },
        {
            "num": "3",
            "img": "/static/sealing.jpg",
            "title": "含浸封孔",
            "desc": "提升氣密性與耐用性",
            "route": "sealing"
        },
        {
            "num": "4",
            "img": "/static/coating.jpg",
            "title": "皮膜化成",
            "desc": "依需求選擇性進行",
            "route": "coating"
        },
        {
            "num": "5",
            "img": "/static/wastewater.jpg",
            "title": "廢水處理",
            "desc": "淨化廢水、達標排放",
            "route": "wastewater"
        }
    ]
    flow_html = """<div class="flow-horizontal" tabindex="0" data-aos="fade-in">"""
    for i, s in enumerate(steps):
        flow_html += f"""
        <a href="/{s['route']}" class="flow-step" tabindex="0">
            <img src="{s['img']}" class="flow-step-img" alt="{s['title']}">
            <h3>{s['title']}</h3>
            <p>{s['desc']}</p>
        </a>
        """
        if i != len(steps)-1:
            flow_html += f"""
            <div class="flow-arrow-box">
              <div class="flow-arrow-num">{steps[i+1]['num']}</div>
              <div class="flow-arrow">→</div>
            </div>
            """
    flow_html += "</div>"
    desc_html = """
    <div class="dragon-desc-section" data-aos="fade-up">
      <h3 style="color:#4166a9; font-size:1.25em; margin:0 0 18px 0;">加工流程補充說明</h3>
      <p>
        本公司依據 <b>ISO 9001:2015 品質管理系統</b> 作業，從客戶送來的貨件開始，即進行嚴格的<span style="color:#4166a9;"><b>進料檢驗</b></span>。若發現異常情形，如生鏽、碰損或其他瑕疵，會第一時間主動通知廠商，並依廠商決定是否退回或繼續加工。<br><br>
        每一品項皆建立對應的 <b>SOP 標準作業流程</b>，並搭配照片與紀錄，要求所有員工依照流程標準執行，確保加工一致性與品質穩定性。<br><br>
        <b>1. 初步處理</b>：鑄造完成的工件會產生毛邊，若毛邊過厚、振動研磨無法直接處理，則會先進行前處理（如：機械手臂修整、氣動銼刀修邊），再進入振動研磨程序。<br><br>
        <b>2. 振動研磨</b>：毛邊去除後，表面會留有加工痕跡，因此透過振動研磨來統一表面質感、修飾瑕疵。部分廠商會於此階段先將工件取回再加工後，重新交由我們執行下一步。<br><br>
        <b>3. 含浸封孔與皮膜化成</b>：汽車零件常見沙孔問題，若零件需具備氣密性，會進行含浸封孔處理以補強孔隙。考量部分工件需經海運，也會配合進行皮膜化成處理，以提升抗鹽霧腐蝕能力。<br><br>
        <b>4. 廢水處理</b>：因加工各項程序會需要排放廢水，本公司設有自主管理的廢水處理系統，將所有排出液體集中處理、過濾與排放，符合環保與法規要求。
      </p>
    </div>
    """
    return render_subpage("加工流程", flow_html + desc_html, aos_effect="fade-down")

@app.route("/vibration")
def vibration():
    return render_subpage("振動研磨", "<p>採用三次元震動研磨機，<b>精細處理產品邊角</b>，有效去除毛刺與尖角，實現鈍化效果。研磨後的產品邊角光滑圓潤，不僅提升後續製程的附著力，也確保組裝時的安全性。</p>")

@app.route("/sealing")
def sealing():
    return render_subpage("含浸封孔", "<p>針對鑄造過程產生的沙孔，運用<b>專業含浸封孔技術</b>進行填補密封，有效防止液體或氣體因壓力而洩漏。含浸處理後，產品密封性與耐壓性大幅提升。</p>")

@app.route("/coating")
def coating():
    return render_subpage("皮膜化成", "<p>於產品表面生成<b>均勻的金屬皮膜鍍層</b>，大幅提升表面硬度、耐磨性與抗腐蝕性，同時增強表面附著力，為後續工藝流程打下堅實基礎。</p>")

@app.route("/robotic")
def robotic():
    return render_subpage("自動化機械手臂", "<p>搭配工具快速作業。</p>")

@app.route("/wastewater")
def wastewater():
    return render_subpage("廢水處理", "<p>淨化廢水、達標排放。</p>")

if __name__ == "__main__":
    app.run(debug=True)
