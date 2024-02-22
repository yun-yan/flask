from flask import Flask, render_template

app = Flask(__name__)

# 主页路由
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('main.html')  # 假设您的主页文件名为 main.html

# 课程安排页面路由
@app.route('/schedule')
def schedule():
    return render_template('schedule.html')  # 假设您的课程安排页面文件名为 schedule.html

if __name__ == '__main__':
    app.run()
