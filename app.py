from flask import Flask, render_template_string

app = Flask(__name__)

HOME_HTML = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>溍慎/鈦吉有限公司</title>
    <style>
        /* 基本配色 */
        :root {
            --primary-blue: #004080;
            --accent-yellow: #FFC107;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0; padding: 0;
        }
        header {
            background-color: var(--primary-blue);
            padding: 15px 30px;
            color: white;
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            align-items: center;
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
            background-image: none;
            height: 200px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 36px;
            font-weight: bold;
            text-shadow: none;
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
        .service-item h3 {
            background-color: var(--accent-yellow);
            color: var(--primary-blue);
            display: inline-block;
            padding: 4px 8px;
            border-radius: 4px;
            margin-bottom: 8px;
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
            overflow: hidden;
            cursor: pointer;
            transition: transform 0.3s ease;
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
        .service-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
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
            header {
                flex-direction: column;
                align-items: flex-start;
            }
            .brand, .title {
                margin-bottom: 10px;
                width: 100%;
            }
            nav {
                flex-wrap: wrap;
                width: 100%;
            }
            #mobile-footer-nav { display: flex; }
            #topBtn { display: block; }
        }

        /* 手機底部導航 */
        #mobile-footer-nav {
            display: none;
            position: fixed;
            bottom: 0; left: 0; right: 0;
            background-color: var(--primary-blue);
            padding: 8px 0;
            display: flex; justify-content: space-around;
        }
        #mobile-footer-nav a {
            color: white;
            font-weight: 600;
            text-decoration: none;
            font-size: 14px;
        }

        /* 返回頂端按鈕 */
        #topBtn {
            display: none;
            position: fixed;
            bottom: 60px; right: 20px;
            font-size: 18px;
            background-color: var(--primary-blue);
            color: white;
            padding: 12px; border-radius: 50%;
            border: none; cursor: pointer;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        }
        #topBtn:hover {
            background-color: #003366;
        }

        /* Lightbox */
        #lightbox-overlay {
            position: fixed;
            inset: 0; background: rgba(0,0,0,0.8);
            display: none; justify-content: center; align-items: center;
            z-index: 1000;
        }
        #lightbox-overlay img {
            max-width: 90%; max-height: 90%;
            border-radius: 8px;
            box-shadow: 0 0 20px rgba(255,255,255,0.5);
        }
    </style>
</head>
<body>
    <header>
        <div class="brand">
            <img src="/static/logo.png" alt="公司LOGO">
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
            <p>本公司專營鋁合金與鋅合金產品之表面處理，服務內容涵蓋振動研磨、含浸封孔及皮膜化成處理。</p>
        </section>

        <section id="services">
            <h2>服務項目</h2>
            <div class="services">
                <!-- 各服務項目 -->
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

    <!-- 手機版底部 -->
    <nav id="mobile-footer-nav">
        <a href="/">首頁</a>
        <a href="#about">關於溍慎</a>
        <a href="#services">服務項目</a>
        <a href="#contact">聯絡我們</a>
    </nav>

    <!-- 返回頂端 -->
    <button id="topBtn">▲</button>

    <!-- Lightbox -->
    <div id="lightbox-overlay"><img src="" alt=""></div>

    <script>
    // 返回頂端
    const topBtn = document.getElementById("topBtn");
    window.addEventListener("scroll", () => {
        topBtn.style.display = document.documentElement.scrollTop > 200 ? "block" : "none";
    });
    topBtn.onclick = () => window.scrollTo({ top: 0, behavior: 'smooth' });

    // Lightbox 效果
    document.querySelectorAll('.service-item').forEach(item => {
        item.onclick = () => {
            document.querySelector('#lightbox-overlay img').src = item.getAttribute('data-img');
            document.getElementById('lightbox-overlay').style.display = 'flex';
        };
    });
    document.getElementById('lightbox-overlay').onclick = e => {
        if (e.target !== e.currentTarget.querySelector('img')) {
            document.getElementById('lightbox-overlay').style.display = 'none';
        }
    };
    </script>
</body>
</html>
"""

# ...Flask路由與SUB_TEMPLATE省略，與之前相同...
