from flask import Flask, render_template_string

app = Flask(__name__)

# 共用 Header 與 Footer HTML
HEADER_HTML = """
<header>
    <div class="brand">
        <img src="/static/logo_transparent.png" alt="LOGO" class="logo">
        <div class="title">溍慎有限公司<br>鈦吉有限公司</div>
    </div>
    <nav class="nav-bar">
        <a href="/">首頁</a>
        <a href="/about">關於溍慎</a>
        <a href="/#services">服務項目</a>
        <a href="/onedragon">一條龍產線</a>
        <a href="/#contact">聯絡我們</a>
    </nav>
</header>
"""

FOOTER_HTML = """
<section id="contact" data-aos="fade-up">
    <h2>聯絡資訊</h2>
    <div class="contact-info">
        地址：<a href="https://maps.app.goo.gl/8dkFhGhkzxeEaBYaA" target="_blank">台南市仁德區義林路148巷16號</a><br>
        Tel：06-2708989<br>
        Fax：06-2707878<br>
        Mobile：0975124624（鄭先生）<br>
        Email：<a href="mailto:js42915245@gmail.com">js42915245@gmail.com</a>
    </div>
</section>
"""

# 首頁 HTML
HOME_HTML = f"""
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1"/>
    <title>溍慎/鈦吉有限公司</title>
    <link rel="icon" href="/static/favicon.ico" type="image/x-icon">
    <!-- AOS 動畫 -->
    <link href="https://unpkg.com/aos@2.3.4/dist/aos.css" rel="stylesheet">
    <script src="https://unpkg.com/aos@2.3.4/dist/aos.js"></script>
    <script>document.addEventListener('DOMContentLoaded', () => AOS.init());</script>
    <style>
        :root {{--primary-blue:#6d8ec7;--accent-yellow:#FFD85A;}}
        html {{scroll-padding-top:120px;scroll-behavior:smooth;}}
        body {{margin:0;font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif;background:white;}}
        header {{background:var(--primary-blue);padding:15px 30px;color:white;display:flex;justify-content:space-between;align-items:center;position:sticky;top:0;z-index:999;}}
        .logo {{height:60px;}}
        .nav-bar a {{color:white;text-decoration:none;font-weight:600;padding:8px 12px;border-radius:4px;}}
        .nav-bar a:hover {{background:rgba(255,255,255,0.2);}}
        .banner {{background:var(--accent-yellow);color:var(--primary-blue);height:240px;display:flex;align-items:center;justify-content:center;font-size:36px;font-weight:bold;}}
        main {{max-width:1000px;margin:40px auto;padding:0 20px;}}
        h2 {{color:var(--primary-blue);border-bottom:2px solid var(--primary-blue);padding-bottom:8px;}}
        .services {{display:flex;flex-wrap:wrap;gap:20px;}}
        .service-item {{position:relative;flex:1 1 calc(25%-20px);max-width:calc(25%-20px);height:220px;padding:20px;border-radius:6px;color:white;background-size:cover;background-position:center;display:flex;flex-direction:column;justify-content:flex-end;text-decoration:none;overflow:hidden;transition:transform .3s;}}
        .service-item::before {{content:"";position:absolute;inset:0;background:rgba(0,0,0,0.45);z-index:0;}}
        .service-item:hover {{transform:translateY(-5px) scale(1.02);}}
        .service-item * {{position:relative;z-index:1;}}
        .contact-info a {{color:var(--primary-blue);text-decoration:none;}}
        .contact-info a:hover {{text-decoration:underline;}}
    </style>
</head>
<body>
    {HEADER_HTML}
    <div class="banner" data-aos="fade-in">專業服務，信賴首選</div>
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

# 子頁面渲染函式
def render_subpage(title, content_html, aos="fade-up"):
    return render_template_string(f"""
    <!DOCTYPE html>
    <html lang="zh-Hant">
    <head>
        <meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1"/>
        <title>{title}</title>
        <link rel="icon" href="/static/favicon.ico" type="image/x-icon">
        <link href="https://unpkg.com/aos@2.3.4/dist/aos.css" rel="stylesheet">
        <script src="https://unpkg.com/aos@2.3.4/dist/aos.js"></script>
        <script>document.addEventListener('DOMContentLoaded', () => AOS.init());</script>
        <style>
            :root {{--primary-blue:#6d8ec7;}}
            html {{scroll-padding-top:120px;scroll-behavior:smooth;}}
            body {{margin:0;font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif;background:white;}}
            header {{background:var(--primary-blue);padding:15px 30px;color:white;display:flex;justify-content:space-between;align-items:center;position:sticky;top:0;z-index:999;}}
            .nav-bar a {{color:white;text-decoration:none;font-weight:600;padding:8px 12px;border-radius:4px;}}
            .nav-bar a:hover {{background:rgba(255,255,255,0.2);}}
            main {{max-width:1000px;margin:40px auto;padding:0 20px;}}
            .contact-info {{background:#f2f7fb;padding:20px;border-radius:6px;line-height:1.8;}}
            .contact-info a {{color:var(--primary-blue);text-decoration:none;}}
            .contact-info a:hover {{text-decoration:underline;}}
        </style>
    </head>
    <body>
        {HEADER_HTML}
        <main data-aos="{aos}">
            <h2>{title}</h2>
            {content_html}
        </main>
        {FOOTER_HTML}
    </body>
    </html>
    """)

# 路由配置
@app.route("/")
def home():
    return render_template_string(HOME_HTML)

@app.route("/about")
def about():
    return render_subpage("關於溍慎", "<p>本頁可新增公司介紹內容。</p>")

@app.route("/onedragon")
def onedragon():
    return render_subpage("一條龍產線服務", """
        <ol data-aos="fade-up">
            <li>毛邊去除（可搭配機械手臂）</li>
            <li>振動研磨</li>
            <li>含浸封孔</li>
            <li>皮膜化成（視需求）</li>
        </ol>
        <p data-aos="fade-up">我們提供整合式產線，節省客戶物流時間與管理成本。</p>
    """, aos="fade-down")

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
 ​:contentReference[oaicite:0]{index=0}​
