# Star Courier: Полный архив проекта

## Описание

Данный архив содержит все материалы, разработанные для расширения проекта Star Courier — интерактивной текстовой RPG в жанре космической научной фантастики.

**Репозитории оригинального проекта:**
- Native (Python): https://github.com/QuadDarv1ne/Star-Courier
- Web (Vue.js): https://github.com/QuadDarv1ne/star-courier-web

---

## Структура архива

```
Star_Courier_Project/
├── documents/           # Документы Word (DOCX)
│   ├── Star_Courier_Complete_Story.docx
│   ├── Star_Courier_Chapters_16_18.docx
│   ├── Star_Courier_Chapters_11_15.docx
│   ├── Star_Courier_Character_Plan.docx
│   ├── Star_Courier_Characters_TNR.docx
│   ├── Star_Courier_Full_Character_List_v2.docx
│   ├── Star_Courier_Technical_Docs.docx
│   └── Star_Courier_Story_Continuation.docx
│
├── python_files/        # Python файлы для интеграции
│   ├── star_courier_dialogues_ch6_10.py
│   ├── star_courier_dialogues_ch11_18.py
│   ├── star_courier_quests_ch6_10.py
│   ├── star_courier_quests_ch11_18.py
│   ├── star_courier_new_characters_dialogues.py
│   ├── star_courier_abilities_advanced.py
│   └── star_courier_path_quests.py
│
├── json_data/           # JSON файлы для веб-версии
│   ├── scenes_ch11_18.json
│   ├── characters_py.json
│   ├── dialogues_py.json
│   ├── abilities_py.json
│   ├── star_courier_main.json
│   └── star_courier_readme.json
│
├── documentation/       # Техническая документация
│   ├── README_DEVELOPERS.md
│   └── Star_Courier_New_Mechanics.md
│
└── README.md           # Этот файл
```

---

## Содержимое

### Документы (documents/)

| Файл | Описание |
|------|----------|
| `Star_Courier_Complete_Story.docx` | Полное описание сюжета (главы 1-18) |
| `Star_Courier_Chapters_16_18.docx` | Финальные главы с тремя концовками |
| `Star_Courier_Chapters_11_15.docx` | Главы 11-15: подготовка к финалу |
| `Star_Courier_Character_Plan.docx` | План развития 26 персонажей по главам |
| `Star_Courier_Characters_TNR.docx` | Полный список персонажей |
| `Star_Courier_Full_Character_List_v2.docx` | Детальные описания персонажей |
| `Star_Courier_Technical_Docs.docx` | Техническая документация |
| `Star_Courier_Story_Continuation.docx` | Продолжение истории (главы 6-10) |

### Python файлы (python_files/)

| Файл | Описание |
|------|----------|
| `star_courier_dialogues_ch6_10.py` | Диалоги для глав 6-10 |
| `star_courier_dialogues_ch11_18.py` | Диалоги для глав 11-18 (100+ диалогов) |
| `star_courier_quests_ch6_10.py` | Квесты для глав 6-10 |
| `star_courier_quests_ch11_18.py` | Квесты для глав 11-18 (20+ квестов) |
| `star_courier_new_characters_dialogues.py` | Диалоги новых персонажей (Зара, Волков, и др.) |
| `star_courier_abilities_advanced.py` | Способности уровней 50-100 + новые механики |
| `star_courier_path_quests.py` | Квесты для трёх путей развития |

### JSON данные (json_data/)

| Файл | Описание |
|------|----------|
| `scenes_ch11_18.json` | Сцены для веб-версии (главы 11-18) |
| `characters_py.json` | Экспорт персонажей |
| `dialogues_py.json` | Экспорт диалогов |
| `abilities_py.json` | Экспорт способностей |

### Документация (documentation/)

| Файл | Описание |
|------|----------|
| `README_DEVELOPERS.md` | Полная документация для разработчиков |
| `Star_Courier_New_Mechanics.md` | Описание новых игровых механик |

---

## Новые игровые механики

### Система Резонанса
- 4 уровня развития
- Связь с Сущностью и аномалиями
- Требуется для финала Слияния

### Система Путей (Глава 13)
- **Альянс** — флот, ресурсы, официальная поддержка
- **Наблюдатель** — древние знания, Psychic усиление
- **Независимость** — свобода, сеть агентов

### Система Концовок (Глава 18)
- **Изгнание** — уничтожение якоря, жертва (любой путь)
- **Договор** — Хранительство Границы (Psychic 70+)
- **Слияние** — трансцендентная эволюция (Psychic 90+)

---

## Персонажи (26)

### Основной экипаж (6)
- **Курьер** — протагонист
- **Мия** — тактик (романтика ✓)
- **Мария** — медик (романтика ✓)
- **Анна** — навигатор (романтика ✓)
- **Сергей** — инженер
- **Дмитрий** — пилот

### Ключевые NPC (20)
- **Вероника** — информатор (романтика ✓)
- **Зара** — рыцарь Ордена (романтика ✓)
- **Кира** — курьер (романтика ✓)
- **Райнер** — наёмник
- **Волков** — капитан, лидер независимых
- **Маркус Рид** — командир Альянса
- **Вера** — учёный
- **Эхо** — древний ИИ
- **Страж Ядра** — последний выживший древней цивилизации
- + 11 других персонажей

---

## Интеграция с существующим проектом

### dialogues.py
```python
from star_courier_dialogues_ch6_10 import DIALOGUES_CHAPTERS_6_10
from star_courier_dialogues_ch11_18 import DIALOGUES_CHAPTERS_11_18

ALL_DIALOGUES = {
    **EXISTING_DIALOGUES,
    **DIALOGUES_CHAPTERS_6_10,
    **DIALOGUES_CHAPTERS_11_18
}
```

### quests.py
```python
from star_courier_quests_ch6_10 import QUESTS_CHAPTERS_6_10
from star_courier_quests_ch11_18 import QUESTS_CHAPTERS_11_18

ALL_QUESTS = {
    **EXISTING_QUESTS,
    **QUESTS_CHAPTERS_6_10,
    **QUESTS_CHAPTERS_11_18
}
```

### abilities.py
```python
from star_courier_abilities_advanced import (
    ALCHEMY_ADVANCED,
    BIOTICS_ADVANCED, 
    PSYCHIC_ADVANCED,
    RESONANCE_ABILITIES,
    PATH_ABILITIES,
    FINAL_BATTLE_ABILITIES
)
```

---

## Статистика проекта

- **Главы:** 18 (4 арки)
- **Персонажи:** 26
- **Романтические линии:** 6
- **Диалоги:** 200+
- **Квесты:** 40+
- **Способности:** 50+ (уровни 50-100)
- **Концовки:** 3 (с вариациями по путям и романтике)

---

## Автор

Материалы разработаны для расширения проекта Star Courier.

**Оригинальные репозитории:**
- https://github.com/QuadDarv1ne/Star-Courier
- https://github.com/QuadDarv1ne/star-courier-web

---

*Версия архива: 1.0*
*Дата создания: 2025*
