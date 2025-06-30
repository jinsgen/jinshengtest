from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>企業網站範例</title>
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
            justify-content: space-between;
        }
        .service-item {
            flex-basis: 30%;
            background: #f0f4f8;
            padding: 20px;
            border-radius: 6px;
            box-shadow: 0 0 8px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        .service-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
        }
    </style>
</head>
<body>
    <header>
        <h1>簡單企業</h1>
        <nav>
            <a href="#">首頁</a>
            <a href="#">關於我們</a>
            <a href="#">服務項目</a>
            <a href="#">聯絡我們</a>
        </nav>
    </header>

    <div class="banner">專業服務，信賴首選</div>

    <main>
        <section id="about">
            <h2>關於我們</h2>
            <p>我們是一家專注於提供優質服務的企業，致力於創新與客戶滿意，打造專業且值得信賴的品牌形象。</p>
        </section>

        <section id="services">
            <h2>服務項目</h2>
            <div class="services">
                <div class="service-item">
                    <h3>專業顧問諮詢</h3>
                    <p>提供量身打造的顧問服務，協助企業提升競爭力與營運效率。</p>
                </div>
                <div class="service-item">
                    <h3>產品設計與開發</h3>
                    <p>結合最新技術與市場趨勢，打造符合客戶需求的創新產品。</p>
                </div>
                <div class="service-item">
                    <h3>客戶化解決方案</h3>
                    <p>根據企業特性提供專屬方案，解決各種營運與管理挑戰。</p>
                </div>
            </div>
        </section>
    </main>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)

