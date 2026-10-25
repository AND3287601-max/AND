// === ТЕСТОВАЯ КОМНАТА JAVASCRIPT ===

// Константы (Предметы, которые нельзя изменить)
const MAX_LEVEL = 99;
// Переменные (Предметы, которые меняются)
let currentLevel = 1;

// Классы 
class Entity {
    constructor(type) {
        this.type = type;
        this.active = true;
    }
}

// Стрелочные функции (Короткий синтаксис для способностей)
const spawnEnemy = (name, health) => {
    return { name: name, hp: health }; // Возвращает JSON-объект
};

function startDebug() {
    // Массивы разных типов
    let coordinates = [10.5, 20.1, 5.0];

    // Цепочка условий
    if (currentLevel < MAX_LEVEL) {
        console.log("Можно получать опыт.");
    } else if (currentLevel === MAX_LEVEL) {
        console.log("Достигнут максимальный уровень!");
    } else {
        console.log("Глитч уровня.");
    }

    // Классический цикл FOR
    for (let i = 0; i < coordinates.length; i++) {
        console.log(`Координата оси ${i}: ${coordinates[i]}`);
    }

    // Оператор Switch (Машина состояний)
    let weather = "RAIN";
    switch (weather) {
        case "SUN":
            console.log("Солнечно.");
            break;
        case "RAIN":
            console.log("Идет дождь. Снижена видимость.");
            break;
        default:
            console.log("Обычная погода.");
    }

    // Обработка ошибок
    try {
        throw new Error("Сбой физического движка!");
    } catch (error) {
        console.error("Пойман баг:", error.message);
    }
}

startDebug();
