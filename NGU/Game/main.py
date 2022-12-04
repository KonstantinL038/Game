import time
import Class

out_menu = Class.Menu("Script.txt")
player = Class.Stats("Script.txt", 50, 50, 50, 50)

Class.Menu.loading()
Class.Menu.loading_text("text.txt")


def player_ans():
    tries = 1
    player_answer = int(input("Выберите вариант: "))

    while player_answer != 1 and player_answer != 2:
        if tries <= 3:
            print('Милорд мы же вас предупреждали!\nТолько 1 или 2!')
            player_answer = int(input("Выберите вариант: "))
            tries += 1
        elif 4 <= tries <= 7:
            print('Милорд с вами все в порядке? Пожалуйста выберите 1 или 2!')
            player_answer = int(input("Выберите вариант: "))
            tries += 1
        elif tries > 7:
            print('Милорд мы можем с вами спорить бесконечно, но ситуация не изменится! 1 или 2!')
            player_answer = int(input("Выберите вариант: "))
            tries += 1
    else:
        return player_answer


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
    ans = player_ans()
    player.change_stat(ans, out_menu.ans1, out_menu.ans2)

print("ВЫ ПРОИГРАЛИ!")