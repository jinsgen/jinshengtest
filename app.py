from flask import Flask, render_template_string

app = Flask(__name__)

HOME_HTML = """
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>溍慎/鈦吉有限公司</title>
    <style>
        :root {
            --primary-blue: #004080;
            --accent-yellow: #FFC107;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: var(--primary-blue);
            padding: 15px 30px;
            color: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
        }
        .brand {
            display: flex;
            align-items: center;
        }
        .brand img {
            height: 40px;
            margin-right: 10px;
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
            background-color: var(--accent-yellow);
            color: var(--primary-blue);
            height: 200px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 36px;
            font-weight: bold;
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

        /* 手機底部導航 */
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
            <img src="/static/logo.png" alt="LOGO">
            <div class="title">溍慎有限公司<br>鈦吉有限公司</div>
        </div>
        <nav>
            <a href="/">首頁</a>
            <a href="#about">關於溍慎</a>
            <a href="#services">服務項目</a>
            <a href="#contact">聯絡我們</a>
        </nav>
    </header>

    <div class="banner">專業服務，信賴首選</div>

    <main>
        <section id="about">
            <h2>關於溍慎</h2>
            <p>本公司專營鋁合金與鋅合金產品之表面處理，服務內容涵蓋振動研磨、含浸封孔、金屬皮膜化成處理等。</p>
        </section>

        <section id="services">
            <h2>服務項目</h2>
            <div class="services">
                <a href="/vibration" class="service-item" style="background-image: url('/static/vibration.jpg');">
                    <h3>振動研磨</h3>
                    <p>去除毛邊、拋光與表面均化。</p>
                </a>
                <a href="/sealing" class="service-item" style="background-image: url('/static/sealing.jpg');">
                    <h3>含浸封孔</h3>
                    <p>提高氣密性與耐用性。</p>
                </a>
                <a href="/coating" class="service-item" style="background-image: url('/static/coating.jpg');">
                    <h3>皮膜化成</h3>
                    <p>耐蝕塗裝處理，自動化產線。</p>
                </a>
                <a href="/robotic" class="service-item" style="background-image: url('/static/robotic.jpg');">
                    <h3>自動化機械手臂</h3>
                    <p>搭配工具快速作業。</p>
                </a>
                <a href="/wastewater" class="service-item" style="background-image: url('/static/wastewater.jpg');">
                    <h3>廢水處理</h3>
                    <p>淨化廢水、達標排放，降低污染。</p>
                </a>
            </div>
        </section>

        <section id="contact">
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

    <!-- 手機底部導航 -->
    <nav id="mobile-footer-nav">
        <a href="/">首頁</a>
        <a href="#about">關於</a>
        <a href="#services">服務</a>
        <a href="#contact">聯絡</a>
    </nav>

    <!-- 返回頂端 -->
    <button id="topBtn" onclick="window.scrollTo({top: 0, behavior: 'smooth'})">▲</button>
</body>
</html>
"""

SUB_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>
    <p>這是「{{ title }}」頁面的內容。</p>
    <p><a href="/">← 回首頁</a></p>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HOME_HTML)

@app.route("/vibration")
def vibration():
    return render_template_string(SUB_TEMPLATE, title="振動研磨")

@app.route("/sealing")
def sealing():
    return render_template_string(SUB_TEMPLATE, title="含浸封孔")

@app.route("/coating")
def coating():
    return render_template_string(SUB_TEMPLATE, title="皮膜化成")

@app.route("/robotic")
def robotic():
    return render_template_string(SUB_TEMPLATE, title="自動化機械手臂")

@app.route("/wastewater")
def wastewater():
    return render_template_string(SUB_TEMPLATE, title="廢水處理")

@app.route("/certification")
def certification():
    return render_template_string(SUB_TEMPLATE, title="關於證照")

if __name__ == "__main__":
    app.run(debug=True)
