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
  {{HEADER_HOME}}
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
    {{FOOTER_HTML}}
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
    ...（同上 CSS 不再重複貼）
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
""", HEADER_SOLID=HEADER_SOLID, FOOTER_HTML=FOOTER_HTML)

@app.route("/")
def home():
    return render_template_string(HOME_HTML, HEADER_HOME=HEADER_HOME, FOOTER_HTML=FOOTER_HTML)

@app.route("/about")
def about():
    core_diagram_html = """
<div class="aboutus-mainblock">
  <div class="aboutus-imageblock">
    <img src="/static/company_entrance.jpg" alt="公司門口照">
  </div>
  <div class="aboutus-textblock">
    <h2>關於我們</h2>
    <div class="aboutus-intro">
      <p>
        <b>溍慎有限公司</b>（2018年成立）、<b>鈦吉有限公司</b>（2017年成立），位於台南仁德，專精於汽機車零組件及五金加工品的表面處理與後製加工，提供一站式振動研磨、含浸封孔、皮膜化成、自動化修邊、廢水處理等完整服務。<br><br>
        公司持續導入創新自動化設備，堅持「溍於專業，慎於品質」，以高品質、穩定可靠的工藝與管理，獲得眾多客戶長期肯定。<br><br>
        全面導入 <b>ISO 9001:2015 品質管理系統</b>，並依法取得工廠登記證、廢水排放許可證，落實企業社會責任。
      </p>
      <div style="font-size:1em; color:#6d8ec7; margin-top:20px;">
        成立日期：<br>
        溍慎有限公司 — 2018年5月30日（民國107年）<br>
        鈦吉有限公司 — 2017年7月12日（民國106年）
      </div>
    </div>
  </div>
</div>
<div class="core-value-section">
  <div class="core-diagram-wrap">
    <svg class="core-curve" viewBox="0 0 380 380">
      <circle cx="190" cy="190" r="150" fill="none" stroke="#bfd4e6" stroke-width="14"/>
    </svg>
    <div class="core-center">核心<br>價值</div>
    <div class="core-point core-point1">具競爭力的技術</div>
    <div class="core-point core-point2">ISO9001<br>證證</div>
    <div class="core-point core-point3">環境責任</div>
    <div class="core-point core-point4">信守承諾</div>
  </div>
</div>
<section class="aboutus-philosophy">
  <ul>
    <li><strong>創新</strong>：持續導入具市場競爭力的技術與自動化設備，包括機械手臂整修工程、含浸自動化生產線、多軸器與自動化清洗化成產線，全面提升產能與穩定度。</li>
    <li><strong>誠信</strong>：以誠待人、信守承諾，加工品保留限度樣供品質比對，報價單明確載明各工段，流程透明，與客戶建立長期互信。</li>
    <li><strong>服務</strong>：嚴格遵守ISO 9001品質管理規範，建立SOP與檢驗制度，確保穩定可靠的表面處理品質，不斷優化生產流程。</li>
    <li><strong>永續</strong>：合法設立並取得合格工廠登記證及廢水排放許可，廠區配備完善的廢水、廢土處理設施，致力於降低對環境衝擊。定期勞資會議，確保勞資雙方權益，落實企業社會責任。</li>
  </ul>
</section>
"""
    return render_subpage("關於溍慎", core_diagram_html, aos_effect="fade-up")

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
  <h3 style="color:#4166a9; font-size:1.12em; margin:0 0 15px 0;">加工流程補充說明</h3>
  <p>
    我們公司依據 <b>ISO 9001:2015 品質管理系統</b> 作業，從客戶送來的貨件開始，即進行嚴格的<span style="color:#4166a9;"><b>進料檢驗</b></span>。若發現異常情形，如生鏽、碰損或其他瑕疵，會第一時間主動通知廠商，並依廠商決定是否退回或繼續加工。<br><br>
    每一品項皆建立對應的 <b>SOP 標準作業流程</b>，並搭配照片與紀錄，要求所有員工依照流程標準執行，確保加工一致性與品質穩定性。<br><br>
    <b>➀ 初步處理</b>：鑄造完成的工件會產生毛邊，若毛邊過厚、振動研磨無法直接處理，則會先進行前處理（如：機械手臂修整、氣動銼刀修邊），再進入振動研磨程序。<br><br>
    <b>➁ 振動研磨</b>：毛邊去除後，表面會留有加工痕跡，因此透過振動研磨來統一表面質感、修飾瑕疵。部分廠商會於此階段先將工件取回再加工後，重新交由我們執行下一步。<br><br>
    <b>➂ 含浸封孔與皮膜化成</b>：汽車零件常見沙孔問題，若零件需具備氣密性，會進行含浸封孔處理以補強孔隙。考量部分工件需經海運，也會配合進行皮膜化成處理，以提升抗鹽霧腐蝕能力。<br><br>
    <b>➃ 廢水處理</b>：加工過程會有廢水產生，本公司設有自主管理的廢水處理系統，將所有排出液體集中處理、過濾與排放，符合環保與法規要求。
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
