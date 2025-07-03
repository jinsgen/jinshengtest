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
  <script>document.addEventListener('DOMContentLoaded',()=>AOS.init());</script>
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

    /* Hamburger (手機menu) */
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

    /* Banner 與 Slogan */
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

    /* 服務項目五格(大格、2排平均) */
    .services {{
      display: flex;
      flex-wrap: wrap;
      gap: 48px 38px;
      justify-content: center;
      align-items: flex-start;
      margin-bottom: 30px;
      margin-top: 30px;
      min-height: 620px;
      width:100%;
    }}
    .service-item {{
      width: 325px;
      height: 265px;
      border-radius: 18px;
      background-size:cover;
      background-position:center;
      text-decoration:none;
      overflow:hidden;
      transition:transform .3s,box-shadow .3s;
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      min-width:0;
      box-shadow: 0 2px 12px rgba(90,110,160,0.12);
      margin-bottom:0;
      margin-right:0;
    }}
    .service-item::before {{
      content:""; position:absolute; inset:0; background:rgba(0,0,0,0.38); z-index:0;
    }}
    .service-item h3 {{
      position:relative; z-index:1; 
      color:#fff;
      font-family: 'Montserrat', 'Noto Sans TC', sans-serif;
      font-size:2.1rem; 
      font-weight: 700;
      letter-spacing: 1.3px;
      margin:0 0 10px 0;
      line-height: 1.17;
      text-shadow: 0 3px 9px rgba(45,60,110,0.23);
      text-align: left;
      padding-left: 16px;
    }}
    .service-item p {{
      position:relative; z-index:1;
      color: #f5f5f7;
      font-family: 'Noto Sans TC', 'Montserrat', sans-serif;
      font-size:1.25rem;
      margin:0 0 18px 0;
      text-align: left;
      padding-left: 16px;
      text-shadow: 0 1px 4px rgba(50,55,85,0.18);
      line-height:1.4;
      letter-spacing: 0.6px;
    }}
    .service-item:hover {{
      transform:translateY(-9px) scale(1.06);
      box-shadow:0 12px 38px rgba(0,0,0,0.21);
    }}

    @media (max-width:1150px) {{
      .services {{
        gap:32px 12px;
      }}
      .service-item {{
        width: 250px; height: 165px;
      }}
      .service-item h3{{font-size:1.1rem;}}
      .service-item p{{font-size:0.92rem;}}
    }}
    @media (max-width:900px) {{
      .services{{gap:12px 8px;}}
      .service-item{{width:43vw; min-width:150px; max-width:99vw; height:20vw; min-height:60px;}}
      main{{max-width:98vw;}}
    }}
    @media (max-width:650px) {{
      .banner-bg,.banner-content{{height:95px;}}
      main{{margin-top:135px;}}
      .services{{
        display: flex;
        flex-direction: column;
        gap:10px;
        min-height:unset;
        width:98vw;
      }}
      .service-item{{width:100%; height:86px; padding:6px 10px; font-size:11px;}}
      .service-item h3{{font-size:1em;}}
      .service-item p{{font-size:0.8em;}}
    }}
    @media(max-width:400px){{
      .banner-content{{height:60px;}}
      .slogan-line{{font-size:10px;}}
      .service-item{{height:60px; font-size:9px;}}
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
          <h3>振動研磨</h3><p>去除毛邊、拋光與表面均化。</p>
        </a>
        <a href="/sealing" class="service-item" style="background-image:url('/static/sealing.jpg');" data-aos="zoom-in">
          <h3>含浸封孔</h3><p>提高氣密性與耐用性。</p>
        </a>
        <a href="/coating" class="service-item" style="background-image:url('/static/coating.jpg');" data-aos="zoom-in">
          <h3>皮膜化成</h3><p>耐蝕塗裝處理，自動化產線。</p>
        </a>
        <a href="/robotic" class="service-item" style="background-image:url('/static/robotic.jpg');" data-aos="zoom-in">
          <h3>自動化機械手臂</h3><p>搭配工具快速作業。</p>
        </a>
        <a href="/wastewater" class="service-item" style="background-image:url('/static/wastewater.jpg');" data-aos="zoom-in">
          <h3>廢水處理</h3><p>淨化廢水、達標排放。</p>
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
  <script>document.addEventListener('DOMContentLoaded',()=>AOS.init());</script>
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
    .dragon-flow {{
      display: flex;
      flex-direction: row;
      align-items: flex-end;
      justify-content: flex-start;
      gap: 0;
      overflow-x: auto;
      padding-bottom: 34px;
      margin-bottom: 16px;
      scrollbar-width: thin;
      scrollbar-color: #b1bed7 #f2f7fb;
      -webkit-overflow-scrolling: touch;
      cursor: grab;
      user-select: none;
      position: relative;
    }}
    .step-card {{
      width: 220px;
      min-width: 220px;
      max-width: 220px;
      height: 250px;
      margin: 0 20px;
      border-radius: 12px;
      box-shadow: 0 2px 14px rgba(60, 70, 90, 0.12);
      overflow: hidden;
      background: #f7fafb;
      text-decoration: none;
      display: flex;
      flex-direction: column;
      align-items: center;
      transition: transform .3s, box-shadow .3s;
      position: relative;
    }}
    .step-card:hover {{
      transform: translateY(-7px) scale(1.04);
      box-shadow: 0 8px 24px rgba(0,0,0,0.18);
    }}
    .step-card img {{
      width: 100%;
      height: 130px;
      object-fit: cover;
      border-radius: 12px 12px 0 0;
      display: block;
    }}
    .step-card h3, .step-card p {{
      margin: 10px 0 3px 0;
      color: #365481;
      text-align: center;
      z-index: 1;
    }}
    .step-card p {{ font-size: 1rem; margin-bottom: 10px; }}
    .dragon-arrow {{
      display: flex;
      flex-direction: column;
      align-items: center;
      margin: 0 8px 18px 8px;
      user-select: none;
      min-width: 38px;
      font-weight: 800;
      opacity: 0.98;
    }}
    .dragon-arrow .arrow-num {{
      font-size: 1.18em;
      color: #fff;
      background: #6d8ec7;
      width: 38px;
      height: 38px;
      border-radius: 50%;
      display: flex; align-items: center; justify-content: center;
      margin-bottom: 2px;
      box-shadow: 0 2px 6px rgba(40,60,90,.10);
      font-family: inherit;
    }}
    .dragon-arrow .arrow-icon {{
      font-size: 2.1em;
      color: #6d8ec7;
      line-height: 1;
      margin-bottom:0;
      display:block;
    }}
    @media (max-width: 1250px) {{
      .step-card{{width:150px;min-width:150px;max-width:150px;height:140px;}}
      .step-card img{{height:60px;}}
      .dragon-arrow .arrow-num{{width:23px;height:23px;font-size:.86em;}}
    }}
    @media(max-width:1100px){{
      main {{padding:0 2vw;}}
      .header-content{{height:44px;}}
      .logo{{height:30px; width:30px;}}
      .brand{{font-size:12px;}}
    }}
    @media(max-width:800px){{
      .header-content{{
        flex-direction: column;
        align-items: flex-start;
        height:auto;
        padding: 6px 4px;
        gap: 4px;
      }}
      .logo-area{{gap:6px;}}
      nav{{gap:5px;font-size:12px;}}
      .logo{{height:22px; width:22px;}}
      .brand{{font-size:9.6px;}}
    }}
    @media (max-width: 700px) {{
      main {{padding:0 3vw;}}
      .dragon-flow {{padding-bottom:10px;}}
      .step-card {{ width: 105px; min-width:105px; max-width:105px; height: 78px; }}
      .step-card img {{ height: 30px; }}
      .dragon-arrow .arrow-num{{width:13px;height:13px;font-size:.7em;}}
      .dragon-arrow .arrow-icon{{font-size:1em;}}
    }}
    h2{{ color:var(--primary-blue); border-bottom:2px solid var(--primary-blue); padding-bottom:8px; }}
    .dragon-desc-section {{
      background: #f7fafb;
      border-radius: 10px;
      margin: 40px auto 0 auto;
      padding: 38px 32px 38px 32px;
      font-size: 1.12em;
      color: #284052;
      box-shadow: 0 2px 8px rgba(110,140,180,0.06);
      max-width: 980px;
      line-height: 1.8;
    }}
    .contact-info{{ background:#f2f7fb; padding:20px; border-radius:6px; line-height:1.8; margin-top:40px; }}
    .contact-info a{{ color:var(--primary-blue); text-decoration:none; }}
    .contact-info a:hover{{ text-decoration:underline; }}
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
  // 加工流程支援橫移
  const dragonFlow = document.querySelector('.dragon-flow');
  if(dragonFlow){{
    dragonFlow.addEventListener('wheel', function(e){{
      if (e.deltaY === 0) return;
      e.preventDefault();
      dragonFlow.scrollLeft += e.deltaY;
    }}, {{ passive: false }});
    let isDown = false, startX, scrollLeft;
    dragonFlow.addEventListener('mousedown', function(e){{
      isDown = true;
      dragonFlow.classList.add('dragging');
      startX = e.pageX - dragonFlow.offsetLeft;
      scrollLeft = dragonFlow.scrollLeft;
    }});
    dragonFlow.addEventListener('mouseleave', ()=>{{isDown=false;dragonFlow.classList.remove('dragging');}});
    dragonFlow.addEventListener('mouseup', ()=>{{isDown=false;dragonFlow.classList.remove('dragging');}});
    dragonFlow.addEventListener('mousemove', function(e){{
      if(!isDown)return;
      e.preventDefault();
      const x = e.pageX - dragonFlow.offsetLeft;
      const walk = (x - startX)*1.1;
      dragonFlow.scrollLeft = scrollLeft - walk;
    }});
    // 手機拖動
    let isTouch = false, touchStartX, touchScrollLeft;
    dragonFlow.addEventListener('touchstart', function(e){{
      isTouch = true;
      touchStartX = e.touches[0].pageX;
      touchScrollLeft = dragonFlow.scrollLeft;
    }});
    dragonFlow.addEventListener('touchmove', function(e){{
      if(!isTouch)return;
      const x = e.touches[0].pageX;
      const walk = (x - touchStartX)*1.1;
      dragonFlow.scrollLeft = touchScrollLeft - walk;
    }});
    dragonFlow.addEventListener('touchend', function(){{ isTouch = false;}});
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
    content_html = """
<div style="display: flex; flex-wrap: wrap; gap: 32px 3vw; align-items: flex-start; margin-bottom: 42px;">
  <!-- 左圖 -->
  <div style="flex:1 1 300px; min-width:220px; max-width:370px;">
    <img src="/static/company_entrance.jpg" alt="公司入口" style="width:100%; border-radius:16px; box-shadow: 0 2px 16px rgba(60,90,150,0.14); object-fit:cover;">
  </div>
  <!-- 右文 -->
  <div style="flex:2 1 330px; min-width:240px; max-width:700px;">
    <h3 style="color:#4166a9; font-size:1.44em; margin:0 0 18px 0; letter-spacing:1.2px;">
      關於溍慎有限公司
    </h3>
    <div style="font-size:1.13em; color:#2d425c; line-height:1.92;">
      溍慎有限公司成立於台南，專注於提供專業的表面處理加工服務，擁有多年實務經驗與高效率自動化設備，持續為客戶提供高品質、穩定可靠的技術支援。<br><br>
      我們秉持「品質第一、誠信經營、顧客滿意」的宗旨，並致力於持續創新，成為業界值得信賴的夥伴。
    </div>
  </div>
</div>

<!-- 核心價值環形圖 -->
<div style="display:flex; flex-direction:column; align-items:center; margin: 32px 0 30px 0;">
  <div style="width:360px; max-width:96vw; height:360px; position:relative;">
    <svg viewBox="0 0 360 360" width="360" height="360" style="width:100%;height:100%;">
      <circle cx="180" cy="180" r="145" stroke="#b3d0ea" stroke-width="16" fill="none"/>
      <!-- 四個圓點 -->
      <circle cx="180" cy="40"  r="48" fill="#98ceef"/>
      <circle cx="320" cy="180" r="48" fill="#98ceef"/>
      <circle cx="180" cy="320" r="48" fill="#98ceef"/>
      <circle cx="40"  cy="180" r="48" fill="#98ceef"/>
      <!-- 核心圓 -->
      <circle cx="180" cy="180" r="62" fill="#e51919"/>
      <!-- 文字 -->
      <text x="180" y="186" text-anchor="middle" fill="#fff" font-size="2.2em" font-family="Noto Sans TC,Segoe UI" font-weight="700" dominant-baseline="middle">核心&#10;價值</text>
      <text x="180" y="70" text-anchor="middle" fill="#2d425c" font-size="1.06em" font-family="Noto Sans TC,Segoe UI" font-weight="700">具競爭力的<br/>技術</text>
      <text x="320" y="186" text-anchor="middle" fill="#2d425c" font-size="1.05em" font-family="Noto Sans TC,Segoe UI" font-weight="700">ISO9001<br/>認證</text>
      <text x="180" y="310" text-anchor="middle" fill="#2d425c" font-size="1.05em" font-family="Noto Sans TC,Segoe UI" font-weight="700">環境責任</text>
      <text x="40" y="186" text-anchor="middle" fill="#2d425c" font-size="1.05em" font-family="Noto Sans TC,Segoe UI" font-weight="700">信守承諾</text>
    </svg>
  </div>
</div>

<!-- 補充說明 -->
<div style="background: #f5f7fc; border-radius: 10px; max-width: 900px; margin: 0 auto; padding: 32px 20px 22px 28px; font-size: 1.07em; color: #284052; box-shadow: 0 2px 8px rgba(110,140,180,0.06); line-height: 2;">
  <b style="color:#4166a9;font-size:1.12em;">• 創新</b><br>
  我們持續導入具市場競爭力的技術與自動化設備，包括機械手臂整修工程、兩套含浸自動化生產線、多軸器與龍門式自動化清洗化成產線，提升產能與穩定度。<br><br>
  <b style="color:#4166a9;font-size:1.12em;">• 誠信</b><br>
  以誠待人、信守承諾，加工品皆保留限度樣供品質比對；報價單明確載明各項作業工段，透明化管理流程，建立與客戶間的長期信任。<br><br>
  <b style="color:#4166a9;font-size:1.12em;">• 服務</b><br>
  我們重視每一道作業流程，嚴格遵守ISO 9001品質管理規範，確保提供穩定、可靠的表面處理服務，並持續優化生產與檢驗流程。<br><br>
  <b style="color:#4166a9;font-size:1.12em;">• 永續</b><br>
  公司依法設立並取得合格工廠登記證及廢水排放許可證，廠區具備完善廢水與廢土處理設施，致力於降低對環境的衝擊。
  並定期召開勞資會議，促進員工與公司間的雙向溝通，確保勞資雙方權益，實踐企業社會責任。
</div>
"""
    return render_subpage("關於溍慎", content_html)

@app.route("/process")
def process():
    flow_html = """
<div class="dragon-flow">
  <a href="/robotic" class="step-card" data-aos="zoom-in">
    <img src="/static/robotic.jpg" alt="自動化機械手臂">
    <h3>自動化機械手臂</h3>
    <p>可搭配工具快速作業</p>
  </a>
  <div class="dragon-arrow" data-aos="fade-right">
    <div class="arrow-num">➀</div>
    <div class="arrow-icon">&#8594;</div>
  </div>
  <a href="/vibration" class="step-card" data-aos="zoom-in">
    <img src="/static/vibration.jpg" alt="振動研磨">
    <h3>振動研磨</h3>
    <p>表面均化處理</p>
  </a>
  <div class="dragon-arrow" data-aos="fade-right">
    <div class="arrow-num">➁</div>
    <div class="arrow-icon">&#8594;</div>
  </div>
  <a href="/sealing" class="step-card" data-aos="zoom-in">
    <img src="/static/sealing.jpg" alt="含浸封孔">
    <h3>含浸封孔</h3>
    <p>提升氣密性與耐用性</p>
  </a>
  <div class="dragon-arrow" data-aos="fade-right">
    <div class="arrow-num">➂</div>
    <div class="arrow-icon">&#8594;</div>
  </div>
  <a href="/coating" class="step-card" data-aos="zoom-in">
    <img src="/static/coating.jpg" alt="皮膜化成">
    <h3>皮膜化成</h3>
    <p>依需求選擇性進行</p>
  </a>
  <div class="dragon-arrow" data-aos="fade-right">
    <div class="arrow-num">➃</div>
    <div class="arrow-icon">&#8594;</div>
  </div>
  <a href="/wastewater" class="step-card" data-aos="zoom-in">
    <img src="/static/wastewater.jpg" alt="廢水處理">
    <h3>廢水處理</h3>
    <p>淨化廢水、達標排放</p>
  </a>
</div>
<div class="dragon-desc-section" data-aos="fade-up" style="margin-bottom:20px;">
  <h3 style="color:#4166a9; font-size:1.25em; margin:0 0 18px 0;">加工流程補充說明</h3>
  <p>
    本公司依據 <b>ISO 9001:2015 品質管理系統</b> 作業，從客戶送來的貨件開始，即進行嚴格的<span style="color:#4166a9;"><b>進料檢驗</b></span>。若發現異常情形，如生鏽、碰損或其他瑕疵，會第一時間主動通知廠商，並依廠商決定是否退回或繼續加工。<br><br>
    每一品項皆建立對應的 <b>SOP 標準作業流程</b>，並搭配照片與紀錄，要求所有員工依照流程標準執行，確保加工一致性與品質穩定性。<br><br>
    <b>➀ 初步處理</b>：鑄造完成的工件會產生毛邊，若毛邊過厚、振動研磨無法直接處理，則會先進行前處理（如：機械手臂修整、氣動銼刀修邊），再進入振動研磨程序。<br><br>
    <b>➁ 振動研磨</b>：毛邊去除後，表面會留有加工痕跡，因此透過振動研磨來統一表面質感、修飾瑕疵。部分廠商會於此階段先將工件取回再加工後，重新交由我們執行下一步。<br><br>
    <b>➂ 含浸封孔與皮膜化成</b>：汽車零件常見沙孔問題，若零件需具備氣密性，會進行含浸封孔處理以補強孔隙。考量部分工件需經海運，也會配合進行皮膜化成處理，以提升抗鹽霧腐蝕能力。<br><br>
    <b>➃ 廢水處理</b>：因加工各項程序會需要排放廢水，本公司設有自主管理的廢水處理系統，將所有排出液體集中處理、過濾與排放，符合環保與法規要求。
  </p>
</div>
"""
    return render_subpage("加工流程", flow_html, aos_effect="fade-down")

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
