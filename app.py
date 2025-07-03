from flask import Flask, render_template_string

app = Flask(__name__)

HEADER_HOME = """
<header style="
  background: rgba(109, 142, 199, 0.6);
  padding: 15px 30px;
  color: white;
  display: flex; flex-wrap: wrap;
  justify-content: space-between; align-items: center;
  position: sticky; top: 0; z-index: 10;
  backdrop-filter: blur(4px);
">
  <div style="display:flex; align-items:center;">
    <img src="/static/logo_transparent.png" alt="LOGO" style="height:60px; margin-right:14px;">
    <div style="font-size:20px; line-height:1.2; white-space:pre-line;">
      溍慎有限公司<br>鈦吉有限公司
    </div>
  </div>
  <nav>
    <a href="/"           class="nav-link">首頁</a>
    <a href="/about"      class="nav-link">關於溍慎</a>
    <a href="/#services"  class="nav-link">服務項目</a>
    <a href="/onedragon"  class="nav-link">一條龍產線</a>
    <a href="#contact"    class="nav-link">聯絡我們</a>
  </nav>
</header>
"""

HEADER_SOLID = """
<header style="
  background: #6d8ec7;
  padding: 15px 30px;
  color: white;
  display: flex; flex-wrap: wrap;
  justify-content: space-between; align-items: center;
  position: sticky; top: 0; z-index: 10;
">
  <div style="display:flex; align-items:center;">
    <img src="/static/logo_transparent.png" alt="LOGO" style="height:60px; margin-right:14px;">
    <div style="font-size:20px; line-height:1.2; white-space:pre-line;">
      溍慎有限公司<br>鈦吉有限公司
    </div>
  </div>
  <nav>
    <a href="/"           class="nav-link">首頁</a>
    <a href="/about"      class="nav-link">關於溍慎</a>
    <a href="/#services"  class="nav-link">服務項目</a>
    <a href="/onedragon"  class="nav-link">一條龍產線</a>
    <a href="#contact"    class="nav-link">聯絡我們</a>
  </nav>
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
    :root {{ --primary-blue: #6d8ec7; --accent-yellow: #FFD85A; }}
    html {{ scroll-behavior: smooth; }}
    body {{ margin:0; font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif; background: #fff; }}
    header nav a.nav-link {{
      color:white; text-decoration:none; font-weight:600;
      padding:8px 12px; border-radius:4px; margin-left:8px;
      transition: background .2s, transform .1s;
    }}
    header nav a.nav-link:hover {{
      background: rgba(255,255,255,0.2);
    }}
    header nav a.nav-link:active {{
      background: rgba(255,255,255,0.4);
      transform: translateY(2px);
    }}
    .banner-bg {{
      position: absolute;
      top: 0; left: 0;
      width: 100vw; height: 350px;
      background: url('/static/banner_new.jpg') center center/cover no-repeat;
      z-index: 0;
      min-height: 200px;
      pointer-events: none;
    }}
    .banner-content {{
      position: relative;
      width: 100vw;
      height: 350px;
      z-index: 1;
      display: flex;
      align-items: center;
      justify-content: flex-end;
    }}
    .slogan-group {{
      margin-right: 10vw;
      display: flex;
      flex-direction: column;
      align-items: flex-end;
    }}
    .slogan-line {{
      font-size: 34px;
      font-weight: 700;
      color: #fff;
      letter-spacing: 1.5px;
      margin: 0 0 10px 0;
      line-height: 1.3;
      text-shadow: 0 3px 8px rgba(40,60,90,0.32), 0 2px 8px rgba(0,0,0,0.23);
      background: none;
      border: none;
      padding: 0;
    }}
    .slogan-line:last-child{{margin-bottom:0;}}
    main {{ max-width:1000px; margin:40px auto; padding:0 20px; position:relative; z-index:2; }}
    h2 {{ color:var(--primary-blue); border-bottom:2px solid var(--primary-blue); padding-bottom:8px; }}
    .services {{
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
      justify-content: center;
      margin-bottom: 20px;
    }}
    .service-item {{
      position:relative; flex:1 1 calc(25% - 20px); max-width:calc(25% - 20px);
      height:220px; padding:20px; border-radius:6px;
      background-size:cover; background-position:center; text-decoration:none;
      overflow:hidden; transition:transform .3s ease,box-shadow .3s ease;
      min-width: 180px;
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
    }}
    .service-item::before {{
      content:""; position:absolute; inset:0; background:rgba(0,0,0,0.45); z-index:0;
    }}
    .service-item h3, .service-item p {{ position:relative; z-index:1; margin:0; color:white; }}
    .service-item p {{ font-size:.9rem; }}
    .service-item:hover {{
      transform:translateY(-5px) scale(1.02);
      box-shadow:0 8px 20px rgba(0,0,0,0.3);
    }}
    /* 手機排版優化 */
    @media(max-width:950px){{
      main {{padding:0 2vw;}}
      .service-item{{min-width:130px; height:140px; padding:12px; font-size:13px;}}
      .services {{gap:12px;}}
      .slogan-group{{margin-right:4vw;}}
      .slogan-line{{font-size:20px;}}
      .banner-bg,.banner-content{{height:200px;}}
    }}
    @media(max-width:650px){{
      .banner-bg, .banner-content{{height:110px;}}
      .slogan-line{{font-size:13px;}}
      .slogan-group{{margin-right:2vw;}}
      .services{{
        gap:8px;
      }}
      .service-item{{
        min-width: 99vw;
        max-width: 99vw;
        height:90px;
        padding:8px 12px;
        font-size:11px;
      }}
      .service-item h3, .service-item p {{
        font-size:12px;
      }}
    }}
    @media(max-width:420px){{
      .banner-content{{height:85px;}}
      .service-item{{height: 80px; font-size:10px;}}
      .service-item h3, .service-item p {{
        font-size:10px;
      }}
      .slogan-line{{font-size:10px;}}
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
    # 已加入 .dragon-flow 拖曳和滾輪橫移功能
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
    :root {{ --primary-blue: #6d8ec7; }}
    html {{ scroll-behavior: smooth; }}
    body {{ margin:0; font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif; }}
    header nav a.nav-link{{ transition:background .2s,transform .1s; color:white; text-decoration:none; font-weight:600; padding:8px 12px; border-radius:4px; margin-left:8px; }}
    header nav a.nav-link:hover{{ background:rgba(255,255,255,0.2); }}
    header nav a.nav-link:active{{ background:rgba(255,255,255,0.4); transform:translateY(2px); }}
    header{{ background:#6d8ec7; padding:15px 30px; color:white; display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; position:sticky; top:0; z-index:10; }}
    main{{ max-width:1000px; margin:40px auto; padding:0 20px; position:relative; z-index:2; }}
    .dragon-flow {{
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: flex-start;
      gap: 0;
      overflow-x: auto;
      padding-bottom: 20px;
      margin-bottom: 16px;
      scrollbar-width: thin;
      scrollbar-color: #b1bed7 #f2f7fb;
      -webkit-overflow-scrolling: touch;
      cursor: grab;
      user-select: none;
    }}
    .step-card {{
      width: 200px;
      min-width: 200px;
      max-width: 200px;
      height: 250px;
      box-sizing: border-box;
      margin: 0 14px;
      border-radius: 10px;
      box-shadow: 0 2px 14px rgba(60, 70, 90, 0.11);
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
      transform: translateY(-5px) scale(1.03);
      box-shadow: 0 8px 22px rgba(0,0,0,0.18);
    }}
    .step-card img {{
      width: 100%;
      height: 130px;
      object-fit: cover;
      border-radius: 10px 10px 0 0;
      display: block;
    }}
    .step-card h3, .step-card p {{
      margin: 10px 0 3px 0;
      color: #365481;
      text-align: center;
      z-index: 1;
    }}
    .step-card p {{ font-size: 0.95rem; margin-bottom: 10px; }}
    .dragon-arrow {{
      font-size: 38px;
      color: #6d8ec7;
      margin: 0 6px;
      user-select: none;
      min-width: 38px;
      text-align: center;
      font-weight: 800;
      transition: color 0.2s;
      opacity: 0.92;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}
    @media (max-width: 1150px) {{
      .step-card {{ width: 165px; min-width:165px; max-width:165px; height: 200px; }}
      .step-card img {{ height: 90px; }}
    }}
    @media (max-width: 700px) {{
      main {{padding:0 3vw;}}
      .dragon-flow {{padding-bottom:10px;}}
      .step-card {{ width: 120px; min-width:120px; max-width:120px; height: 145px; }}
      .step-card img {{ height: 55px; }}
      .dragon-arrow {{ font-size: 22px; min-width: 18px; }}
    }}
    h2{{ color:var(--primary-blue); border-bottom:2px solid var(--primary-blue); padding-bottom:8px; }}
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
  // 僅一條龍產線流程支援橫移
  const dragonFlow = document.querySelector('.dragon-flow');
  if(dragonFlow){{
    // 滾輪橫移
    dragonFlow.addEventListener('wheel', function(e){{
      if (e.deltaY === 0) return;
      e.preventDefault();
      dragonFlow.scrollLeft += e.deltaY;
    }}, {{ passive: false }});

    // 拖拉橫移
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
    return render_subpage("關於溍慎", "<p>本頁內容待補充。</p>")

@app.route("/onedragon")
def onedragon():
    flow_html = """
<div class="dragon-flow">
  <a href="/robotic" class="step-card" data-aos="zoom-in">
    <img src="/static/robotic.jpg" alt="自動化機械手臂">
    <h3>自動化機械手臂</h3>
    <p>可搭配工具快速作業</p>
  </a>
  <div class="dragon-arrow" data-aos="fade-right">&#8594;</div>
  <a href="/vibration" class="step-card" data-aos="zoom-in">
    <img src="/static/vibration.jpg" alt="振動研磨">
    <h3>振動研磨</h3>
    <p>表面均化處理</p>
  </a>
  <div class="dragon-arrow" data-aos="fade-right">&#8594;</div>
  <a href="/sealing" class="step-card" data-aos="zoom-in">
    <img src="/static/sealing.jpg" alt="含浸封孔">
    <h3>含浸封孔</h3>
    <p>提升氣密性與耐用性</p>
  </a>
  <div class="dragon-arrow" data-aos="fade-right">&#8594;</div>
  <a href="/coating" class="step-card" data-aos="zoom-in">
    <img src="/static/coating.jpg" alt="皮膜化成">
    <h3>皮膜化成</h3>
    <p>依需求選擇性進行</p>
  </a>
  <div class="dragon-arrow" data-aos="fade-right">&#8594;</div>
  <a href="/wastewater" class="step-card" data-aos="zoom-in">
    <img src="/static/wastewater.jpg" alt="廢水處理">
    <h3>廢水處理</h3>
    <p>淨化廢水、達標排放</p>
  </a>
</div>
<p data-aos="fade-up" style="margin-top:20px; text-align:center;">我們提供整合式產線，節省客戶物流時間與管理成本。</p>
"""
    return render_subpage("一條龍產線服務", flow_html)

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
