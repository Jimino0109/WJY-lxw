from flask import Flask, render_template, request
import random

app = Flask(__name__)

# 存储道路名称
road_names = []


@app.route('/', methods=['GET', 'POST'])
def index():
    global road_names
    random_roads = []

    if request.method == 'POST':
        # 获取用户输入的道路名称
        input_text = request.form['road_names']
        road_names = [name.strip() for name in input_text.split('\n') if name.strip()]

        # 随机选择五个路名
        if len(road_names) >= 5:
            random_roads = random.sample(road_names, 5)
        else:
            random_roads = ["至少需要输入五个道路名称！"]

    return render_template('index.html', random_roads=random_roads)


if __name__ == '__main__':
    app.run(debug=True)