**Стэк технологий**
1) Python3
2) MongoDB
3) Mongoengine
4) Flask
5) Flask restful
6) Telebot
7) Google cloud
8) Nginx
9) Gunicorn
10) Marhsmallow

**Сущности бд**
1) Продукты
   1. Название
   2. Описание
   3. {Категория} 
   4. Цена
   5. Наличие
   6. Картинка
   7. Скидка в процентах 
    
2) Категории
   1. Название
   2. Описание
   3. {parent}
   4. [{подкатегории}] 
3) Пользователи
   1. telegram id (ПК)
   2. Номер телефона
   3. Никнейм
4) Корзина
5) Заказы
6) Новости
   1. Заголовок
   2. Содержимое
   3. Дата публикации 
   
#Lesson 12
1) Создать абстрактную колекцию. Она должна содержать два поля created и modified, и хранить в них дату и время. 
created - время создания объекта, modified - время последнего обновления. Логику со временем размещаем в методе save.
2) Проинициализровать бот. Описать хендлер /start. При старте приветсвовать пользователя. Создать модуль constants, в котором
будем хранитьс текста и другие константы. 
   
#Lesson 13
1) Описать хендлер, который будет отрабатывать при клике на кнопку "Новости". Выводить последние 5 новостей
   отдельными сообщениями.
2) Колекция новостей должна наследовать абстрактную колекцию (created_at, modified_at, 12.1)
3) Описать хендлер для клика на кнопку определенной категории. Выводить названия всех продуктов, которые 
относятся к кликнкутой категории. Названия продуктов выводить отдельными сообщениями. 
   
#Lesson 14

1) Описать метод форматирования описания продукта (цена, название, описание, характеристки). Отправлять 
эту информацию под картинкой продукта.
2) Описать хендлер для обработки кликов на категории. (Сделано на занятии)
3) Описать колекции корзины и заказа

#Lesson 15
1) Реализовать логику для изменения данных профиля (почта, номер телефона, имя, адресс). Добавить в модель юзера
поле адресс. 