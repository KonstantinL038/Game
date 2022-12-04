import time
import Class

out_menu = Class.Menu("Script.txt")
player = Class.Stats("Script.txt", 50, 50, 50, 50)

Class.Menu.loading()
Class.Menu.loading_text("text.txt")

while player.check_stat():

    player.get_stats()
    out_menu.choose_ques()
    out_menu.print_question()
    out_menu.remove_question()
    player.question = out_menu.question
    out_menu.print_ans1()
    out_menu.print_ans2()
    time.sleep(1)
    print(5 * "\n")
    player_ans = int(input("Выберите вариант: "))
    player.change_stat(player_ans, out_menu.ans1, out_menu.ans2)

print("ВЫ ПРОИГРАЛИ!")