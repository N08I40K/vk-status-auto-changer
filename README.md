# vk-status-auto-changer
Название vk-status-auto-changer говорит само за себя.
Эта программа автоматически изменяет ваш статус в вк каждое указанное количество секунд.
#Установка и запуск
##Windows
1. Скачайте и установите Python (рекомендуется) не ниже 3.7 с [официального сайта](https://python.org)
***Примечание: Во время установки поставте галочку [Add to Path]***
2. Установите Git с [сайта](https://git-scm.com/download/win)
3. Создайте папку в которой будет находится папка с программой программа. (Как бы это странно не звучало :D)
4. В этой же папке создайте .bat файл и запишите в него текст ниже

git clone https://github.com/N08I40K/vk-status-auto-changer

5. Запустите этот файл и зайдите в папку vk-status-auto-changer
6. Установите нужные библиотеки. Для этого откройте консоль в папке где находится файл requirements.txt (Shift + ПКМ -> Открыть коммандную строку здесь) и выполните команду : pip install -r requirements.txt
7. В файле main.py найдите 22-ую строку и измените токен на свой (Сейчас в файле находится не мой токен а рандомный набор символов)
8. По желанию в файле status.txt добавьте или удалите строчки которые будут вашим статусом (Каждый указанный промежуток времени будет менятся статус на любую строчку в этом файле)
***Примечание: randomeasyy = рандомное число, friendsonline = количество друзей онлайн, currtime и currdate = текущее на момент замены статуса дата и время, scriptcycles = сколько раз скрипт дошёл до последней строчки из файла***
9. Запустите файл main.py впишите любую задержку (рекомендуется больше 30 из-за капчи в вк) и дождитесь строчки init4, это значит что скрипт начал работу
10. Остановить скрипт можно комбинацией клавиш **Ctrl + C**

## Связь с разработчиком
[VK](https://vk.com/id_498094647_you_dont_need_him)

Telegram - @N08I40K