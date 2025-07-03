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
    body {{ margin:0; font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif; }}
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

    /* Banner 必須絕對覆蓋頂部，且在 header 下方顯示 */
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
    .slogan-block {{
      margin-right: 9vw;
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      background: rgba(255,255,255,0.22);
      backdrop-filter: blur(7px);
      border-radius: 18px 36px 24px 40px/26px 28px 20px 34px;
      box-shadow: 0 4px 32px 0 rgba(120,145,170,0.13);
      padding: 28px 40px 24px 32px;
      min-width: 320px;
      border: 1.5px solid rgba(140,150,190,0.12);
      /* 溫柔漸變色邊線 */
    }}
    .slogan-line {{
      font-size: 34px;
      font-weight: 700;
      color: #365481;
      letter-spacing: 1.5px;
      margin: 0 0 10px 0;
      text-shadow: 0 1px 8px rgba(255,255,255,0.30),0 2px 12px rgba(109,142,199,0.12);
      line-height: 1.3;
      filter: drop-shadow(0 2px 5px rgba(100,110,130,0.10));
    }}
    .slogan-line:last-child{{margin-bottom:0;}}
    @media(max-width:900px){{
      .banner-bg,.banner-content{{height:200px;}}
      .slogan-block{{padding:16px 24px 14px 16px; min-width:170px;}}
      .slogan-line{{font-size:19px;}}
      .banner-content{{min-height:120px;}}
      .slogan-block{{margin-right:3vw;}}
    }}
    @media(max-width:480px){{
      .banner-bg,.banner-content{{height:110px;}}
      .slogan-block{{padding:7px 10px 8px 10px; min-width:80px;}}
      .slogan-line{{font-size:13px;}}
      .banner-content{{min-height:40px;}}
      .slogan-block{{margin-right:2vw;}}
    }}

    main {{ max-width:1000px; margin:40px auto; padding:0 20px; position:relative; z-index:2; }}
    h2 {{ color:var(--primary-blue); border-bottom:2px solid var(--primary-blue); padding-bottom:8px; }}
    .services {{ display:flex; flex-wrap:wrap; gap:20px; justify-content:center; }}
    .service-item {{
      position:relative; flex:1 1 calc(25% - 20px); max-width:calc(25% - 20px);
      height:220px; padding:20px; border-radius:6px;
      background-size:cover; background-position:center; text-decoration:none;
      overflow:hidden; transition:transform .3s ease,box-shadow .3s ease;
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
  </style>
</head>
<body>
  {HEADER_HOME}
  <div class="banner-bg"></div>
  <div class="banner-content" data-aos="fade-in">
    <div class="slogan-block" data-aos="fade-right" data-aos-delay="200">
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
    :root {{ --primary-blue: #6d8ec7; }}
    html {{ scroll-behavior: smooth; }}
    body {{ margin:0; font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif; }}
    header nav a.nav-link{{ transition:background .2s,transform .1s; color:white; text-decoration:none; font-weight:600; padding:8px 12px; border-radius:4px; margin-left:8px; }}
    header nav a.nav-link:hover{{ background:rgba(255,255,255,0.2); }}
    header nav a.nav-link:active{{ background:rgba(255,255,255,0.4); transform:translateY(2px); }}
    header{{ background:#6d8ec7; padding:15px 30px; color:white; display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; position:sticky; top:0; z-index:10; }}
    main{{ max-width:1000px; margin:40px auto; padding:0 20px; position:relative; z-index:2; }}
    .step-card{{ transition:transform .3s,box-shadow .3s; }}
    .step-card:hover{{ transform:translateY(-5px) scale(1.02); box-shadow:0 8px 20px rgba(0,0,0,0.3); }}
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
<h2 data-aos="fade-down" style="text-align:center;">一條龍加工流程</h2>
<div style="display:flex; flex-wrap:wrap; gap:30px; justify-content:center; margin-top:20px;">
  <a href="/robotic" style="width:200px; text-align:center; text-decoration:none;" data-aos="fade-right" data-aos-delay="100">
    <div class="step-card">
      <img src="/static/step1.jpg" alt="毛邊去除" style="width:100%; border-radius:8px; margin-bottom:10px;">
      <h3>毛邊去除</h3><p>可搭配自動化機械手臂</p>
    </div>
  </a>
  <a href="/vibration" style="width:200px; text-align:center; text-decoration:none;" data-aos="fade-right" data-aos-delay="200">
    <div class="step-card">
      <img src="/static/step2.jpg" alt="振動研磨" style="width:100%; border-radius:8px; margin-bottom:10px;">
      <h3>振動研磨</h3><p>表面均化處理</p>
    </div>
  </a>
  <a href="/sealing" style="width:200px; text-align:center; text-decoration:none;" data-aos="fade-right" data-aos-delay="300">
    <div class="step-card">
      <img src="/static/step3.jpg" alt="含浸封孔" style="width:100%; border-radius:8px; margin-bottom:10px;">
      <h3>含浸封孔</h3><p>提升氣密性與耐用性</p>
    </div>
  </a>
  <a href="/coating" style="width:200px; text-align:center; text-decoration:none;" data-aos="fade-right" data-aos-delay="400">
    <div class="step-card">
      <img src="/static/step4.jpg" alt="皮膜化成" style="width:100%; border-radius:8px; margin-bottom:10px;">
      <h3>皮膜化成</h3><p>依需求選擇性進行</p>
    </div>
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
