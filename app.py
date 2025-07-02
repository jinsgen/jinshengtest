from flask import Flask, render_template_string

app = Flask(__name__)

# 首頁 HTML
HOME_HTML = """
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>溍慎/鈦吉有限公司</title>
    <link rel="icon" href="/static/favicon.ico" type="image/x-icon">
    <link href="https://unpkg.com/aos@2.3.4/dist/aos.css" rel="stylesheet">
    <script src="https://unpkg.com/aos@2.3.4/dist/aos.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', () => AOS.init());
    </script>
    <style>
        :root {
            --primary-blue: #6d8ec7;
            --accent-yellow: #FFD85A;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: white;
            scroll-padding-top: 80px;
        }
        header {
            background-color: var(--primary-blue);
            padding: 15px 30px;
            color: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            position: sticky;
            top: 0;
            z-index: 999;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        .brand {
            display: flex;
            align-items: center;
        }
        .brand img {
            height: 60px;
            margin-right: 14px;
        }
        .title {
            font-size: 20px;
            line-height: 1.2;
            white-space: pre-line;
        }
        nav {
            display: flex;
            gap: 15px;
        }
        nav a {
            color: white;
            text-decoration: none;
            font-weight: 600;
            padding: 8px 12px;
            border-radius: 4px;
        }
        nav a:hover {
            background-color: rgba(255,255,255,0.2);
        }
        .banner {
            background-image: url('/static/banner.jpg');
            background-size: cover;
            background-position: center;
            height: 300px;
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 36px;
            font-weight: bold;
            text-shadow: 2px 2px 4px #000;
        }
        main {
            max-width: 1000px;
            margin: 40px auto;
            padding: 0 20px;
        }
        h2 {
            color: var(--primary-blue);
            border-bottom: 2px solid var(--primary-blue);
        }
        .services {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
        }
        .service-item {
            position: relative;
            flex: 1 1 calc(25% - 20px);
            max-width: calc(25% - 20px);
            height: 220px;
            padding: 20px;
            border-radius: 6px;
            color: white;
            background-size: cover;
            background-position: center;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            text-decoration: none;
            overflow: hidden;
            transition: transform 0.3s;
        }
        .service-item:hover {
            transform: scale(1.05);
        }
        .service-item::before {
            content: "";
            position: absolute;
            inset: 0;
            background: rgba(0,0,0,0.45);
            z-index: 0;
        }
        .service-item * {
            position: relative;
            z-index: 1;
        }
        .contact-info {
            background-color: #f2f7fb;
            padding: 20px;
            border-radius: 6px;
            line-height: 1.8;
        }
        .contact-info a {
            color: var(--primary-blue);
            text-decoration: none;
        }
        .contact-info a:hover {
            text-decoration: underline;
        }
        #mobile-footer-nav {
            display: none;
            position: fixed;
            bottom: 0; left: 0; right: 0;
            background-color: var(--primary-blue);
            padding: 8px 0;
            justify-content: space-around;
        }
        #mobile-footer-nav a {
            color: white;
            font-weight: 600;
            text-decoration: none;
            font-size: 14px;
        }
        #topBtn {
            display: none;
            position: fixed;
            bottom: 60px;
            right: 20px;
            background-color: var(--primary-blue);
            color: white;
            padding: 10px 14px;
            border-radius: 50%;
            border: none;
            cursor: pointer;
        }
        @media (max-width: 992px) {
            .service-item {
                flex: 1 1 45%;
                max-width: 45%;
            }
        }
        @media (max-width: 600px) {
            .service-item {
                flex: 1 1 100%;
                max-width: 100%;
            }
            #mobile-footer-nav {
                display: flex;
            }
            #topBtn {
                display: block;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="brand">
            <img src="/static/logo_transparent.png" alt="LOGO">
            <div class="title">溍慎有限公司<br>鈦吉有限公司</div>
        </div>
        <nav>
            <a href="/">首頁</a>
            <a href="/about">關於溍慎</a>
            <a href="#services">服務項目</a>
            <a href="/onedragon">一條龍產線</a>
            <a href="#contact">聯絡我們</a>
        </nav>
    </header>
    <div class="banner" data-aos="fade-in">專業服務，信賴首選</div>
    <main>
        <section id="services">
            <h2 data-aos="fade-up">服務項目</h2>
            <div class="services">
                <a href="/vibration" class="service-item" style="background-image: url('/static/vibration.jpg');" data-aos="zoom-in">
                    <h3>振動研磨</h3>
                    <p>去除毛邊、拋光與表面均化。</p>
                </a>
                <a href="/sealing" class="service-item" style="background-image: url('/static/sealing.jpg');" data-aos="zoom-in">
                    <h3>含浸封孔</h3>
                    <p>提高氣密性與耐用性。</p>
                </a>
                <a href="/coating" class="service-item" style="background-image: url('/static/coating.jpg');" data-aos="zoom-in">
                    <h3>皮膜化成</h3>
                    <p>耐蝕塗裝處理，自動化產線。</p>
                </a>
                <a href="/robotic" class="service-item" style="background-image: url('/static/robotic.jpg');" data-aos="zoom-in">
                    <h3>自動化機械手臂</h3>
                    <p>搭配工具快速作業。</p>
                </a>
                <a href="/wastewater" class="service-item" style="background-image: url('/static/wastewater.jpg');" data-aos="zoom-in">
                    <h3>廢水處理</h3>
                    <p>淨化廢水、達標排放，降低污染。</p>
                </a>
            </div>
        </section>
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
    </main>
    <nav id="mobile-footer-nav">
        <a href="/">首頁</a>
        <a href="/about">關於</a>
        <a href="#services">服務</a>
        <a href="#contact">聯絡</a>
    </nav>
    <button id="topBtn" onclick="window.scrollTo({top: 0, behavior: 'smooth'})">▲</button>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HOME_HTML)

@app.route("/about")
def about():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="zh-Hant">
    <head>
        <meta charset="UTF-8">
        <title>關於溍慎</title>
    </head>
    <body>
        <header style="background:#6d8ec7;color:white;padding:15px 30px;display:flex;justify-content:space-between;">
            <div>關於溍慎</div>
            <a href="/" style="color:white;text-decoration:none;">← 回首頁</a>
        </header>
        <main style="max-width:800px;margin:40px auto;padding:20px;font-family:sans-serif;">
            <h2>我們的使命</h2>
            <p>溍慎有限公司/鈦吉有限公司專注於金屬表面處理，致力於提供穩定、高品質的一站式加工服務。</p>
            <p>我們擁有完整產線與專業人員，可提供彈性化的代工方案，服務產業包含汽車、航太、電子等。</p>
        </main>
        <footer style="background:#f2f7fb;padding:20px;font-family:sans-serif;line-height:1.8;">
            地址：<a href="https://maps.app.goo.gl/8dkFhGhkzxeEaBYaA" target="_blank">台南市仁德區義林路148巷16號</a><br>
            Tel：06-2708989<br>
            Fax：06-2707878<br>
            Mobile：0975124624（鄭先生）<br>
            Email：<a href="mailto:js42915245@gmail.com">js42915245@gmail.com</a>
        </footer>
    </body>
    </html>
    """)

@app.route("/onedragon")
def onedragon():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="zh-Hant">
    <head>
        <meta charset="UTF-8">
        <title>一條龍產線</title>
    </head>
    <body>
        <header style="background:#6d8ec7;color:white;padding:15px 30px;display:flex;justify-content:space-between;">
            <div>一條龍產線服務</div>
            <a href="/" style="color:white;text-decoration:none;">← 回首頁</a>
        </header>
        <main style="max-width:800px;margin:40px auto;padding:20px;font-family:sans-serif;">
            <h2>完整加工流程</h2>
            <ol>
                <li>毛邊去除（可搭配機械手臂）</li>
                <li>振動研磨</li>
                <li>含浸封孔</li>
                <li>皮膜化成（視需求）</li>
            </ol>
            <p>我們提供整合式產線，節省客戶物流時間與管理成本。</p>
        </main>
        <footer style="background:#f2f7fb;padding:20px;font-family:sans-serif;line-height:1.8;">
            地址：<a href="https://maps.app.goo.gl/8dkFhGhkzxeEaBYaA" target="_blank">台南市仁德區義林路148巷16號</a><br>
            Tel：06-2708989<br>
            Fax：06-2707878<br>
            Mobile：0975124624（鄭先生）<br>
            Email：<a href="mailto:js42915245@gmail.com">js42915245@gmail.com</a>
        </footer>
    </body>
    </html>
    """)

if __name__ == '__main__':
    app.run(debug=True)
