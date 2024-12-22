import os 
os.system("cls")

### **Texnik topshiriq: Ovqat yetkazib berish tizimi**


# class Dish:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
# class Menu:
#     def __init__(self):
#         self.dishes = []

#     def add_dish(self, dish):
#         self.dishes.append(dish)

#     def display_menu(self):
#         for dish in self.dishes:
#             print(f"{dish.name}: ${dish.price:.2f}")
# import itertools

# class Order:
#     _ids = itertools.count(1)

#     def __init__(self, selected_dishes):
#         self.order_id = next(self._ids)
#         self.selected_dishes = selected_dishes
#         self.total_price = sum(dish.price for dish in selected_dishes)
# class Customer:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone

# class DeliveryPerson:
#     def __init__(self, name, vehicle_number):
#         self.name = name
#         self.vehicle_number = vehicle_number
# class DeliverySystem:
#     def __init__(self, menu):
#         self.menu = menu
#         self.orders = []

#     def take_order(self, customer, selected_dishes):
#         order = Order(selected_dishes)
#         self.orders.append(order)
#         print(f"Order ID: {order.order_id}, Total: ${order.total_price:.2f}")
#         return order

#     def deliver_order(self, order, delivery_person):
#         print(f"Order ID: {order.order_id} is being delivered by {delivery_person.name} ({delivery_person.vehicle_number})")

# menu = Menu()
# menu.add_dish(Dish("shorva", 40.99))
# menu.add_dish(Dish("osh", 45.99))
# menu.add_dish(Dish("Somsa", 12.99))
# menu.display_menu()


# customer = Customer("Jasur Samatov", "123-456-7890")
# delivery_person = DeliveryPerson("Jamila Salimova", "XYZ-123")


# system = DeliverySystem(menu)
# selected_dishes = [menu.dishes[0], menu.dishes[2]]  # Mijoz shorva va Somsa tanladi
# order = system.take_order(customer, selected_dishes)
# system.deliver_order(order, delivery_person)
# # 14
# def series14(K, sonlar):
#     kichik_sonlar = [son for son in sonlar if son < K]
#     return len(kichik_sonlar) if kichik_sonlar else 0

# K = 50
# sonlar = [10, 20, 30, 40, 60, 70, 80, 0]
# natija = series14(K, sonlar)
# print(natija) 
# # 15
# def series15(K, sonlar):
#     for i, son in enumerate(sonlar):
#         if son > K:
#             return i + 1 
#     return 0

# K = 30
# sonlar = [10, 20, 30, 40, 50, 60, 0]
# natija = series15(K, sonlar)
# print(natija)  

# # 16
# def series16(K, sonlar):
#     oxirgi_katta_son_indeksi = 0
#     for i, son in enumerate(sonlar):
#         if son > K:
#             oxirgi_katta_son_indeksi = i + 1  
#     return oxirgi_katta_son_indeksi

# K = 30
# sonlar = [10, 20, 30, 40, 50, 60, 0]
# natija = series16(K, sonlar)
# print(natija)  

# # 17
# def series17(B, sonlar):
#     natijalar = [B] + sonlar
#     return natijalar



# B = 3.5
# sonlar = [1.1, 2.2, 3.3, 4.4, 5.5]
# natija = series17(B, sonlar)
# print(natija)  

# # 18
# def series18(sonlar):
#     har_xil_qiymatlar = list(dict.fromkeys(sonlar))
#     return har_xil_qiymatlar


# sonlar = [1, 2, 2, 3, 4, 4, 5]
# natija = series18(sonlar)
# # # 19
# print(natija)  
# def series19(sonlar):
#     kichik_sonlar = [sonlar[i] for i in range(1, len(sonlar)) if sonlar[i] < sonlar[i - 1]]
#     return kichik_sonlar, len(kichik_sonlar)

# sonlar = [10, 9, 8, 7, 6, 5, 4]
# natija, soni = series19(sonlar)
# print(natija)  
# print(soni)    


