// === ТЕСТОВАЯ КОМНАТА C++ ===
#include <iostream> // Ввод/Вывод
#include <vector>   // Динамические массивы
#include <string>   // Работа с текстом

using namespace std;

// Структуры (Простые чертежи данных)
struct Transform {
    float x, y, z;
};

// Классы
class Weapon {
public: // Доступно всем
    string name;
    int damage;

    // Конструктор
    Weapon(string n, int d) : name(n), damage(d) {}

    void upgrade() {
        damage += 5;
    }
};

int main() {
    // Базовые типы
    int gold = 150;
    float speed = 4.5f;
    bool isQuestActive = true;

    // Вектор (Инвентарь, который может расширяться)
    vector<string> spells = {"Fireball", "Heal", "Ice Spike"};

    // === МАГИЯ C++: УКАЗАТЕЛИ ===
    // Мы берем прямой физический адрес переменной gold в памяти
    int* goldPointer = &gold; 
    *goldPointer += 50; // Добавили золото напрямую в память!
    
    cout << "Золото после читов: " << gold << endl;

    // Цикл FOR
    for (int i = 0; i < spells.size(); i++) {
        cout << "Изучено заклинание: " << spells[i] << endl;
    }

    // Работа с объектом
    Weapon sword("Железный меч", 15);
    sword.upgrade();
    cout << sword.name << " теперь наносит " << sword.damage << " урона." << endl;

    return 0; // Код успешного завершения
}
