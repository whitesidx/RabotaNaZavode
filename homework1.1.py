vacation_spots = [
    {'title':'Python Developer','location':'Office','salary':100000,'city':'New York'},
    {'title':'Data Scientist','location':'Remote','salary':120000,'city':'San Francisco'},
    {'title':'Web Developer','location':'Remote','salary':90000,'city':'Los Angeles'},
    {'title':'Software Engineer','location':'Office','salary':110000,'city':'Chicago'},
    {'title':'DevOps Engineer','location':'Remote','salary':95000,'city':'Seattle'},
    {'title':'Mobile Developer','location':'Ofiice','salary':105000,'city':'Boston'},
    {'title':'Game Developer','location':'Remote','salary':98000,'city':'Austin'},
    {'title':'AI Engineer','location':'Remote','salary':130000,'city':'San Jose'},
    {'title':'Frontend Developer','location':'Remote','salary':87000,'city':'Miami'},
    {'title':'Backend Developer','location':'Office','salary':115000,'city':'Denver'}
]

def show_all():
    for dev in vacation_spots:
        print(dev['title'], "-", dev['salary'], "-", dev['city'], "-", dev['location'])

def filter_by_city(city):
    found = False
    for dev in vacation_spots:
        if dev['city'].lower() == city.lower():
            print(dev['title'], "-", dev['salary'], "-", dev['city'], "-", dev['location'])
            found = True
    if not found:
        print("Вакансій у цьому місті не знайдено.")

def filter_by_salary(min_salary):
    found = False
    for dev in vacation_spots:
        if dev['salary'] >= min_salary:
            print(dev['title'], "-", dev['salary'], "-", dev['city'], "-", dev['location'])
            found = True
    if not found:
        print("Вакансій із такою зарплатою не знайдено.")

def filter_remote():
    found = False
    for dev in vacation_spots:
        if dev['location'].lower() == "remote":
            print(dev['title'], "-", dev['salary'], "-", dev['city'], "-", dev['location'])
            found = True
    if not found:
        print("Remote вакансій не знайдено.")

while True:
    print("\nМеню:")
    print("1. Показати всі вакансії")
    print("2. Фільтр по місту")
    print("3. Фільтр по зарплаті")
    print("4. Тільки Remote")
    print("5. Вийти")

    choice = input("Ваш вибір: ")

    if choice == "1":
        show_all()
    elif choice == "2":
        city = input("Введіть місто: ")
        filter_by_city(city)
    elif choice == "3":
        try:
            min_salary = int(input("Введіть мінімальну зарплату: "))
            filter_by_salary(min_salary)
        except ValueError:
            print("Помилка: введіть число")
    elif choice == "4":
        filter_remote()
    elif choice == "5":
        print("Програма завершена.")
        break
    else:
        print("Невірний вибір, спробуйте ще раз.")
