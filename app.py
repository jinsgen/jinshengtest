from flask import Flask, render_template_string

app = Flask(__name__)

# 首頁 HTML
HOME_HTML = """（原本你的首頁 HTML 保留）"""

# 路由：首頁
@app.route("/")
def home():
    return render_template_string(HOME_HTML)

# 路由：關於溍慎
@app.route("/about")
def about():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang=\"zh-Hant\">
    <head>
        <meta charset=\"UTF-8\">
        <title>關於溍慎</title>
    </head>
    <body>
        <header style=\"background:#6d8ec7;color:white;padding:15px 30px;display:flex;justify-content:space-between;\">
            <div>關於溍慎</div>
            <a href=\"/\" style=\"color:white;text-decoration:none;\">← 回首頁</a>
        </header>
        <main style=\"max-width:800px;margin:40px auto;padding:20px;font-family:sans-serif;\">
            <h2>我們的使命</h2>
            <p>溍慎有限公司/鈦吉有限公司專注於金屬表面處理，致力於提供穩定、高品質的一站式加工服務。</p>
            <p>我們擁有完整產線與專業人員，可提供彈性化的代工方案，服務產業包含汽車、航太、電子等。</p>
        </main>
        <footer style=\"background:#f2f7fb;padding:20px;font-family:sans-serif;line-height:1.8;\">
            地址：<a href=\"https://maps.app.goo.gl/8dkFhGhkzxeEaBYaA\" target=\"_blank\">台南市仁德區義林路148巷16號</a><br>
            Tel：06-2708989<br>
            Fax：06-2707878<br>
            Mobile：0975124624（鄭先生）<br>
            Email：<a href=\"mailto:js42915245@gmail.com\">js42915245@gmail.com</a>
        </footer>
    </body>
    </html>
    """)

# 路由：一條龍產線
@app.route("/onedragon")
def onedragon():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang=\"zh-Hant\">
    <head>
        <meta charset=\"UTF-8\">
        <title>一條龍產線</title>
    </head>
    <body>
        <header style=\"background:#6d8ec7;color:white;padding:15px 30px;display:flex;justify-content:space-between;\">
            <div>一條龍產線服務</div>
            <a href=\"/\" style=\"color:white;text-decoration:none;\">← 回首頁</a>
        </header>
        <main style=\"max-width:800px;margin:40px auto;padding:20px;font-family:sans-serif;\">
            <h2>完整加工流程</h2>
            <ol>
                <li>毛邊去除（可搭配機械手臂）</li>
                <li>振動研磨</li>
                <li>含浸封孔</li>
                <li>皮膜化成（視需求）</li>
            </ol>
            <p>我們提供整合式產線，節省客戶物流時間與管理成本。</p>
        </main>
        <footer style=\"background:#f2f7fb;padding:20px;font-family:sans-serif;line-height:1.8;\">
            地址：<a href=\"https://maps.app.goo.gl/8dkFhGhkzxeEaBYaA\" target=\"_blank\">台南市仁德區義林路148巷16號</a><br>
            Tel：06-2708989<br>
            Fax：06-2707878<br>
            Mobile：0975124624（鄭先生）<br>
            Email：<a href=\"mailto:js42915245@gmail.com\">js42915245@gmail.com</a>
        </footer>
    </body>
    </html>
    """)

if __name__ == '__main__':
    app.run(debug=True)
