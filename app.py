from flask import Flask, render_template, request, redirect, url_for, session, flash
import hashlib  # 用于密码加密

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# 预设的用户名和加密后的密码（'0000'的MD5加密结果）
PRESET_CREDENTIALS = {'admin': hashlib.md5('0000'.encode()).hexdigest()}

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'username' in session:
        return render_template('main.html', username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.md5(request.form['password'].encode()).hexdigest()  # 对密码进行MD5加密

        if username in PRESET_CREDENTIALS and PRESET_CREDENTIALS[username] == password:
            session['username'] = username  # 登录成功，设置session
            return redirect(url_for('home'))
        else:
            flash('用户名或密码错误！')  # 登录失败，显示错误信息

    return render_template('login.html')  # 显示登录页面

@app.route('/logout')
def logout():
    session.pop('username', None)  # 登出，清除session
    return redirect(url_for('home'))  # 重定向到首页

@app.route('/schedule')
def schedule():
    if 'username' in session:
        return render_template('schedule.html')  # 如果用户已登录，显示课程安排页面
    else:
        return redirect(url_for('login'))  # 未登录用户重定向到登录页面

if __name__ == '__main__':
    app.run(debug=True)
