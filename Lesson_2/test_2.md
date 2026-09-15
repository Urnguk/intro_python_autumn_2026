# Test_2: Python basics

1.  Перечислите основные типы данных которые вы знаете.
2.  Что выведет на экран данная программа?

```python
order_sum = 4200

if order_sum >= 5000:
    delivery = 0
elif order_sum >= 3000:
    delivery = 200
else:
    delivery = 400

if delivery == 0:
    print("Доставка бесплатная")
elif order_sum + delivery >= 4250:
    print("Стоимость доставки:", delivery // 2)
else:
    print("Стоимость доставки:", delivery)
```

Запишите точно, что будет выведено на экран, и обоснуйте.

3. Напишите программу, которая выводит на экран все числа от 1 до 30, кратные 3 и не кратные 2.