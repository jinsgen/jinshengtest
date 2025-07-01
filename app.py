from flask import Flask, render_template_string
import os

app = Flask(__name__)

# 首頁 HTML
HOME_HTML = """
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>溍慎/鈦吉有限公司</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #004080;
            padding: 15px 30px;
            color: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        header .title {
            margin: 0;
            font-size: 20px;
            line-height: 1.5;
            white-space: pre-line;
        }
        nav a {
            color: white;
            text-decoration: none;
            margin-left: 20px;
            font-weight: 600;
        }
        nav a:hover {
            text-decoration: underline;
        }
        .banner {
            background-image: url('https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1350&q=80');
            background-size: cover;
            background-position: center;
            height: 300px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 36px;
            font-weight: bold;
            text-shadow: 1px 1px 5px rgba(0,0,0,0.7);
        }
        main {
            max-width: 1000px;
            margin: 40px auto;
            padding: 0 20px;
        }
        section {
            margin-bottom: 40px;
        }
        h2 {
            border-bottom: 2px solid #004080;
            padding-bottom: 8px;
            color: #004080;
        }

        .about {
            display: flex;
            flex-wrap: wrap;
            gap: 30px;
        }

        .about p {
            flex: 1 1 400px;
        }

        .about .contact-info {
            flex: 1 1 400px;
            background-color: #f2f7fb;
            padding: 20px;
            border-radius: 6px;
            line-height: 1.8;
        }

        .about .contact-info a {
            display: inline-block;
            margin-top: 10px;
            color: #004080;
            font-weight: bold;
            text-decoration: none;
        }

        .about .contact-info a:hover {
            text-decoration: underline;
        }

        .services {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            justify-content: space-between;
        }

        .service-item {
            position: relative;
            flex: 1 1 calc(25% - 20px);
            max-width: calc(25% - 20px);
            height: 220px;
            padding: 20px;
            border-radius: 6px;
            color: white;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.6);
            box-shadow: 0 0 8px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            text-decoration: none;
            background-size: cover;
            background-position: center;
            overflow: hidden;
        }

        .service-item::before {
            content: "";
            position: absolute;
            inset: 0;
            background: rgba(0, 0, 0, 0.45);
            z-index: 0;
        }

        .service-item * {
            position: relative;
            z-index: 1;
        }

        .service-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
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
        }
    </style>
</head>
<body>
    <header>
        <div class="title">溍慎有限公司<br>鈦吉有限公司</div>
        <nav>
            <a href="/">首頁</a>
            <a href="#about">關於我們</a>
            <a href="#services">服務項目</a>
            <a href="https://www.facebook.com/JinShenTaiji/" target="_blank">聯絡我們</a>
        </nav>
    </header>

    <div class="banner">專業服務，信賴首選</div>

    <main>
        <section id="about">
            <h2>關於我們</h2>
            <div class="about">
                <p>本公司專營鋁合金與鋅合金產品之表面處理，服務內容涵蓋：
                <br>• 振動研磨邊角鈍化
                <br>• 含浸封孔處理
                <br>• 金屬皮膜化成處理</p>
                <div class="contact-info">
                    歡迎洽詢更多資訊<br>
                    地址：台南市仁德區義林路148巷16號<br>
                    電話：06-2708989<br>
                    手機：0975124624（鄭先生）<br>
                    Email：js42915245@gmail.com
                    <br><a href="/certification">▶ 關於證照</a>
                </div>
            </div>
        </section>

        <section id="services">
            <h2>服務項目</h2>
            <div class="services">
                <a href="/vibration" class="service-item" style="background-image: url('/static/vibration.jpg');">
                    <h3>振動研磨</h3>
                    <p>去除毛邊、表面鈍化及拋光、表面均化／去除加工痕跡、細微倒角。</p>
                </a>
                <a href="/sealing" class="service-item" style="background-image: url('/static/sealing.jpg');">
                    <h3>含浸封孔</h3>
                    <p>提高氣密度、降低洩漏量、加強零件強度與耐用性，增加物件穩定性。</p>
                </a>
                <a href="/coating" class="service-item" style="background-image: url('/static/coating.jpg');">
                    <h3>皮膜化成</h3>
                    <p>耐蝕保護、塗裝前處理，全部實現自動化產線。</p>
                </a>
                <a href="/robotic" class="service-item" style="background-image: url('/static/robotic.jpg');">
                    <h3>自動化機械手臂</h3>
                    <p>可搭配砂輪、去毛邊刷、氣動磨筆等工具，快速更換、即插即用。</p>
                </a>
            </div>
        </section>
    </main>
</body>
</html>
"""

# 子頁模板
SUB_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            padding: 40px;
            background-color: #f9f9f9;
            color: #333;
        }
        a {
            text-decoration: none;
            color: #004080;
            font-weight: bold;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
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

@app.route("/certification")
def certification
