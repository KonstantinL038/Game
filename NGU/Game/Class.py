from random import choice
import time


class ScriptReader:
    script = dict()

    def __init__(self, file: str):
        with open(file, "r", encoding="utf-8") as f_in:
            line: str
            for line in f_in.readlines():
                stat_dict = dict()

                question = line[:line.find(" 1)")]
                ans1 = line[line.find("1)") + 2:line.find(":")]
                stat1 = line[line.find(":") + 2:line.find(";")]
                ans2 = line[line.find("2)") + 2:line.find(":", line.find("2)"))]
                stat2 = line[line.find(":", line.find("2)")) + 2:-1]

                stat_dict[ans1] = stat1
                stat_dict[ans2] = stat2

                self.script[question] = stat_dict

    def all_question(self):
        q_l = list()
        for key in self.script.keys():
            q_l.append(key)

        return q_l


class Menu(ScriptReader):

    def __init__(self, file):
        super().__init__(file)
        self.question = None
        self.ans1 = None
        self.ans2 = None
        self.q_list = self.all_question()

    def choose_ques(self):
        # Вопросы
        q = choice(self.q_list)
        self.question = q
        # Варианты ответа
        ans = [i for i in self.script[q]]
        self.ans1 = ans[0]
        self.ans2 = ans[1]

    def remove_question(self):
        self.q_list.remove(self.question)

    def print_question(self):
        for ch in self.question:
            time.sleep(0.02)
            print(ch, end="")
        print("")

    def print_ans1(self):
        print(f'{self.ans1} - 1')

    def print_ans2(self):
        print(f'{self.ans2} - 2')

    @staticmethod
    def loading():
        print('                                                     ....GAME Of KiNGDOMS....')
        s = '█'
        for i in range(101):
            time.sleep(0.08)
            print("\r"'Loading:', i * s, str(i), '%', end='')

        print(' \DONE...\n')
        input("\nНажмите Enter, чтобы продолжить.")
        print("")

    @staticmethod
    def loading_text(file: str, k=0):
        with open(file, "r", encoding="utf-8") as f_out:
            print("┍─━───━───━────━──━──┙◆┕──━──━───━───━───━──┑")
            for line in f_out.readlines():
                for ch in line:
                    time.sleep(0.05)
                    if line == "\n":
                        print("┕─━───━───━────━──━──┑◆┍──━──━───━───━───━──┙")
                        input("\nНажмите Enter, чтобы продолжить.")
                        print("")
                        k += 1
                        if k <= 3:
                            print("┍─━───━───━────━──━──┙◆┕──━──━───━───━───━──┑")

                    else:
                        print(ch, end="")


class Stats(Menu):

    def __init__(self, file: str, church=50, society=50, army=50, treasury=50, year=1500):
        super().__init__(file)
        self.church = church
        self.society = society
        self.army = army
        self.treasury = treasury
        self.year = year

    def check_stat(self):
        st1, st2 = self.church, self.society
        st3, st4 = self.army, self.treasury

        if 0 < st1 < 100:
            if 0 < st2 < 100:
                if 0 < st3 < 100:
                    if 0 < st4:
                        return True
        return False

    def change_stat(self, player_ans: int, ans1, ans2):
        global event
        even = "answer"
        if player_ans == 1:
            event = ans1
        elif player_ans == 2:
            event = ans2

        event_st = self.script[self.question][event].split()

        self.church += int(event_st[0])
        self.society += int(event_st[1])
        self.army += int(event_st[2])
        self.treasury += int(event_st[3])

        if self.treasury > 100:
            self.treasury = 100

    def get_stats(self):
        stat_list = [self.church, self.society, self.army, self.treasury]
        stat_sing = ["†", "♀", "⚔", "$"]
        print(
            "\n─━───━────━──━──┙◆┕──━──━───━───━───━───━────━──━──┙◆┕──━──━───━───━───━───━────━──━──┙◆┕──━──━───━───━──")
        print(f"\n                                                 Год {self.year} ")
        self.year += 1
        print(f"                                                СТАТИСТИКА")
        for i in range(len(stat_list)):
            time.sleep(0.08)
            if 0 < int(stat_list[i]) <= 10:
                print(f'                                        {stat_sing[i]} -〘 ▌︎︎ ︎︎             〙')
            elif 10 < int(stat_list[i]) <= 20:
                print(f'                                        {stat_sing[i]} -〘 ▌︎▌︎ ︎︎           〙')
            elif 20 < int(stat_list[i]) <= 30:
                print(f'                                        {stat_sing[i]} -〘 ▌︎▌︎▌︎︎︎          〙')
            elif 30 < int(stat_list[i]) <= 40:
                print(f'                                        {stat_sing[i]} -〘 ▌︎▌︎▌︎▌︎︎ ︎︎        〙')
            elif 40 < int(stat_list[i]) <= 50:
                print(f'                                        {stat_sing[i]} -〘 ▌︎▌︎▌︎▌︎▌︎︎       〙')
            elif 50 < int(stat_list[i]) <= 60:
                print(f'                                        {stat_sing[i]} -〘 ▌︎▌︎▌︎▌︎▌︎▌︎︎ ︎︎     〙')
            elif 60 < int(stat_list[i]) <= 70:
                print(f'                                        {stat_sing[i]} -〘 ▌︎▌︎▌︎▌︎▌︎▌︎▌︎︎    〙')
            elif 70 < int(stat_list[i]) <= 80:
                print(f'                                        {stat_sing[i]} -〘 ▌︎▌︎▌︎▌︎▌︎▌︎▌︎▌︎︎ ︎︎  〙')
            elif 80 < int(stat_list[i]) <= 90:
                print(f'                                        {stat_sing[i]} -〘 ▌︎▌︎▌︎▌︎▌︎▌︎▌︎▌︎▌︎ 〙')
            elif 90 < int(stat_list[i]) <= 100:
                print(f'                                        {stat_sing[i]} -〘 ▌︎▌︎▌︎▌︎▌︎▌︎▌︎▌︎▌︎︎▌︎〙')

        print("")
