import time
import random
import os
import sys
is_trd_python = 0 # 0 = python, 1 = python3
escape = 0
if is_trd_python != "1":
    python_start = "python"
else:
    python_start = "python3"
try:
    import vk_api
    from vk_api.longpoll import VkEventType, VkLongPoll
    from vk_api import VkApi
except Exception as error:
    if str(error) == "No module named \'vk_api\'":
        soglasie = input("Install python module \"vk-api\"? (y/n)\n")
        if str(soglasie) == "y":
            os.system(python_start + " -m pip install vk-api --user")
            del soglasie
            escape = "1"
        else:
            exit()
try:
    import datetime
except Exception as error:
    if str(error) == "No module named \'datetime\'":
        soglasie = input("Install python module \"datetime\"? (y/n)\n")
        if str(soglasie) == "y":
            os.system(python_start + " -m pip install datetime --user")
            del soglasie
            escape = "1"
        else:
            exit()
try:
    import pytz
except Exception as error:
    if str(error) == "No module named \'pytz\'":
        soglasie = input("Install python module \"pytz\"? (y/n)\n")
        if str(soglasie) == "y":
            os.system(python_start + " -m pip install pytz --user")
            del soglasie
            escape = "1"
        else:
            exit()
if escape == "1":
    print("Restart this!")
    exit()
def reboot():
    # функция перезагрузки бота
    # аругмент функции влияет на выбор команды для перезагрузки
    way = os.path.abspath(__file__)
    os.system(python_start + " \"" + way + "\"")

def get_time():
    # возвращает время формата ДД.ММ.ГГ ЧЧ:ММ:СС (по МСК)
    # например, 01.01.01 13:37:00
    return datetime.datetime.strftime(datetime.datetime.now(pytz.timezone('Europe/Moscow')), "%d.%m.%Y %H:%M:%S")


def console_log(text, symbols_amount=30):
    # выводит данные в консоль с указанием времени и интервалом после
    print("[" + get_time() + "] " + text)
    print("-" * symbols_amount)
try:
    vk_session = vk_api.VkApi(token="your token")
    long_poll = VkLongPoll(vk_session)
    vk = vk_session.get_api()
except Exception as e:
    console_log("Во время подключения/получения параметров произошла ошибка: ")
    console_log("Произвожу попытку переподключения через 10 секунд...")
    time.sleep(10)


def status_set(text=None):
    vk.status.set(
        random_id=random.randint(-2147483648, 2147483647),
    )

def main():
    timeout_set = 120
    try:
        script_path = os.path.abspath(__file__).replace("main.py", "")
        configg_lines = open(script_path + "status.txt", encoding="utf-8").readlines()
        def count_lines(filename, chunk_size=1<<13):
            with open(filename) as file:
                return sum(chunk.count('\n')
                    for chunk in iter(lambda: file.read(chunk_size), ''))
        count_lines("status.txt")
        strnum = 0
        scriptcycless = 0
        strings = count_lines("status.txt") + 1
        status_text = ""
        while True:
            if strnum >= strings:
                strnum = 0
                scriptcycless += 1 
            # VARS
            delta = datetime.timedelta(hours=3, minutes=0) # разница от UTC. Можете вписать любое значение вместо 3
            t = (datetime.datetime.now(datetime.timezone.utc) + delta) # Присваиваем дату и время переменной «t»
            nowtime = t.strftime("%H:%M")
            nowdate = t.strftime("%d.%m.%Y")
            on = vk.friends.getOnline()
            friendsonlinee = len(on)
            # VARS                    
            status_text = configg_lines[int(strnum)].replace("scriptcycles", str(scriptcycless)).replace("friendsonline", str(friendsonlinee)).replace("currdate", str(nowdate)).replace("currtime", str(nowtime)).replace("randomeasyy", str(random.randint(-1000000000000000000000000000, 1000000000000000000000000000)))
            vk.status.set(text=status_text, random_id=random.randint(-2147483648, 2147483647))
            print("Ваш статус: " + status_text)
            strnum += 1
            time.sleep(int(timeout_set))
    except Exception as vk_error:
        console_log("Ошибка")
        reboot()
main()