from flask import Flask, render_template_string

app = Flask(__name__)

# -----------------------
# 共用 Footer（所有頁面共用）
# -----------------------
FOOTER_HTML = """
<footer id="contact" style="background:#f2f7fb; padding:20px; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height:1.8;">
  地址：<a href="https://maps.app.goo.gl/8dkFhGhkzxeEaBYaA" target="_blank">台南市仁德區義林路148巷16號</a><br>
  Tel：06-2708989<br>
  Fax：06-2707878<br>
  Mobile：0975124624（鄭先生）<br>
  Email：<a href="mailto:js42915245@gmail.com">js42915245@gmail.com</a>
</footer>
"""

# -----------------------
# 半透明 Header（首頁專用）
# -----------------------
HEADER_TRANSPARENT = """
<header style="
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  background: rgba(109, 142, 199, 0.6);
  padding:15px 30px;
  color:white;
  display:flex;
  flex-wrap:wrap;
  justify-content:space-between;
  align-items:center;
  z-index:999;
  box-sizing:border-box;
">
  <div style="display:flex; align-items:center;">
    <img src="/static/logo_transparent.png" alt="LOGO" style="height:60px; margin-right:14px;">
    <div style="font-size:20px; line-height:1.2; white-space:pre-line;">溍慎有限公司<br>鈦吉有限公司</div>
  </div>
  <nav style="display:flex; gap:15px; flex-wrap:wrap; margin-top:8px;">
    <a href="/"           style="color:white; text-decoration:none; font-weight:600; padding:8px 12px;">首頁</a>
    <a href="/about"      style="color:white; text-decoration:none; font-weight:600; padding:8px 12px;">關於溍慎</a>
    <a href="/#services"  style="color:white; text-decoration:none; font-weight:600; padding:8px 12px;">服務項目</a>
    <a href="/onedragon"  style="color:white; text-decoration:none; font-weight:600; padding:8px 12px;">一條龍產線</a>
    <a href="/#contact"   style="color:white; text-decoration:none; font-weight:600; padding:8px 12px;">聯絡我們</a>
  </nav>
</header>
"""

# -----------------------
# 實心 Header（子頁面專用）
# -----------------------
HEADER_SOLID = HEADER_TRANSPARENT.replace("background: rgba(109, 142, 199, 0.6);", "background: #6d8ec7;")

# -----------------------
# 首頁 HTML
# -----------------------
HOME_HTML = f"""
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>溍慎/鈦吉有限公司</title>
  <link rel="icon" href="/static/favicon.ico" type="image/x-icon">
  <link href="https://unpkg.com/aos@2.3.4/dist/aos.css" rel="stylesheet">
  <script src="https://unpkg.com/aos@2.3.4/dist/aos.js"></script>
  <script>document.addEventListener('DOMContentLoaded', ()=>AOS.init());</script>
  <style>
    html {{ scroll-padding-top: 120px; scroll-behavior: smooth; }}
    body {{
      margin: 0;
      padding-top: 90px;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: white;
    }}
    .banner {{
      margin-top: -90px;
      padding-top: 90px;
      height: 390px;
      background-image: url('/static/banner_new.jpg');
      background-size: cover;
      background-position: center;
      color: white;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding-left: 10px; padding-right: 10px;
      text-shadow: 2px 2px 4px rgba(0,0,0,0.6);
    }}
    @keyframes typing {{ from {{ width: 0; }} to {{ width: 100%; }} }}
    @keyframes blink {{ 50% {{ border-color: transparent; }} }}
    .typewriter {{
      overflow: hidden;
      white-space: nowrap;
      border-right: .15em solid #6d8ec7;
      font-size: 36px;
      font-weight: bold;
      width: 0;
      animation:
        typing 2s steps(30,end) forwards,
        blink .75s step-end infinite;
    }}
    .typewriter.second {{ animation-delay: 2.2s; animation-fill-mode: forwards; }}
    main {{
      max-width: 1000px;
      margin: 40px auto;
      padding: 0 20px;
    }}
    h2 {{
      color: #6d8ec7;
      border-bottom: 2px solid #6d8ec7;
      padding-bottom: 8px;
    }}
    .services {{
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
    }}
    .service-item {{
      position: relative;
      flex: 1 1 calc(25% - 20px);
      max-width: calc(25% - 20px);
      height: 220px;
      padding: 20px;
      border-radius: 6px;
      background-size: cover;
      background-position: center;
      text-decoration: none;
      overflow: hidden;
      transition: transform .3s ease, box-shadow .3s ease;
    }}
    .service-item::before {{
      content: "";
      position: absolute;
      inset: 0;
      background: rgba(0,0,0,0.45);
      z-index: 0;
    }}
    .service-item h3, .service-item p {{
      position: relative;
      z-index: 1;
      margin: 0;
      color: white;
    }}
    .service-item:hover {{
      transform: translateY(-5px) scale(1.02);
      box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    }}
    @media (max-width: 768px) {{
      .banner {{ height: auto; padding: 90px 10px 30px; }}
      .typewriter, .typewriter.second {{ font-size: 24px; }}
      .service-item {{ flex: 1 1 calc(50% - 15px); max-width: calc(50% - 15px); }}
    }}
    @media (max-width: 480px) {{
      .typewriter, .typewriter.second {{ font-size: 20px; }}
      .service-item {{ flex: 1 1 100%; max-width: 100%; }}
    }}
  </style>
</head>
<body>
  {HEADER_TRANSPARENT}
  <div class="banner">
    <div class="typewriter" data-aos="fade-in">溍於專業，慎於品質</div>
    <div class="typewriter second" data-aos="fade-in">鈦造未來，吉刻成型</div>
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

# -----------------------
# 共用 Subpage HTML
# -----------------------
def render_subpage(title, content_html, aos_effect="fade-up"):
    return render_template_string(f"""
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>{title}</title>
  <link rel="icon" href="/static/favicon.ico" type="image/x-icon">
  <link href="https://unpkg.com/aos@2.3.4/dist/aos.css" rel="stylesheet">
  <script src="https://unpkg.com/aos@2.3.4/dist/aos.js"></script>
  <script>document.addEventListener('DOMContentLoaded',()=>AOS.init());</script>
  <style>
    html {{ scroll-padding-top: 120px; scroll-behavior: smooth; }}
    body {{
      margin: 0;
      padding-top: 90px;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: white;
    }}
    header {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      background: #6d8ec7;
      padding: 15px 30px;
      color: white;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      z-index: 999;
      box-sizing: border-box;
    }}
    nav a {{
      color: white;
      text-decoration: none;
      font-weight: 600;
      padding: 8px 12px;
    }}
    main {{
      max-width: 1000px;
      margin: 40px auto;
      padding: 0 20px;
    }}
  </style>
</head>
<body>
  {HEADER_SOLID}
  <main data-aos="{aos_effect}">
    <h2>{title}</h2>
    {content_html}
  </main>
  {FOOTER_HTML}
</body>
</html>
""")

# -----------------------
# Flask Routes
# -----------------------
@app.route("/")
def home():
    return render_template_string(HOME_HTML)

@app.route("/about")
def about():
    return render_subpage("關於溍慎", "<p>本頁內容待補充。</p>")

@app.route("/onedragon")
def onedragon():
    flow_html = """
<p>我們的一條龍產線提供毛邊處理、振動研磨、封孔、皮膜化成等完整製程。</p>
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
