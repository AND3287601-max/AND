# === ТЕСТОВАЯ КОМНАТА PYTHON ===
import math # Импорт модулей (подключение DLC)

# Классы (Создание чертежа для сущности)
class Player:
    def __init__(self, name):
        # Переменные (характеристики)
        self.name = name       # Строка (Текст)
        self.hp = 100          # Целое число (Integer)
        self.is_alive = True   # Логический тип (Boolean)

    # Метод (Способность сущности)
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.is_alive = False

# Главная функция (Точка входа)
def main():
    # Списки (Инвентарь персонажа)
    inventory = ["Меч", "Зелье", "Щит"]
    inventory.append("Карта") # Добавление предмета

    # Словари (База данных ключ-значение)
    stats = {"strength": 15, "agility": 10}

    # Цикл FOR (Перебор всех предметов)
    print("В инвентаре:")
    for item in inventory:
        print(f"- {item}")

    # Создание объекта из класса (Спавн игрока)
    hero = Player("Артур")

    # Условия IF/ELSE (Развилки сюжета)
    if hero.is_alive and hero.hp > 50:
        print(f"{hero.name} готов к бою! HP: {hero.hp}")
    else:
        print("Игроку нужен отдых.")

    # Цикл WHILE (Действие, пока условие истинно)
    while hero.hp > 80:
        hero.take_damage(10)
        print(f"Получен урон от лавы! Текущее HP: {hero.hp}")

    # Обработка исключений (Защита от краша игры)
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Баг: попытка поделить на ноль заблокирована!")

# Запуск программы
if __name__ == "__main__":
    main()
    