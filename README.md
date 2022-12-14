## Дипломный проект TODOLIST
### Стек:
1. python=3.10
2. django=4.1.1
3. django-environ=0.9.0
4. psycopg2-binary=2.9.3

**************************
### Пакеты и их назначение

1. /todolist --- главная папка приложения (Django Rest Framework, API)
   * /core --- пакет ядра, переопределения админки
   * /todolist --- главный пакет
   * /goals --- пакет категорий и целей
   * /bot --- пакет работы с телеграм ботом 
   * .env --- файл с переменными окружения (SECRET_KEY, DEBUG)
   * manage.py --- управляющий файл
**************************
2. /venv --- текущее виртуальное окружение
3. .gitignore --- файл игнорирования коммитов
4. requirements.txt --- файл установленных пакетов
**************************
5. /.github --- папка для GitHub Actions (CI-CD)
   * /workflows
     * build_and_push.yaml --- исполняемый файл для изготовления образов контейнеров и загрузки их на docker-hub
**************************
6. /deploy --- сборка и разворачивание сервиса на виртуальной машине
   * bibaboba --- файл с зашифрованными переменными окружения
   * docker-compose.yaml --- исполняемый файл. 4 контейнера (frontend, backend-api, bot, postgresql)
**************************
7. docker-compose.yaml ---локальный файл для поднятия, тестирования образов frontend, backend-api, bot, postgresql
8. Dockerfile --- локальный файл для сборки и тестирования образа backend-api приложения
9. /tests --- локальная папка для тестирования
**************************

### Deploy
Все необходимые docker-образы загружены на сервер:
1) frontend - скачивается из github
2) backend-api - собирается самостоятельно из todolist
3) bot - собирается самостоятельно из todolist
4) postgresql - собирается самостоятельно из todolist

Приложение доступно по адресу <http://ispirin.site>

### Telegram-бот
В качестве мобильной версии приложения доступен Telegram-бот, позволяющий просматривать цели, 
а также создавать новые в уже существующих категориях.

Бот: _@KorvetBot_

### Доступный функционал:
* Пользователи:
  * Создание пользователя
  * Просмотр, редактирование, удаление профиля
  * Изменение пароля
* Цели:
  * Создание цели
  * Просмотр, редактирование, удаление цели
  * Просмотр списка целей
* Категории:
  * Создание категории
  * Просмотр, редактирование, удаление категории
  * Просмотр списка категорий
* Доски:
  * Создание доски
  * Просмотр, редактирование, удаление доски
  * Просмотр списка досок
* Комментарии:
  * Создание комментария
  * Просмотр, редактирование, удаление комментария
  * Просмотр списка комментариев
### Тесты
Разработаны автоматические тесты, покрывающие основной функционал приложения

Запуск тестов: `pytest`

   