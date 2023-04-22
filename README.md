Пути для проверки работоспособности:
http://127.0.0.1:8000/api/v2/publications/  - метод GET - получаем список всех постов. Метод POST - добавляем новый пост, если авторизован
http://127.0.0.1:8000/api/v2/publications/<int:pk> - метод GET - детальное описание поста. 
Метод PATCH - изменение полей поста, если владелец. Метод DELETE - удаление поста если владелец
http://127.0.0.1:8000/api/v2/like/<int:pk> - где pk - id публикации. Будет работать после логина при верном токене. Снимать либо ставить лайк, логика обрабатывается во вью. 

Учетка для проверки:
логин: aaa
пароль: aaa

Админка:
логин: admin
пароль: root