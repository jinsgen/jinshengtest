from flask import Flask, render_template_string

app = Flask(__name__)

# -----------------------
# 共用 Header & Footer
# -----------------------
HEADER_HTML = """
<header style="background:#6d8ec7; padding:15px 30px; color:white; display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; position:sticky; top:0; z-index:999;">
  <div style="display:flex; align-items:center;">
    <img src="/static/logo_transparent.png" alt="LOGO" style="height:60px; margin-right:14px;">
    <div style="font-size:20px; line-height:1.2; white-space:pre-line;">溍慎有限公司<br>鈦吉有限公司</div>
  </div>
  <nav style="display:flex; gap:15px; flex-wrap:wrap; margin-top:8px;">
    <a href="/"           style="color:white; text-decoration:none; font-weight:600; padding:8px 12px; border-radius:4px;">首頁</a>
    <a href="/about"      style="color:white; text-decoration:none; font-weight:600; padding:8px 12px; border-radius:4px;">關於溍慎</a>
    <a href="/#services"  style="color:white; text-decoration:none; font-weight:600; padding:8px 12px; border-radius:4px;">服務項目</a>
    <a href="/onedragon"  style="color:white; text-decoration:none; font-weight:600; padding:8px 12px; border-radius:4px;">一條龍產線</a>
    <a href="#contact"    style="color:white; text-decoration:none; font-weight:600; padding:8px 12px; border-radius:4px;">聯絡我們</a>
  </nav>
</header>
"""

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
# 首頁 HTML（含打字機動畫及響應式）
# -----------------------
HOME_HTML = f"""
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>溍慎/鈦吉有限公司</title>
<link rel="icon" href="/static/favicon.ico" type="image/x-icon">
<!-- AOS 動畫 -->
<link href="https://unpkg.com/aos@2.3.4/dist/aos.css" rel="stylesheet">
<script src="https://unpkg.com/aos@2.3.4/dist/aos.js"></script>
<script>document.addEventListener('DOMContentLoaded',()=>AOS.init());</script>
<style>
  :root {{
    --primary-blue: #6d8ec7;
    --accent-yellow: #FFD85A;
  }}
  /* 打字機動畫 */
  @keyframes typing {{
    from {{ width: 0; }}
    to   {{ width: 100%; }}
  }}
  @keyframes blink {{
    50% {{ border-color: transparent; }}
  }}
  html {{
    scroll-padding-top: 120px;
    scroll-behavior: smooth;
  }}
  body {{
    margin: 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: white;
  }}
 .banner {
    background-image: url('/static/banner_new.jpg'); /* 換成你的圖片 */
    background-size: cover;
    background-position: center;
    color: white;
    height: 300px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;      /* 🔸讓字水平置中 */
    padding: 0 10px;         /* 🔸防止手機貼邊 */
    text-shadow: 2px 2px 4px rgba(0,0,0,0.6); /* 讓字體清楚 */
}

  .typewriter {{
    overflow: hidden;
    white-space: nowrap;
    border-right: .15em solid var(--primary-blue);
    font-size: 36px;
    font-weight: bold;
    width: 0;
    animation:
      typing 2s steps(30,end) forwards,
      blink .75s step-end infinite;
  }}
  .typewriter.second {{
    /* 與第一行同時打字 */
    animation:
      typing 2s steps(30,end) forwards,
      blink .75s step-end infinite;
  }}
  main {{
    max-width: 1000px;
    margin: 40px auto;
    padding: 0 20px;
  }}
  h2 {{
    color: var(--primary-blue);
    border-bottom: 2px solid var(--primary-blue);
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
    position: absolute; inset: 0;
    background: rgba(0,0,0,0.45); z-index:0;
  }}
  .service-item h3, .service-item p {{
    position: relative; z-index:1; margin:0; color:white;
  }}
  .service-item p {{ font-size:0.9rem; }}
  .service-item:hover {{
    transform: translateY(-5px) scale(1.02);
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
  }}
  /* 手機響應式 */
  @media (max-width: 768px) {{
    .banner {{ height: auto; padding: 30px 10px; }}
    .typewriter, .typewriter.second {{ font-size: 24px; }}
    .services {{ gap: 15px; }}
    .service-item {{ flex: 1 1 calc(50% - 15px); max-width: calc(50% - 15px); }}
  }}
  @media (max-width: 480px) {{
    .typewriter, .typewriter.second {{ font-size: 20px; }}
    .service-item {{ flex: 1 1 100%; max-width: 100%; }}
  }}
</style>
</head>
<body>
  {HEADER_HTML}
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

def render_subpage(title, content_html, aos_effect="fade-up"):
    return render_template_string(f"""
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{title}</title>
<link rel="icon" href="/static/favicon.ico" type="image/x-icon">
<!-- AOS 動畫 -->
<link href="https://unpkg.com/aos@2.3.4/dist/aos.css" rel="stylesheet">
<script src="https://unpkg.com/aos@2.3.4/dist/aos.js"></script>
<script>document.addEventListener('DOMContentLoaded',()=>AOS.init());</script>
<style>
  :root {{ --primary-blue:#6d8ec7; }}
  html {{ scroll-padding-top:120px; scroll-behavior:smooth; }}
  body {{ margin:0; font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif; background:white; }}
  header {{ background:var(--primary-blue); padding:15px 30px; color:white; display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; position:sticky; top:0; z-index:999; }}
  header nav a {{ color:white; text-decoration:none; font-weight:600; padding:8px 12px; border-radius:4px; }}
  header nav a:hover {{ background:rgba(255,255,255,0.2); }}
  main {{ max-width:1000px; margin:40px auto; padding:0 20px; }}
  .contact-info {{ background:#f2f7fb; padding:20px; border-radius:6px; line-height:1.8; }}
  .contact-info a {{ color:var(--primary-blue); text-decoration:none; }}
  .contact-info a:hover {{ text-decoration:underline; }}
</style>
</head>
<body>
  {HEADER_HTML}
  <main data-aos="{aos_effect}">
    <h2>{title}</h2>
    {content_html}
  </main>
  {FOOTER_HTML}
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
<div style="display:flex; flex-wrap:wrap; gap:30px; justify-content:center; max-width:1000px; margin:20px auto;">
  <a href="/robotic" style="width:200px; text-align:center; text-decoration:none;" data-aos="fade-right" data-aos-delay="100">
    <div class="step-card" style="transition:transform .3s, box-shadow .3s;">
      <img src="/static/step1.jpg" alt="毛邊去除" style="width:100%; border-radius:8px; margin-bottom:10px;">
      <h3>毛邊去除</h3><p>可搭配自動化機械手臂</p>
    </div>
  </a>
  <a href="/vibration" style="width:200px; text-align:center; text-decoration:none;" data-aos="fade-right" data-aos-delay="200">
    <div class="step-card" style="transition:transform .3s, box-shadow .3s;">
      <img src="/static/step2.jpg" alt="振動研磨" style="width:100%; border-radius:8px; margin-bottom:10px;">
      <h3>振動研磨</h3><p>表面均化處理</p>
    </div>
  </a>
  <a href="/sealing" style="width:200px; text-align:center; text-decoration:none;" data-aos="fade-right" data-aos-delay="300">
    <div class="step-card" style="transition:transform .3s, box-shadow .3s;">
      <img src="/static/step3.jpg" alt="含浸封孔" style="width:100%; border-radius:8px; margin-bottom:10px;">
      <h3>含浸封孔</h3><p>提升氣密性與耐用性</p>
    </div>
  </a>
  <a href="/coating" style="width:200px; text-align:center; text-decoration:none;" data-aos="fade-right" data-aos-delay="400">
    <div class="step-card" style="transition:transform .3s, box-shadow .3s;">
      <img src="/static/step4.jpg" alt="皮膜化成" style="width:100%; border-radius:8px; margin-bottom:10px;">
      <h3>皮膜化成</h3><p>依需求選擇性進行</p>
    </div>
  </a>
</div>
<p data-aos="fade-up" style="text-align:center;">我們提供整合式產線，節省客戶物流時間與管理成本。</p>
<script>
  document.querySelectorAll('.step-card').forEach(el => {
    el.addEventListener('mouseenter',()=>{
      el.style.transform='translateY(-5px) scale(1.02)';
      el.style.boxShadow='0 8px 20px rgba(0,0,0,0.3)';
    });
    el.addEventListener('mouseleave',()=>{
      el.style.transform='';
      el.style.boxShadow='';
    });
  });
</script>
"""
    return render_subpage("一條龍產線服務", flow_html, aos_effect="fade-down")

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
