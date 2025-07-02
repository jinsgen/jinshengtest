from flask import Flask, render_template_string

app = Flask(__name__)

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
        .process-flow {
            display: flex;
            flex-direction: column;
            gap: 30px;
            margin: 60px 0;
        }
        .process-step {
            display: flex;
            align-items: center;
            gap: 30px;
            flex-wrap: wrap;
            border-left: 4px solid var(--primary-blue);
            padding-left: 20px;
        }
        .process-step img {
            width: 120px;
            height: 120px;
            object-fit: cover;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }
        .process-step h3 {
            margin: 0;
            font-size: 20px;
        }
        .process-step p {
            margin: 5px 0 0 0;
            color: #444;
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
            <a href="#process">加工流程</a>
            <a href="#contact">聯絡我們</a>
        </nav>
    </header>
    <div class="banner">一條龍加工產線服務</div>
    <main>
        <section id="process">
            <h2>加工流程</h2>
            <div class="process-flow">
                <div class="process-step" data-aos="fade-right">
                    <img src="/static/step1.jpg" alt="去除毛邊">
                    <div>
                        <h3>毛邊去除（可搭配機械手臂）</h3>
                        <p>使用機械手臂進行精密去除毛邊作業，確保品質一致。</p>
                    </div>
                </div>
                <div class="process-step" data-aos="fade-left">
                    <img src="/static/step2.jpg" alt="振動研磨">
                    <div>
                        <h3>振動研磨</h3>
                        <p>進行細緻拋光與表面均化，去除殘留不規則。</p>
                    </div>
                </div>
                <div class="process-step" data-aos="fade-right">
                    <img src="/static/step3.jpg" alt="含浸封孔">
                    <div>
                        <h3>含浸封孔</h3>
                        <p>有效封閉孔洞，提升氣密性與耐用性。</p>
                    </div>
                </div>
                <div class="process-step" data-aos="fade-left">
                    <img src="/static/step4.jpg" alt="皮膜化成">
                    <div>
                        <h3>皮膜化成（依需求）</h3>
                        <p>提供防蝕塗裝與表面強化，視需求選擇實施。</p>
                    </div>
                </div>
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
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HOME_HTML)

if __name__ == "__main__":
    app.run(debug=True)
