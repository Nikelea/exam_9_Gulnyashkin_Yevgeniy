Сначала запускаем комманды:
python3.10 -m venv venv 
source venv/bin/activate 
pip install -r requirements.txt
./manage.py migrate
./manage.py loaddata fixtures/auth.json
./manage.py loaddata fixtures/dump.json

Учетка для проверки:
логин: aaa
пароль: aaa

Админка:
логин: admin
пароль: root

Пути для проверки работоспособности АПИ:
http://127.0.0.1:8000/api/v2/publications/  - метод GET - получаем список всех постов. Метод POST - добавляем новый пост, если авторизован
http://127.0.0.1:8000/api/v2/publications/<int:pk> - метод GET - детальное описание поста. 
Метод PATCH - изменение полей поста, если владелец. Метод DELETE - удаление поста если владелец
http://127.0.0.1:8000/api/v2/like/<int:pk> - где pk - id публикации. Будет работать после логина при верном токене. Снимать либо добавлять в избранное, логика обрабатывается во вью. 

