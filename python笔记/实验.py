class Dongwu:
    name = "两栖动物"

    def features(self):
        print("幼年用鳃呼吸")
        print("成年用肺兼皮肤呼吸")

class Frog(Dongwu):
    def attr(self):
        print(f"青蛙是{self.name}")
        print("我会呱呱叫")

frog = Frog()
print(frog.name)
frog.features()
frog.attr()

class Father:
    hight = 178

    def run(self):
        print("跑步速度特别快")
        print("反应也很快")

class Son(Father):
    def write(self):
        print(f"我的身高大于{self.hight}")
        print("字迹十分工整")

son = Son()
print(son.hight)
son.run()
son.write()