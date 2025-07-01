from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>溍慎鈦吉有限公司</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 0; }
        header {
            background-color: #004080;
            padding: 15px 30px;
            color: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        header h1 {
            margin: 0;
            font-size: 24px;
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
        .services {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
        }
        .service-item {
            flex: 1 1 calc(25% - 20px);
            background: #f0f4f8;
            padding: 20px;
            border-radius: 6px;
            box-shadow: 0 0 8px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
            text-decoration: none;
            color: inherit;
        }
        .service-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
            cursor: pointer;
        }
        @media (max-width: 768px) {
            .service-item {
                flex: 1 1 100%;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>溍慎鈦吉有限公司</h1>
        <nav>
            <a href="/">首頁</a>
            <a href="#about">關於我們</a>
            <a href="#services">服務項目</a>
            <a href="https://www.facebook.com/JinShenTaiji/" target="_blank" rel="noopener noreferrer">聯絡我們</a>
        </nav>
    </header>

    <div class="banner">專業服務，信賴首選</div>

    <main>
        <section id="about">
            <h2>關於我們</h2>
            <p>本公司專營鋁合金與鋅合金產品之表面處理，服務內容涵蓋：</p>
            <ul>
                <li>振動研磨邊角鈍化</li>
                <li>含浸封孔處理</li>
                <li>金屬皮膜化成處理</li>
            </ul>
        </section>

        <section id="services">
            <h2>服務項目</h2>
            <div class="services">
                <a href="/vibration" class="service-item">
                    <h3>振動研磨</h3>
                    <p>去除毛邊、表面鈍化及拋光、表面均化／去除加工痕跡、細微倒角。</p>
                </a>
                <a href="/sealing" class="service-item">
                    <h3>含浸封孔</h3>
                    <p>提高氣密度、降低洩漏量、加強零件強度與耐用性增加物件穩定性。</p>
                </a>
                <a href="/coating" class="service-item">
                    <h3>皮膜化成</h3>
                    <p>耐蝕保護、塗裝前處理，全部實現自動化產線。</p>
                </a>
                <a href="/robotic" class="service-item">
                    <h3>自動化機械手臂</h3>
                    <p>可搭配砂輪、去毛邊刷、氣動磨筆等工具，快速更換、即插即用。</p>
                </a>
            </div>
        </section>
    </main>
</body>
</html>
"""

# 首頁
@app.route("/")
def home():
    return render_template_string(HTML)

# 各服務子頁面
@app.route("/vibration")
def vibration():
    return "<h1>振動研磨服務詳情</h1><p>這裡是振動研磨的詳細說明頁面。</p>"

@app.route("/sealing")
def sealing():
    return "<h1>含浸封孔服務詳情</h1><p>這裡是含浸封孔的詳細說明頁面。</p>"

@app.route("/coating")
def coating():
    return "<h1>皮膜化成服務詳情</h1><p>這裡是皮膜化成的詳細說明頁面。</p>"

@app.route("/robotic")
def robotic():
    return "<h1>自動化機械手臂服務詳情</h1><p>這裡是自動化機械手臂的詳細說明頁面。</p>"

if __name__ == "__main__":
    app.run(debug=True)
