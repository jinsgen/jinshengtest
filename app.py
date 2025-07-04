from flask import Flask, render_template_string

app = Flask(__name__)

HEADER_HOME = """
<header class="main-header" style="background:rgba(109, 142, 199, 0.62);color:white;position:sticky;top:0;z-index:10;padding:0;">
  <div class="header-content" style="max-width:1100px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;height:56px;padding:0 16px;">
    <div class="logo-area" style="display:flex;align-items:center;gap:14px;">
      <img src="/static/logo_transparent.png" alt="LOGO" class="logo" style="height:42px;width:42px;object-fit:contain;">
      <div class="brand" style="font-size:1.11rem;font-weight:700;letter-spacing:1.1px;white-space:pre-line;text-shadow:0 2px 6px rgba(30,55,110,0.11);">溍慎有限公司<br>鈦吉有限公司</div>
    </div>
    <nav style="display:flex;gap:12px;align-items:center;">
      <a href="/" class="nav-link" style="color:white;text-decoration:none;font-weight:600;padding:6px 15px;border-radius:4px;">首頁</a>
      <a href="/about" class="nav-link" style="color:white;text-decoration:none;font-weight:600;padding:6px 15px;border-radius:4px;">關於溍慎</a>
      <a href="/#services" class="nav-link" style="color:white;text-decoration:none;font-weight:600;padding:6px 15px;border-radius:4px;">服務項目</a>
      <a href="/process" class="nav-link" style="color:white;text-decoration:none;font-weight:600;padding:6px 15px;border-radius:4px;">加工流程</a>
      <a href="#contact" class="nav-link" style="color:white;text-decoration:none;font-weight:600;padding:6px 15px;border-radius:4px;">聯絡我們</a>
    </nav>
  </div>
</header>
"""
FOOTER_HTML = """
<footer id="contact" style="background:#f2f7fb;padding:20px;font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif;line-height:1.8;margin-top:40px;">
  <h2 style="color:#6d8ec7;border-bottom:2px solid #6d8ec7;padding-bottom:8px;margin-top:0;">聯絡資訊</h2>
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
  <style>
    html { scroll-behavior: smooth; }
    body { margin:0; font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif; background: #fff; }
    .banner-bg {
      position: absolute; top: 0; left: 0; width: 100vw; height: 350px;
      background: url('/static/banner_new.jpg') center center/cover no-repeat; z-index: 0;
      min-height: 200px; pointer-events: none;
    }
    .banner-content {
      position: absolute; top: 0; left: 0; right: 0; width: 100vw; height: 350px; z-index: 1;
      display: flex; align-items: center; justify-content: flex-end; pointer-events: none;
    }
    .slogan-group {
      margin-right: 10vw; display: flex; flex-direction: column; align-items: flex-end; justify-content: center; height: 100%; pointer-events: none;
    }
    .slogan-line {
      font-size: 54px; font-family: 'Montserrat', 'Noto Sans TC', sans-serif; font-weight: 700; color: #fff;
      letter-spacing: 1.2px; margin: 0 0 16px 0; line-height: 1.15;
      text-shadow: 0 3px 12px rgba(40,60,90,0.32), 0 2px 8px rgba(0,0,0,0.18); background: none; border: none; padding: 0; white-space: nowrap;
    }
    .slogan-line:last-child{margin-bottom:0;}
    main { max-width:1200px; margin:400px auto 0 auto; padding:0 20px; position:relative; z-index:2; }
    h2 { color:#6d8ec7; border-bottom:2px solid #6d8ec7; padding-bottom:8px; }
    /* 五格上三下二+居中 */
    .services {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      grid-template-rows: repeat(2, 1fr);
      gap: 32px 38px;
      margin-top: 48px;
      width: 100%;
      max-width: 1000px;
      min-height: 520px;
    }
    .service-item {
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
    }
    .service-item .service-overlay {
      position: absolute; inset: 0;
      background: linear-gradient(to top,rgba(0,0,0,0.49) 80%,rgba(0,0,0,0.08));
      transition: background .24s;
      z-index: 1;
    }
    .service-item:hover {
      box-shadow: 0 10px 30px rgba(90,130,200,0.26);
      transform: translateY(-12px) scale(1.045);
    }
    .service-item:hover .service-overlay {
      background: linear-gradient(to top,rgba(0,0,0,0.7) 90%,rgba(0,0,0,0.13));
    }
    .service-texts {
      position: relative; z-index: 2; padding: 34px 30px 20px 26px; width: 100%;
      color: #fff; text-shadow: 0 3px 12px rgba(30,35,60,0.22);
      display: flex; flex-direction: column; align-items: flex-start; justify-content: flex-end;
    }
    .service-texts h3 { font-size: 1.32em; font-weight: 700; margin: 0 0 12px 0; letter-spacing: 1.2px;}
    .service-texts p { font-size: 1.12em; font-weight: 500; margin: 0; line-height: 1.7;}
    /* 下二格居中 */
    .service-item:nth-child(4) { grid-column:2; grid-row:2; }
    .service-item:nth-child(5) { grid-column:3; grid-row:2; }
    @media (max-width: 1100px) {
      .services {grid-template-columns: repeat(2, 1fr); grid-template-rows: repeat(3,1fr);}
      .service-item {height: 190px;}
      .service-item:nth-child(4) { grid-column: 1; grid-row: 3; }
      .service-item:nth-child(5) { grid-column: 2; grid-row: 3; }
    }
    @media (max-width: 700px) {
      .services {grid-template-columns: 1fr; grid-template-rows: repeat(5,1fr);}
      .service-item {height: 140px;}
      .service-texts h3{font-size:1.06em;}
      .service-texts p{font-size:.93em;}
      .service-item:nth-child(4) { grid-column: 1; grid-row: 4; }
      .service-item:nth-child(5) { grid-column: 1; grid-row: 5; }
    }
  </style>
</head>
<body>
  {{ header|safe }}
  <div class="banner-bg"></div>
  <div class="banner-content">
    <div class="slogan-group">
      <div class="slogan-line">溍於專業，慎於品質</div>
      <div class="slogan-line">鈦造未來，吉刻成型</div>
    </div>
  </div>
  <main>
    <section id="services">
      <h2>服務項目</h2>
      <div class="services">
        <a href="/vibration" class="service-item" style="background-image:url('/static/vibration.jpg');">
          <div class="service-overlay"></div>
          <div class="service-texts">
            <h3>振動研磨</h3>
            <p>去除毛邊、拋光與表面均化。</p>
          </div>
        </a>
        <a href="/sealing" class="service-item" style="background-image:url('/static/sealing.jpg');">
          <div class="service-overlay"></div>
          <div class="service-texts">
            <h3>含浸封孔</h3>
            <p>提高氣密性與耐用性。</p>
          </div>
        </a>
        <a href="/coating" class="service-item" style="background-image:url('/static/coating.jpg');">
          <div class="service-overlay"></div>
          <div class="service-texts">
            <h3>皮膜化成</h3>
            <p>耐蝕塗裝處理，自動化產線。</p>
          </div>
        </a>
        <a href="/robotic" class="service-item" style="background-image:url('/static/robotic.jpg');">
          <div class="service-overlay"></div>
          <div class="service-texts">
            <h3>自動化機械手臂</h3>
            <p>搭配工具快速作業。</p>
          </div>
        </a>
        <a href="/wastewater" class="service-item" style="background-image:url('/static/wastewater.jpg');">
          <div class="service-overlay"></div>
          <div class="service-texts">
            <h3>廢水處理</h3>
            <p>淨化廢水、達標排放。</p>
          </div>
        </a>
      </div>
    </section>
    {{ footer|safe }}
  </main>
</body>
</html>
"""

ABOUT_HTML = """
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>關於溍慎</title>
  <style>
    .core-group { display:flex; justify-content:center; margin:40px 0; }
    .circle-main { position:relative; width:360px; height:360px;}
    .core-circle {
      position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
      background:#e51919;color:white;width:124px;height:124px;border-radius:50%;
      display:flex;align-items:center;justify-content:center;font-weight:bold;font-size:1.4em;z-index:2;box-shadow:0 2px 12px #fbb;
      flex-direction:column;text-align:center;
    }
    .outer-circle {
      position:absolute;width:96px;height:96px;border-radius:50%;background:#98ceef;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px #abd;
      color:#294766;font-weight:bold;font-size:1.04em;white-space:pre-line;text-align:center;
    }
    .outer1 {top:18px;left:50%;transform:translateX(-50%);}
    .outer2 {top:152px;left:343px;transform:translate(-50%,-50%);}
    .outer3 {bottom:18px;left:50%;transform:translateX(-50%);}
    .outer4 {top:152px;left:17px;transform:translate(-50%,-50%);}
    @media(max-width:500px) {
      .circle-main { width:220px;height:220px; }
      .outer-circle {width:60px;height:60px;font-size:.78em;}
      .core-circle {width:76px;height:76px;font-size:.9em;}
      .outer2,.outer4 {top:90px;}
    }
  </style>
</head>
<body>
  {{ header|safe }}
  <div style="max-width:800px;margin:50px auto 0 auto;">
    <div style="color:#4470ad;font-size:1.33em;text-align:center;font-weight:bold;">溍慎有限公司 關於我們</div>
    <div class="core-group">
      <div class="circle-main">
        <div class="core-circle">核心<br>價值</div>
        <div class="outer-circle outer1">具競爭力的<br>技術</div>
        <div class="outer-circle outer2">ISO9001<br>認證</div>
        <div class="outer-circle outer3">環境責任</div>
        <div class="outer-circle outer4">信守承諾</div>
      </div>
    </div>
    <div style="background:#f2f7fb;border-radius:10px;max-width:900px;margin:0 auto 32px auto;padding:32px 20px 22px 28px;font-size:1.07em;color:#284052;box-shadow:0 2px 8px rgba(110,140,180,0.06);line-height:2;">
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
  </div>
  {{ footer|safe }}
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HOME_HTML, header=HEADER_HOME, footer=FOOTER_HTML)

@app.route("/about")
def about():
    return render_template_string(ABOUT_HTML, header=HEADER_HOME, footer=FOOTER_HTML)

if __name__ == "__main__":
    app.run(debug=True)
