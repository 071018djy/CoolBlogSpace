from flask import Flask, request, render_template, redirect
import os

registered_users = [{'username': '豆包豆包', 'password': 'Zy071018'}]  # 模拟已注册用户列表

app = Flask(__name__, template_folder='F:\\web_project')  # 在代码开头创建应用实例

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(f'获取到的用户名: {username}，密码: {password}')
        print("正在处理注册页面的请求")
        return redirect('/success')  # 注册成功后跳转到成功页面
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_username = request.form.get('loginUsername')
        login_password = request.form.get('loginPassword')
        for user in registered_users:
            if login_username == user['username'] and login_password == user['password']:
                print("登录成功，正在处理登录页面的请求")
                return redirect('/welcome')  # 登录成功后跳转到欢迎页面
        print("登录失败，正在处理登录页面的请求")
        return redirect('/login_failed')  # 登录失败后跳转到登录失败页面
    return render_template('login.html')

@app.route('/about')
def about():
    print("正在处理 about 页面的请求")
    return render_template('about.html')

@app.route('/contact')
def contact():
    print("正在处理 contact 页面的请求")
    return render_template('contact.html')

@app.route('/')  
def index():
    print(os.getcwd())  # 打印当前工作目录
    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/login_failed')
def login_failed():
    return render_template('login_failed.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)