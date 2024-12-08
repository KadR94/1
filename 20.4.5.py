import json

file = r'C:\Users\user\Desktop\Учеба\Модуль 20\asset-v1_SkillFactory+QAP-3.0+2021+type@asset+block@orders_july_2023.json'
with open(file, "r") as my_file:
    orders = json.load(my_file)
print(orders)

#1. Какой номер самого дорого заказа за июль?
max_price=0
for orders_num, orders_data in orders.items():
    price=orders_data['price']
    if price>max_price:
        order=orders_num
        max_price=price
print(f'1. Номер заказа с самой большой стоимостью: {order}, стоимость заказа: {max_price}')


#2. Какой номер заказа с самым большим количеством товаров?
max_quantity=0
for orders_num, orders_data in orders.items():
    quantity = orders_data['quantity']
    if quantity >= max_quantity:
        order = orders_num
        max_quantity = quantity
print(f'2. Номер заказа с самым большим количеством товаров: {order} с количеством заказов: {max_quantity}')

#3. В какой день в июле было сделано больше всего заказов?
date_dict={}
for orders_num, orders_data in orders.items():
    date=orders_data['date']
    date_dict[date] = date_dict.get(date, 0) + 1
for date in sorted(date_dict):
    max_value = max(date_dict.values())
    if date_dict[date] == max_value:
        print(f'3. Больше всего заказов было сделано в {date}: {date_dict[date]}')

#4. Какой пользователь сделал самое большое количество заказов за июль?
max_orders = 0
user_dict = {}
for orders_num, orders_data in orders.items():
    user_id=orders_data['user_id']
    user_dict[user_id] = user_dict.get(user_id, 0) + 1
    orders_2 = user_dict.get(user_id)
    if orders_2 > max_orders:
        max_orders = orders_2
print(f'4. Самое большое количество заказов сделал пользователь {user_id} с количеством заказов: {max_orders}')

#5. У какого пользователя самая большая суммарная стоимость заказов за июль?
user_dict={}
max_price = 0
for orders_num, orders_data in orders.items():
    user_id=orders_data['user_id']
    price = orders_data['price']
    user_dict[user_id] = user_dict.get(user_id, 0) + price
    all_price = user_dict.get(user_id)
    if all_price > max_price:
        max_price = all_price
print(f'5. Пользователь {user_id} имеет самую большую суммарную стоимость заказов за июль: {max_price}')

#6. Какая средняя стоимость заказа была в июле?
price_sum = 0
price_count = 0
for orders_num, orders_data in orders.items():
    price = orders_data['price']
    price_sum += price
    price_count = len(orders)
print(f'6. Средняя стоимость заказ в июле: {price_sum//price_count}')

#7. Какая средняя стоимость товаров в июле?
sum_all, count = 0, 0
for orders_num, orders_data in orders.items():
    price = orders_data['price']
    quantity = orders_data['quantity']
    sum_all += price
    count += quantity
print(f'7. Средняя стоимость товаров в июле: {sum_all/count}')