# 1、主持人
# 1、控制游戏流程，控制通信，接收所有人的发言，转发给其他人
# 流程
# 1、发牌
# 2、天亮，天黑，
# 3、记录天黑的动作
# 4、统筹投票，踢人
# 5、判断游戏的胜负
# 三个狼都死  正义胜利
# 三个平民或者三个神都死  狼赢了
#
# 2、其他人
# 投票
# 选出其他人当中的一个，杀死
# 发言
# 发言
# 遗言
# 发言，完成之后退出
# 3、平民
# 普通的其他人
# 4、狼人
# 知道队友
# 每晚投票杀人
# 5、预言家
# 没晚查看其他人身份
# 6、女巫
# 有一次晚上杀人的机会
# 有一次晚上救人的机会
# 每晚只能执行一种
# 只有第一晚可以自救
# 7、猎人
# 被杀死可以杀死一人
# 如果被女巫毒死不可以开枪
class Timer:
    pass

class Judger:
    def control_time(self):
        print("天黑请闭眼")
        print("天亮了")
    def check_time(self):
        print("狼人请睁眼")
    def speak_time(self):
        print("玩家请发言")
    def choice(self):
        print("玩家请投票")
    def end_game(self):
        if Wolf.number==0:
            print("平民获胜,游戏结束")
        elif Hunter.number==0 and Prophet.number==0 and Hunter.number==0:
            print("狼人获胜,游戏结束")
        elif Villager.number==0:
            print("狼人获胜,游戏结束")

class People:
    def __init__(self,number):
        self.number=number
        hp=1
    def speak(self):
        print("发言内容")
    def make_choice(self):
        print("我选择玩家")

class Hunter(People):
    identity="猎人"
    def shoot(self):
        pass
class Wolf(People):
    identity="狼人"
    def attack(self):
        pass
class witch(People):
    identity="女巫"
    def heal(self):
        pass
    def poison(self):
        pass
class Prophet(People):
    identity="预言家"
    def check(self):
        pass
class Villager(People):
    identity="平民"