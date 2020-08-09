from random import choice

class RandomWalk():
    """一个生成随机漫步数据的类"""

    def __init__(self, num_point=500):
        # 初始化随机漫步的属性
        self.num_point = num_point

        # 所有随机漫步都始于(0,0)
        self.x_values = [0]
        self.y_values = [0]

