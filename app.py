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

HOME_HTML = """
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>溍慎/鈦吉有限公司</title>
  <link rel="icon" href="/static/favicon.ico" type="image/x-icon">
  <link href="https://unpkg.com/aos@2.3.4/dist/aos.css" rel="stylesheet">
  <script src="https://unpkg.com/aos@2.3.4/dist/aos.js"></script>
  <script>document.addEventListener('DOMContentLoaded',function(){{AOS.init({{duration:800,once:true}});}});</script>
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
    .main-header.solid {{ background: #6d8ec7; backdrop-filter: none; }}
    .header-content {{ max-width: 1100px; margin: 0 auto; display: flex; align-items: center; justify-content: space-between; height: 56px; padding: 0 16px; position:relative; }}
    .logo-area {{ display: flex; align-items: center; gap: 14px; min-width:0; }}
    .logo {{ height: 42px; width: 42px; min-width:38px; object-fit: contain; display: block; transition: all 0.2s; }}
    .brand {{ font-size: 1.11rem; line-height: 1.19; font-weight: 700; letter-spacing: 1.1px; white-space: pre-line; text-shadow: 0 2px 6px rgba(30,55,110,0.11); margin-top: 1px; transition: all 0.2s; }}
    nav {{ display: flex; gap: 12px; align-items: center; flex-wrap: wrap; font-size: 1em; transition: all 0.2s; }}
    .nav-link {{ color:white; text-decoration:none; font-weight:600; padding:6px 15px; border-radius:4px; transition: background .2s, transform .1s; font-size: 1em; letter-spacing: 0.5px; }}
    .nav-link:hover {{ background: rgba(255,255,255,0.22); }}
    .nav-link:active {{ background: rgba(255,255,255,0.32); transform: translateY(2px); }}
    .banner-bg {{
      position: absolute; top: 0; left: 0;
      width: 100vw; height: 350px;
      background: url('/static/banner_new.jpg') center center/cover no-repeat;
      z-index: 0;
      min-height: 200px;
      pointer-events: none;
    }}
    .banner-content {{
      position: absolute; top: 0; left: 0; right: 0;
      width: 100vw; height: 350px;
      z-index: 1; display: flex; align-items: center; justify-content: flex-end; pointer-events: none;
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
    /* 上三下二置中 */
    .services {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      grid-template-rows: repeat(2, 1fr);
      gap: 32px 38px;
      margin-top: 48px;
      width: 100%;
      max-width: 1000px;
      min-height: 520px;
    }}
    .service-item {{
      position: relative;
      height: 260px;
      border-radius: 20px;
      overflow: hidden;
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;
      box-shadow: 0 2px 14px rgba(100,130,180,0.12);
      transition: box-shadow .22s, transform .16s;
      display: flex;
      align-items: flex-end;
      justify-content: flex-start;
      cursor: pointer;
      text-decoration: none;
      min-width: 0;
    }}
    .service-item .service-overlay {{
      position: absolute;
      inset: 0;
      background: linear-gradient(to top,rgba(0,0,0,0.49) 80%,rgba(0,0,0,0.08));
      transition: background .24s;
      z-index: 1;
    }}
    .service-item:hover {{
      box-shadow: 0 10px 30px rgba(90,130,200,0.26);
      transform: translateY(-12px) scale(1.045);
    }}
    .service-item:hover .service-overlay {{
      background: linear-gradient(to top,rgba(0,0,0,0.7) 90%,rgba(0,0,0,0.13));
    }}
    .service-texts {{
      position: relative;
      z-index: 2;
      padding: 34px 30px 20px 26px;
      width: 100%;
      color: #fff;
      text-shadow: 0 3px 12px rgba(30,35,60,0.22);
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-end;
    }}
    .service-texts h3 {{
      font-size: 1.32em;
      font-weight: 700;
      margin: 0 0 12px 0;
      letter-spacing: 1.2px;
    }}
    .service-texts p {{
      font-size: 1.12em;
      font-weight: 500;
      margin: 0;
      line-height: 1.7;
    }}
    /* 只顯示下二格在中間 */
    .service-item:nth-child(4) {{ grid-column: 2; grid-row: 2; }}
    .service-item:nth-child(5) {{ grid-column: 3; grid-row: 2; }}
    @media (max-width: 1100px) {{
      .services {{grid-template-columns: repeat(2, 1fr); grid-template-rows: repeat(3,1fr);}}
      .service-item {{height: 190px;}}
      .service-item:nth-child(4) {{ grid-column: 1; grid-row: 3; }}
      .service-item:nth-child(5) {{ grid-column: 2; grid-row: 3; }}
    }}
    @media (max-width: 700px) {{
      .services {{grid-template-columns: 1fr; grid-template-rows: repeat(5,1fr);}}
      .service-item {{height: 140px;}}
      .service-texts h3{{font-size:1.06em;}}
      .service-texts p{{font-size:.93em;}}
      .service-item:nth-child(4) {{ grid-column: 1; grid-row: 4; }}
      .service-item:nth-child(5) {{ grid-column: 1; grid-row: 5; }}
    }}
  </style>
</head>
<body>
  {{header|safe}}
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
          <div class="service-overlay"></div>
          <div class="service-texts">
            <h3>振動研磨</h3>
            <p>去除毛邊、拋光與表面均化。</p>
          </div>
        </a>
        <a href="/sealing" class="service-item" style="background-image:url('/static/sealing.jpg');" data-aos="zoom-in" data-aos-delay="50">
          <div class="service-overlay"></div>
          <div class="service-texts">
            <h3>含浸封孔</h3>
            <p>提高氣密性與耐用性。</p>
          </div>
        </a>
        <a href="/coating" class="service-item" style="background-image:url('/static/coating.jpg');" data-aos="zoom-in" data-aos-delay="100">
          <div class="service-overlay"></div>
          <div class="service-texts">
            <h3>皮膜化成</h3>
            <p>耐蝕塗裝處理，自動化產線。</p>
          </div>
        </a>
        <a href="/robotic" class="service-item" style="background-image:url('/static/robotic.jpg');" data-aos="zoom-in" data-aos-delay="150">
          <div class="service-overlay"></div>
          <div class="service-texts">
            <h3>自動化機械手臂</h3>
            <p>搭配工具快速作業。</p>
          </div>
        </a>
        <a href="/wastewater" class="service-item" style="background-image:url('/static/wastewater.jpg');" data-aos="zoom-in" data-aos-delay="200">
          <div class="service-overlay"></div>
          <div class="service-texts">
            <h3>廢水處理</h3>
            <p>淨化廢水、達標排放。</p>
          </div>
        </a>
      </div>
    </section>
    {{footer|safe}}
  </main>
</body>
</html>
"""

def render_subpage(title, content_html, aos_effect="fade-up"):
    return render_template_string("""
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>{{title}}</title>
  <link rel="icon" href="/static/favicon.ico" type="image/x-icon">
  <link href="https://unpkg.com/aos@2.3.4/dist/aos.css" rel="stylesheet">
  <script src="https://unpkg.com/aos@2.3.4/dist/aos.js"></script>
  <script>document.addEventListener('DOMContentLoaded',function(){{AOS.init({{duration:800,once:true}});}});</script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700&family=Noto+Sans+TC:wght@700&display=swap');
    :root {{ --primary-blue: #6d8ec7; }}
    html {{ scroll-behavior: smooth; }}
    body {{ margin:0; font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif; }}
    .main-header {{ width: 100vw; background: #6d8ec7; color: white; position: sticky; top: 0; z-index: 10; min-width: 320px; font-size: 16px; }}
    .header-content {{ max-width: 1100px; margin: 0 auto; display: flex; align-items: center; justify-content: space-between; height: 56px; padding: 0 16px; }}
    .logo-area {{ display: flex; align-items: center; gap: 14px; min-width:0; }}
    .logo {{ height: 42px; width: 42px; min-width:38px; object-fit: contain; display: block; }}
    .brand {{ font-size: 1.11rem; line-height: 1.19; font-weight: 700; letter-spacing: 1.1px; white-space: pre-line; text-shadow: 0 2px 6px rgba(30,55,110,0.11); margin-top: 1px; }}
    nav {{ display: flex; gap: 12px; align-items: center; flex-wrap: wrap; font-size: 1em; }}
    .nav-link {{ color:white; text-decoration:none; font-weight:600; padding:6px 15px; border-radius:4px; transition: background .2s, transform .1s; font-size: 1em; letter-spacing: 0.5px; }}
    .nav-link:hover {{ background: rgba(255,255,255,0.22); }}
    .nav-link:active {{ background: rgba(255,255,255,0.32); transform: translateY(2px); }}
    main{{ max-width:1100px; margin:40px auto; padding:0 20px; position:relative; z-index:2; }}
  </style>
</head>
<body>
  {{header|safe}}
  <main data-aos="{{aos_effect}}">
    <h2 data-aos="fade-up">{{title}}</h2>
    {{content_html|safe}}
    {{footer|safe}}
  </main>
</body>
</html>
""", header=HEADER_SOLID, footer=FOOTER_HTML, title=title, content_html=content_html, aos_effect=aos_effect)

@app.route("/")
def home():
    return render_template_string(HOME_HTML, header=HEADER_HOME, footer=FOOTER_HTML)

@app.route("/about")
def about():
    content_html = """
<div style="display:flex;flex-wrap:wrap;gap:32px 3vw;align-items:flex-start;margin-bottom:42px;">
  <div style="flex:1 1 300px;min-width:220px;max-width:370px;" data-aos="fade-right">
    <img src="/static/company_entrance.jpg" alt="公司入口" style="width:100%;border-radius:16px;box-shadow:0 2px 16px rgba(60,90,150,0.14);object-fit:cover;">
  </div>
  <div style="flex:2 1 330px;min-width:240px;max-width:700px;" data-aos="fade-left">
    <h3 style="color:#4166a9;font-size:1.44em;margin:0 0 18px 0;letter-spacing:1.2px;">關於溍慎有限公司</h3>
    <div style="font-size:1.13em;color:#2d425c;line-height:1.92;">
      溍慎有限公司自2018年成立於台南，專注於精密零件表面處理與自動化加工，擁有多項先進設備與 ISO 9001 國際認證，為汽車、工業、五金等產業客戶提供穩定可靠、高效率且貼心的解決方案。<br><br>
      我們以「品質第一、誠信經營、持續創新」為核心精神，協助客戶提升競爭力，並積極落實環保與永續理念，成為值得信賴的專業夥伴。
      <div style="margin:22px 0 0 0;font-size:1.03em;line-height:1.7;color:#4470ad;">
        <b>公司資訊：</b><br>
        溍慎有限公司：2018年5月30日（民國107年）<br>
        鈦吉有限公司：2017年7月12日（民國106年）
      </div>
    </div>
  </div>
</div>
<!-- 核心價值圓環 -->
<div style="display:flex; justify-content:center; margin: 38px 0 30px 0; position:relative;">
  <div style="width:360px; max-width:98vw; height:360px; position:relative;">
    <svg viewBox="0 0 360 360" width="360" height="360" style="width:100%;height:100%;position:absolute;top:0;left:0;z-index:0;" data-aos="fade-in">
      <circle cx="180" cy="180" r="145" stroke="#b3d0ea" stroke-width="16" fill="none"/>
    </svg>
    <!-- 中央紅圓 -->
    <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);z-index:1;" data-aos="zoom-in" data-aos-delay="100">
      <div style="background:#e51919;color:#fff;text-align:center;font-size:2em;font-weight:700;line-height:1.2;font-family:'Noto Sans TC','Segoe UI',sans-serif;width:124px;height:124px;display:flex;flex-direction:column;align-items:center;justify-content:center;border-radius:50%;box-shadow:0 2px 16px rgba(180,40,50,0.10);">核心<br>價值</div>
    </div>
    <!-- 四個外圓，左右下移回圓 -->
    <div style="position:absolute;top:14px;left:50%;transform:translateX(-50%);width:96px;height:96px;z-index:2;" data-aos="fade-down" data-aos-delay="240">
      <div style="background:#98ceef;border-radius:50%;width:96px;height:96px;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(80,130,200,0.08);">
        <span style="font-size:1.07em;color:#294766;font-weight:700;text-align:center;line-height:1.32;white-space:pre-line;">具競爭力的<br>技術</span>
      </div>
    </div>
    <div style="position:absolute;top:154px;left:345px;transform:translate(-50%,-50%);width:96px;height:96px;z-index:2;" data-aos="fade-left" data-aos-delay="320">
      <div style="background:#98ceef;border-radius:50%;width:96px;height:96px;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(80,130,200,0.08);">
        <span style="font-size:1.04em;color:#294766;font-weight:700;text-align:center;line-height:1.32;white-space:pre-line;">ISO9001<br>認證</span>
      </div>
    </div>
    <div style="position:absolute;bottom:14px;left:50%;transform:translateX(-50%);width:96px;height:96px;z-index:2;" data-aos="fade-up" data-aos-delay="400">
      <div style="background:#98ceef;border-radius:50%;width:96px;height:96px;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(80,130,200,0.08);">
        <span style="font-size:1.04em;color:#294766;font-weight:700;text-align:center;line-height:1.32;white-space:pre-line;">環境責任</span>
      </div>
    </div>
    <div style="position:absolute;top:154px;left:15px;transform:translate(-50%,-50%);width:96px;height:96px;z-index:2;" data-aos="fade-right" data-aos-delay="320">
      <div style="background:#98ceef;border-radius:50%;width:96px;height:96px;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(80,130,200,0.08);">
        <span style="font-size:1.04em;color:#294766;font-weight:700;text-align:center;line-height:1.32;white-space:pre-line;">信守承諾</span>
      </div>
    </div>
  </div>
</div>
<div style="background:#f2f7fb;border-radius:10px;max-width:900px;margin:0 auto 32px auto;padding:32px 20px 22px 28px;font-size:1.07em;color:#284052;box-shadow:0 2px 8px rgba(110,140,180,0.06);line-height:2;" data-aos="fade-up" data-aos-delay="320">
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

# ...其餘子頁面如 /process 等請用你前面流程的版本...

if __name__ == "__main__":
    app.run(debug=True)
