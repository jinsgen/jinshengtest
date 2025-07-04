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

    /* ===== 服務項目新排版：三上二下 ===== */
    .services {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      grid-template-rows: repeat(2, 210px);
      gap: 32px 32px;
      margin: 38px auto 0 auto;
      max-width: 900px;
      width:100%;
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
      transition: transform .25s cubic-bezier(.22,1.14,.36,1), box-shadow .19s, filter .18s;
      min-width: 0;
    }}
    .service-item::before {{
      content:'';
      display:block;
      position:absolute;inset:0;
      background:rgba(255,255,255,0.61);
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
      background:rgba(255,255,255,0.40);
    }}
    .service-item-content {{
      position: relative;
      z-index:2;
      padding: 20px 20px 18px 22px;
      width:100%;
      color:#294766;
      text-shadow:0 2px 6px rgba(255,255,255,0.07);
    }}
    .service-item h3 {{
      font-size:1.28em;
      font-family:'Montserrat','Noto Sans TC',sans-serif;
      font-weight:900;
      letter-spacing:1.2px;
      margin:0 0 10px 0;
      color:#1a385c;
      text-shadow:0 3px 12px rgba(250,255,255,0.22);
    }}
    .service-item p {{
      font-size:1.09em;
      font-weight:600;
      margin:0;
      color:#345377;
      line-height:1.6;
      text-shadow:0 3px 12px rgba(255,255,255,0.12);
    }}
    /* 三上二下配置 */
    .services .service-item:nth-child(4) {{
      grid-column: 2/3;
      grid-row: 2/3;
      justify-self: center;
    }}
    .services .service-item:nth-child(5) {{
      grid-column: 3/4;
      grid-row: 2/3;
      justify-self: center;
    }}
    /* 移動端優化 */
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
        grid-column:1;
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
    /* 加工流程圖 */
    .flow-horizontal {{
      display: flex;
      align-items: center;
      gap: 44px;
      overflow-x: auto;
      overflow-y: visible;
      padding: 22px 12px 12px 12px;
      margin: 0 auto 30px auto;
      max-width: 98vw;
      scrollbar-width: thin;
      cursor: grab;
      user-select: none;
      -webkit-overflow-scrolling: touch;
      background: transparent;
    }}
    .flow-horizontal:active {{ cursor: grabbing; }}
    .flow-step {{
      background: #f2f7fb;
      min-width: 172px;
      width: 205px;
      max-width: 260px;
      border-radius: 17px;
      box-shadow: 0 2px 11px rgba(70,120,160,0.10);
      padding: 22px 15px 18px 15px;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      transition: transform .18s, box-shadow .18s;
      position:relative;
      border: 2px solid #dde8f5;
    }}
    .flow-step:hover, .flow-step:focus {{
      transform: scale(1.045) translateY(-2px);
      box-shadow:0 6px 22px rgba(60,100,160,0.16);
      z-index:2;
      border-color: #6d8ec7;
    }}
    .flow-step:active {{
      transform: scale(1.01) translateY(1px);
      box-shadow:0 2px 7px rgba(80,110,160,0.17);
    }}
    .flow-step-img {{
      width: 92px; height: 92px;
      object-fit: cover;
      border-radius: 13px;
      margin-bottom: 10px;
      border: 2px solid #e1eefa;
      background: #fff;
      box-shadow: 0 2px 6px rgba(110,180,230,0.11);
    }}
    .flow-step-num {{
      position:absolute;
      top:-19px; left:50%; transform:translateX(-50%);
      background:#6d8ec7;
      color:#fff;font-size:1.18em;
      border-radius:50%;
      width:36px;height:36px;
      display:flex;align-items:center;justify-content:center;
      box-shadow:0 2px 6px rgba(60,90,140,0.13);
      font-weight:700;letter-spacing:0.5px;
      border:2px solid #e7eff8;
      z-index:3;
    }}
    .flow-step h3 {{
      font-size:1.18em;
      font-family:'Montserrat','Noto Sans TC',sans-serif;
      font-weight:900;
      color:#2a476c;
      margin:0 0 8px 0;
      letter-spacing:1.2px;
      text-shadow:0 2px 8px rgba(255,255,255,0.14);
    }}
    .flow-step p {{
      font-size:1.06em;
      font-weight:600;
      margin:0;
      color:#4d7299;
      text-shadow:0 3px 12px rgba(255,255,255,0.10);
    }}
    .flow-arrow {{
      font-size:3.3em;
      color:#b3d0ea;
      min-width: 44px;
      margin: 0 4px;
      user-select: none;
      pointer-events: none;
      display: flex;
      align-items: center;
      font-weight: 800;
      text-shadow: 0 2px 8px rgba(110,140,200,0.08);
    }}
    /* 行動裝置橫滑優化 */
    @media (max-width:900px){{
      .flow-horizontal {{
        gap:18px;
        padding:8px 3vw 8px 3vw;
        max-width: 99vw;
      }}
      .flow-step {{ min-width:142px; width:170px; padding:13px 5px 12px 5px; }}
      .flow-step-img {{ width:60px;height:60px;margin-bottom:6px; }}
      .flow-step-num {{ width:26px;height:26px;font-size:1em;top:-13px; }}
      .flow-arrow {{ font-size:2.3em;min-width:24px; }}
    }}
    /* 流程補充說明背景 */
    .dragon-desc-section {{
      background: #f2f7fb;
      border-radius: 10px;
      max-width: 900px;
      margin: 0 auto 22px auto;
      padding: 32px 20px 22px 28px;
      font-size: 1.07em;
      color: #284052;
      box-shadow: 0 2px 8px rgba(110,140,180,0.06);
      line-height: 2;
    }}
  </style>
  <!-- 拖曳/滾輪橫移功能 -->
  <script>
    document.addEventListener("DOMContentLoaded",function(){{
      const flow = document.querySelector('.flow-horizontal');
      if(flow) {{
        let isDown=false,startX,scrollLeft;
        flow.addEventListener('mousedown',e=>{{isDown=true;flow.classList.add('active');startX=e.pageX-flow.offsetLeft;scrollLeft=flow.scrollLeft;}});
        flow.addEventListener('mouseleave',()=>{{isDown=false;flow.classList.remove('active');}});
        flow.addEventListener('mouseup',()=>{{isDown=false;flow.classList.remove('active');}});
        flow.addEventListener('mousemove',e=>{{
          if(!isDown)return;
          e.preventDefault();
          const x=e.pageX-flow.offsetLeft;
          const walk=(x-startX)*1.2;
          flow.scrollLeft=scrollLeft-walk;
        }});
        // 滾輪橫移
        flow.addEventListener('wheel',e=>{{
          if(Math.abs(e.deltaX)<1&&Math.abs(e.deltaY)>0) {{
            flow.scrollLeft+=e.deltaY;
            e.preventDefault();
          }}
        }},{{passive:false}});
      }}
    }});
  </script>
</head>
<body>
  {HEADER_SOLID}
  <main data-aos="{aos_effect}">
    <h2 data-aos="fade-up">{title}</h2>
    {content_html}
    {FOOTER_HTML}
  </main>
</body>
</html>
""")

@app.route("/")
def home():
    return render_template_string(HOME_HTML)

@app.route("/about")
def about():
    content_html = "<p style='margin:40px 0;'>（原 about 內容可保留，略）</p>"
    return render_subpage("關於溍慎", content_html)

@app.route("/process")
def process():
    # 橫向流程圖步驟內容（五步驟 + 箭頭）
    steps = [
        {
            "num": "1",
            "img": "/static/robotic.jpg",
            "title": "自動化機械手臂",
            "desc": "可搭配工具快速作業"
        },
        {
            "num": "2",
            "img": "/static/vibration.jpg",
            "title": "振動研磨",
            "desc": "表面均化處理"
        },
        {
            "num": "3",
            "img": "/static/sealing.jpg",
            "title": "含浸封孔",
            "desc": "提升氣密性與耐用性"
        },
        {
            "num": "4",
            "img": "/static/coating.jpg",
            "title": "皮膜化成",
            "desc": "依需求選擇性進行"
        },
        {
            "num": "5",
            "img": "/static/wastewater.jpg",
            "title": "廢水處理",
            "desc": "淨化廢水、達標排放"
        }
    ]
    flow_html = """<div class="flow-horizontal" tabindex="0" data-aos="fade-in">"""
    for i, s in enumerate(steps):
        flow_html += f"""
        <a href="/{s['title'][:8]}" class="flow-step" tabindex="0">
            <div class="flow-step-num">{s['num']}</div>
            <img src="{s['img']}" class="flow-step-img" alt="{s['title']}">
            <h3>{s['title']}</h3>
            <p>{s['desc']}</p>
        </a>
        """
        if i != len(steps)-1:
            flow_html += """<div class="flow-arrow">→</div>"""
    flow_html += "</div>"
    # 補充說明
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
    return render_subpage("振動研磨", "<p>去除毛邊、拋光與表面均化。</p>")

@app.route("/sealing")
def sealing():
    return render_subpage("含浸封孔", "<p>提高氣密性與耐用性。</p>")

@app.route("/coating")
def coating():
    return render_subpage("皮膜化成", "<p>耐蝕塗裝處理，自動化產線。</p>")

@app.route("/robotic")
def robotic():
    return render_subpage("自動化機械手臂", "<p>搭配工具快速作業。</p>")

@app.route("/wastewater")
def wastewater():
    return render_subpage("廢水處理", "<p>淨化廢水、達標排放。</p>")

if __name__ == "__main__":
    app.run(debug=True)
