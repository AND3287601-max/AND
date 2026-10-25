using UnityEngine;

public class PlayerSurvival : MonoBehaviour
{
    [Header("Показатели")]
    public float maxHealth = 100f;
    public float maxHunger = 100f;
    public float maxThirst = 100f;

    public float currentHealth;
    public float currentHunger;
    public float currentThirst;

    [Header("Скорость падения характеристик")]
    public float hungerDepletionRate = 0.5f; // Голод падает на 0.5 в секунду
    public float thirstDepletionRate = 0.8f; // Жажда падает быстрее
    public float starvationDamage = 2f;      // Урон при нулевом голоде/жажде

    void Start()
    {
        currentHealth = maxHealth;
        currentHunger = maxHunger;
        currentThirst = maxThirst;
    }

    void Update()
    {
        // Уменьшаем голод и жажду со временем
        currentHunger = Mathf.Clamp(currentHunger - hungerDepletionRate * Time.deltaTime, 0, maxHunger);
        currentThirst = Mathf.Clamp(currentThirst - thirstDepletionRate * Time.deltaTime, 0, maxThirst);

        // Если голод или жажда на нуле, отнимаем здоровье
        if (currentHunger == 0 || currentThirst == 0)
        {
            currentHealth -= starvationDamage * Time.deltaTime;
        }

        // Проверка на смерть
        if (currentHealth <= 0)
        {
            Die();
        }
    }

    public void ConsumeItem(float foodValue, float waterValue)
    {
        currentHunger = Mathf.Clamp(currentHunger + foodValue, 0, maxHunger);
        currentThirst = Mathf.Clamp(currentThirst + waterValue, 0, maxThirst);
    }

    void Die()
    {
        Debug.Log("Вы не выжили...");
        // Логика перезапуска игры
    }
}
using UnityEngine;

public class ZombieAI : MonoBehaviour
{
    public Transform player;
    public float walkSpeed = 1f;
    public float runSpeed = 3f;
    public float detectionRadius = 5f;
    public float attackRange = 0.5f;

    private bool isChasing = false;

    void Update()
    {
        if (player == null) return;

        float distanceToPlayer = Vector2.Distance(transform.position, player.position);

        if (distanceToPlayer < detectionRadius)
        {
            isChasing = true;
        }
        else
        {
            isChasing = false;
        }

        if (isChasing)
        {
            if (distanceToPlayer > attackRange)
            {
                // Двигаемся к игроку
                transform.position = Vector2.MoveTowards(transform.position, player.position, runSpeed * Time.deltaTime);
            }
            else
            {
                AttackPlayer();
            }
        }
        else
        {
            // Здесь может быть логика случайного патрулирования (Idle/Wander)
        }
    }

    void AttackPlayer()
    {
        Debug.Log("Зомби кусает игрока!");
        // Вызов получения урона у игрока
    }
}
using UnityEngine;

public class LootSpawner : MonoBehaviour
{
    public enum BuildingType { Residential, Military, Medical }
    public BuildingType type;

    [Header("Списки лута (Префабы)")]
    public GameObject[] residentialLoot;
    public GameObject[] militaryLoot;
    public GameObject[] medicalLoot;

    public Transform[] spawnPoints; // Точки внутри здания, где может появиться лут
    
    [Range(0, 1)]
    public float spawnChance = 0.5f; // Шанс появления предмета в каждой точке

    void Start()
    {
        SpawnLoot();
    }

    void SpawnLoot()
    {
        foreach (Transform spawnPoint in spawnPoints)
        {
            if (Random.value <= spawnChance)
            {
                GameObject itemToSpawn = GetRandomItemByBuildingType();
                if (itemToSpawn != null)
                {
                    Instantiate(itemToSpawn, spawnPoint.position, Quaternion.identity);
                }
            }
        }
    }

    GameObject GetRandomItemByBuildingType()
    {
        switch (type)
        {
            case BuildingType.Residential:
                return residentialLoot[Random.Range(0, residentialLoot.Length)];
            case BuildingType.Military:
                return militaryLoot[Random.Range(0, militaryLoot.Length)];
            case BuildingType.Medical:
                return medicalLoot[Random.Range(0, medicalLoot.Length)];
            default:
                return null;
        }
    }
}
