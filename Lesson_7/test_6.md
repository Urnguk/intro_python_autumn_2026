# Test: Linux и Bash

1. Вы скачали скрипт `report.sh` и проверили его содержимое. Команда `bash report.sh` работает, а `./report.sh` выдаёт `Permission denied`. У файла есть строка `#!/bin/bash`, вы его владелец, а `ls -l` показывает права `-rw-r-----`.

   Выберите одну команду, которая позволит вам запускать скрипт через `./report.sh` и сохранит права группы и остальных пользователей:

   ```bash
   chmod a+x report.sh
   chmod u+r report.sh
   chmod g+x report.sh
   chmod u+x report.sh
   ```

   Почему `bash report.sh` работал с самого начала? Сможет ли участник группы запустить скрипт через `bash report.sh` после изменения прав?

2. В текущей папке есть файл `notes.txt` и папка `reports`. Файла `missing.txt` нет. Рассмотрите скрипт `check.sh`:

   ```bash
   if [ "$#" -eq 0 ]; then
       echo "Укажите путь"
   elif [ -f "$1" ]; then
       echo "Это файл"
   elif [ -d "$1" ]; then
       echo "Это папка"
   else
       echo "Путь не найден"
   fi
   ```

   Что выведет каждый запуск?

   ```bash
   bash check.sh
   bash check.sh notes.txt
   bash check.sh reports
   bash check.sh missing.txt
   bash check.sh missing.txt notes.txt
   ```

   

3. В текущей папке есть ровно два файла с расширением `.txt`: `a.txt` и `b.txt`. Bash перебирает их в алфавитном порядке.

   ```bash
   for file in *.txt; do
       echo "$file" > names.log
   done
   ```

   Что окажется в `names.log` после цикла? Что изменится, если заменить `>` на `>>`? Считайте, что перед каждым запуском `names.log` ещё не существует.