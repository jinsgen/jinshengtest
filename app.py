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

    /* Banner（封面）區塊 */
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

    /* 服務項目 五格平均分配+浮動特效+黑色遮罩+文字清楚 */
    .services {{
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 28px;
      margin-top: 48px;
      width: 100%;
    }}
    .service-item {{
      position: relative;
      height: 220px;
      border-radius: 16px;
      overflow: hidden;
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;
      box-shadow: 0 2px 14px rgba(100,130,180,0.10);
      transition: box-shadow .22s, transform .16s;
      display: flex;
      align-items: flex-end;
      justify-content: flex-start;
      cursor: pointer;
      text-decoration: none;
    }}
    .service-item .service-overlay {{
      position: absolute;
      inset: 0;
      background: linear-gradient(to top,rgba(0,0,0,0.44) 80%,rgba(0,0,0,0.06));
      transition: background .24s;
      z-index: 1;
    }}
    .service-item:hover {{
      box-shadow: 0 10px 30px rgba(90,130,200,0.20);
      transform: translateY(-9px) scale(1.038);
    }}
    .service-item:hover .service-overlay {{
      background: linear-gradient(to top,rgba(0,0,0,0.60) 85%,rgba(0,0,0,0.12));
    }}
    .service-texts {{
      position: relative;
      z-index: 2;
      padding: 22px 20px 20px 20px;
      width: 100%;
      color: #fff;
      text-shadow: 0 3px 12px rgba(30,35,60,0.22);
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-end;
    }}
    .service-texts h3 {{
      font-size: 1.21em;
      font-weight: 700;
      margin: 0 0 10px 0;
      letter-spacing: 1.2px;
    }}
    .service-texts p {{
      font-size: 1.04em;
      font-weight: 500;
      margin: 0;
      line-height: 1.7;
    }}
    @media (max-width: 1050px) {{
      .services {{
        grid-template-columns: repeat(2, 1fr);
        gap: 16px;
      }}
      .service-item {{
        height: 140px;
      }}
    }}
    @media (max-width: 650px) {{
      .services {{
        grid-template-columns: 1fr;
        gap: 12px;
      }}
      .service-item {{
        height: 90px;
      }}
      .service-texts h3{{font-size:1.04em;}}
      .service-texts p{{font-size:.93em;}}
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

@app.route("/process")
def process():
    flow_html = """
<style>
.process-scrollbar-wrap {
  overflow-x: auto;
  overflow-y: visible;
  -webkit-overflow-scrolling: touch;
  cursor: grab;
  padding-bottom: 24px;
  margin-bottom: 28px;
}
.process-scrollbar-wrap::-webkit-scrollbar {
  height: 8px;
  background: #eee;
  border-radius: 8px;
}
.process-scrollbar-wrap::-webkit-scrollbar-thumb {
  background: #c5daf5;
  border-radius: 8px;
}
.process-timeline {
  display: flex;
  align-items: center;
  gap: 36px;
  min-width: 850px;
  padding: 16px 0 8px 0;
  user-select: none;
}
.process-step-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #f7fbff;
  border-radius: 18px;
  box-shadow: 0 2px 10px rgba(70,130,200,0.06);
  padding: 16px 18px 14px 18px;
  width: 190px;
  min-width: 190px;
  text-align: center;
  transition: transform 0.19s, box-shadow 0.17s;
  cursor: pointer;
  text-decoration: none;
  color: #183A61;
  position: relative;
  z-index: 1;
}
.process-step-card img {
  width: 110px;
  height: 110px;
  border-radius: 14px;
  object-fit: cover;
  margin-bottom: 18px;
  box-shadow: 0 1px 6px rgba(90,120,150,0.14);
  background: #ddeefd;
}
.process-step-card:hover {
  transform: scale(1.055) translateY(-4px);
  box-shadow: 0 4px 20px rgba(110,140,220,0.16);
  background: #e9f3fd;
  color: #0f2c56;
}
.process-step-title {
  font-weight: bold;
  font-size: 1.09em;
  margin-bottom: 8px;
  color: #4470ad;
  letter-spacing: 0.5px;
}
.process-step-desc {
  font-size: 0.97em;
  color: #385370;
  line-height: 1.7;
  min-height: 34px;
}
.process-arrow-block {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-width: 54px;
  position: relative;
}
.process-arrow-num {
  font-size: 0.98em;
  font-weight: 600;
  background: #6d8ec7;
  color: #fff;
  border-radius: 50%;
  width: 32px; height: 32px;
  display: flex; align-items: center; justify-content: center;
  box-shadow: 0 1px 7px rgba(90,120,180,0.08);
  margin-bottom: 4px;
  z-index: 2;
}
.process-arrow-line {
  width: 54px; height: 6px;
  background: linear-gradient(90deg, #e2edfa 18%, #6d8ec7 94%);
  border-radius: 4px;
  margin-top: -16px;
  margin-bottom: -8px;
  position: relative;
}
@media (max-width: 850px) {
  .process-timeline { min-width: 620px;}
  .process-step-card {width:144px;min-width:144px;}
  .process-step-card img{width:68px;height:68px;}
}
</style>
<div class="process-scrollbar-wrap" id="processTimeline">
  <div class="process-timeline">
    <a href="/robotic" class="process-step-card" tabindex="0">
      <img src="/static/robotic.jpg" alt="自動化機械手臂">
      <div class="process-step-title">自動化機械手臂</div>
      <div class="process-step-desc">可搭配工具快速作業</div>
    </a>
    <div class="process-arrow-block">
      <div class="process-arrow-num">➀</div>
      <div class="process-arrow-line"></div>
    </div>
    <a href="/vibration" class="process-step-card" tabindex="0">
      <img src="/static/vibration.jpg" alt="振動研磨">
      <div class="process-step-title">振動研磨</div>
      <div class="process-step-desc">表面均化處理</div>
    </a>
    <div class="process-arrow-block">
      <div class="process-arrow-num">➁</div>
      <div class="process-arrow-line"></div>
    </div>
    <a href="/sealing" class="process-step-card" tabindex="0">
      <img src="/static/sealing.jpg" alt="含浸封孔">
      <div class="process-step-title">含浸封孔</div>
      <div class="process-step-desc">提升氣密性與耐用性</div>
    </a>
    <div class="process-arrow-block">
      <div class="process-arrow-num">➂</div>
      <div class="process-arrow-line"></div>
    </div>
    <a href="/coating" class="process-step-card" tabindex="0">
      <img src="/static/coating.jpg" alt="皮膜化成">
      <div class="process-step-title">皮膜化成</div>
      <div class="process-step-desc">依需求選擇性進行</div>
    </a>
    <div class="process-arrow-block">
      <div class="process-arrow-num">➃</div>
      <div class="process-arrow-line"></div>
    </div>
    <a href="/wastewater" class="process-step-card" tabindex="0">
      <img src="/static/wastewater.jpg" alt="廢水處理">
      <div class="process-step-title">廢水處理</div>
      <div class="process-step-desc">淨化廢水、達標排放</div>
    </a>
  </div>
</div>
<script>
const wrap = document.getElementById('processTimeline');
wrap.addEventListener('wheel', e => {
  if (e.deltaY === 0) return;
  e.preventDefault();
  wrap.scrollLeft += e.deltaY * 1.15;
});
let isDown = false, startX, scrollLeft;
wrap.addEventListener('mousedown', (e) => {
  isDown = true;
  wrap.classList.add('dragging');
  startX = e.pageX - wrap.offsetLeft;
  scrollLeft = wrap.scrollLeft;
});
wrap.addEventListener('mouseleave', () => {
  isDown = false;
  wrap.classList.remove('dragging');
});
wrap.addEventListener('mouseup', () => {
  isDown = false;
  wrap.classList.remove('dragging');
});
wrap.addEventListener('mousemove', (e) => {
  if (!isDown) return;
  e.preventDefault();
  const x = e.pageX - wrap.offsetLeft;
  const walk = (x - startX) * 1.3;
  wrap.scrollLeft = scrollLeft - walk;
});
</script>
<div class="dragon-desc-section" data-aos="fade-up" style="margin-bottom:20px;
  background:#f2f7fb; padding:28px 26px 18px 28px; border-radius:12px; color:#244560; box-shadow:0 2px 8px rgba(100,130,180,0.09); line-height:2;">
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
<div style="display:flex; flex-direction:column; align-items:center; margin: 32px 0 30px 0; position:relative;">
  <div style="width:360px; max-width:96vw; height:360px; position:relative;">
    <svg viewBox="0 0 360 360" width="360" height="360" style="width:100%;height:100%;position:absolute;top:0;left:0;z-index:0;" data-aos="fade-in">
      <circle cx="180" cy="180" r="145" stroke="#b3d0ea" stroke-width="16" fill="none"/>
    </svg>
    <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);z-index:1;" data-aos="zoom-in" data-aos-delay="100">
      <div style="background:#e51919;color:#fff;text-align:center;font-size:2em;font-weight:700;line-height:1.2;font-family:'Noto Sans TC','Segoe UI',sans-serif;width:124px;height:124px;display:flex;flex-direction:column;align-items:center;justify-content:center;border-radius:50%;box-shadow:0 2px 16px rgba(180,40,50,0.10);">核心<br>價值</div>
    </div>
    <!-- 四個外圓 -->
    <div style="position:absolute;top:-3px;left:50%;transform:translateX(-50%);width:96px;height:96px;z-index:2;" data-aos="fade-down" data-aos-delay="240">
      <div style="background:#98ceef;border-radius:50%;width:96px;height:96px;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(80,130,200,0.08);">
        <span style="font-size:1.07em;color:#294766;font-weight:700;text-align:center;line-height:1.32;white-space:pre-line;">具競爭力的<br>技術</span>
      </div>
    </div>
    <div style="position:absolute;top:50%;left:calc(100% - 3px);transform:translateY(-50%);width:96px;height:96px;z-index:2;" data-aos="fade-left" data-aos-delay="320">
      <div style="background:#98ceef;border-radius:50%;width:96px;height:96px;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(80,130,200,0.08);">
        <span style="font-size:1.04em;color:#294766;font-weight:700;text-align:center;line-height:1.32;white-space:pre-line;">ISO9001<br>認證</span>
      </div>
    </div>
    <div style="position:absolute;bottom:-3px;left:50%;transform:translateX(-50%);width:96px;height:96px;z-index:2;" data-aos="fade-up" data-aos-delay="400">
      <div style="background:#98ceef;border-radius:50%;width:96px;height:96px;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(80,130,200,0.08);">
        <span style="font-size:1.04em;color:#294766;font-weight:700;text-align:center;line-height:1.32;white-space:pre-line;">環境責任</span>
      </div>
    </div>
    <div style="position:absolute;top:50%;left:-3px;transform:translateY(-50%);width:96px;height:96px;z-index:2;" data-aos="fade-right" data-aos-delay="320">
      <div style="background:#98ceef;border-radius:50%;width:96px;height:96px;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(80,130,200,0.08);">
        <span style="font-size:1.04em;color:#294766;font-weight:700;text-align:center;line-height:1.32;white-space:pre-line;">信守承諾</span>
      </div>
    </div>
  </div>
</div>
"""
    return render_subpage("關於溍慎", content_html)

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
