# Руководство для контрибьюторов Star Courier

Спасибо за интерес к проекту! Это руководство поможет вам начать вносить свой вклад.

## Быстрый старт

### 1. Форк и клонирование

```bash
# Форкните репозиторий через GitHub UI, затем:
git clone https://github.com/YOUR_USERNAME/Star-Courier.git
cd Star-Courier
```

### 2. Настройка окружения

```bash
# Создайте виртуальное окружение
python -m venv venv

# Активируйте
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/macOS

# Установите зависимости
pip install -r requirements.txt
```

### 3. Запуск игры

```bash
python main.py
```

## Как внести вклад

### Идеи и предложения

- Откройте [Issue](https://github.com/QuadDarv1ne/Star-Courier/issues) с описанием идеи
- Используйте метки: `enhancement`, `idea`, `question`

### Исправление ошибок

1. Найдите или создайте Issue с описанием бага
2. Создайте ветку: `git checkout -b fix/issue-123`
3. Исправьте ошибку
4. Напишите тест (если применимо)
5. Отправьте Pull Request

### Новый контент

#### Добавление диалога

Создайте файл в `src/dialogues/` или добавьте в существующий:

```python
from src.dialogues import Dialogue, DialogueNode, Choice, ChoiceEffect

new_dialogue = Dialogue(
    id="unique_id",
    title="Название диалога",
    start_node="start"
)

new_dialogue.add_node(DialogueNode(
    id="start",
    speaker="Имя персонажа",
    text="Текст реплики",
    choices=[
        Choice(
            id="choice_1",
            text="Вариант ответа",
            next_node="next_node_id",
            effect=ChoiceEffect.RELATIONSHIP_UP,
            effect_value=("character_id", 5)
        )
    ]
))
```

#### Добавление персонажа

В `src/characters.py` добавьте в `_init_default_crew`:

```python
self.add_character(Character(
    id="unique_id",
    name="Имя Фамилия",
    role=Role.ROLE_NAME,
    bio="Краткая биография",
    appearance="Описание внешности",
    personality="Характер",
    motivation="Цели и мотивация"
))
```

#### Добавление способности

В `src/abilities.py` добавьте в `_init_default_abilities`:

```python
self.abilities["ability_id"] = AlchemyAbility(  # или BioticAbility, PsychicAbility
    id="ability_id",
    name="Название",
    description="Описание",
    ability_type=AbilityType.ALCHEMY,
    tier=AbilityTier.BASIC,
    energy_cost=10,
    # дополнительные параметры типа
)
```

## Стандарты кода

### Стиль кода

- Следуйте [PEP 8](https://pep8.org/)
- Используйте 4 пробела для отступов
- Максимальная длина строки — 100 символов
- Имена переменных: `snake_case`
- Имена классов: `PascalCase`
- Константы: `UPPER_CASE`

### Документирование

```python
def function_name(param1: str, param2: int) -> bool:
    """
    Краткое описание функции.
    
    Args:
        param1: Описание параметра 1
        param2: Описание параметра 2
    
    Returns:
        Описание возвращаемого значения
    
    Raises:
        ExceptionType: Когда возникает ошибка
    """
    pass
```

### Типизация

Используйте аннотации типов:

```python
from typing import Dict, List, Optional, Union

def process_data(
    items: List[str],
    count: Optional[int] = None
) -> Dict[str, int]:
    pass
```

## Структура коммитов

### Формат сообщения

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Типы коммитов

- `feat` — новая функция
- `fix` — исправление ошибки
- `docs` — изменения в документации
- `style` — форматирование, отступы
- `refactor` — рефакторинг кода
- `test` — добавление тестов
- `chore` — изменения в сборке, зависимости

### Примеры

```
feat(dialogues): добавлен диалог с Селеной Ро

- Создан новый диалог pirate_contact
- Добавлено 5 узлов и 12 вариантов выбора
- Реализованы эффекты влияния на отношения

Closes #42
```

```
fix(save_system): исправлена ошибка загрузки сохранений

- Исправлена ошибка кодировки при чтении JSON
- Добавлена обработка отсутствующих файлов

Fixes #38
```

## Тестирование

### Запуск игры

Перед отправкой PR убедитесь, что:

```bash
# Игра запускается без ошибок
python main.py

# Все диалоги работают
# Сохранение/загрузка функционируют
```

### Проверка кода

```bash
# Проверка стиля (если установлен flake8)
flake8 src/

# Проверка типов (если установлен mypy)
mypy src/
```

## Pull Request процесс

### Перед отправкой

- [ ] Код следует стандартам проекта
- [ ] Добавлены необходимые комментарии
- [ ] Игра тестируется локально
- [ ] Обновлена документация (если нужно)

### Шаблон PR

```markdown
## Описание
Краткое описание изменений

## Тип изменений
- [ ] Новая функция
- [ ] Исправление ошибки
- [ ] Документация
- [ ] Рефакторинг

## Связанные Issues
Closes #123

## Чеклист
- [ ] Тесты пройдены
- [ ] Документация обновлена
- [ ] Код отформатирован
```

## Вопросы?

- Откройте [Issue](https://github.com/QuadDarv1ne/Star-Courier/issues) для вопросов
- Присоединяйтесь к обсуждению в существующих Issues

---

**Спасибо за ваш вклад!** 🚀
