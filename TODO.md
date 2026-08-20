# Star Courier: Рабочие заметки

## Статус на 20.08.2026

---

## АУДИТ ИНТЕГРАЦИИ (20.08.2026) — РЕАЛЬНОЕ ПОЛОЖЕНИЕ ДЕЛ

### Полностью интегрировано (работает в геймплее)
- [x] config, gameplay, save_system, utils, colors, ascii_art
- [x] characters, dialogues, abilities, items, quests
- [x] Диалоги глав 1-5, 6-10, 11-13, 14-18
- [x] Квесты глав 11-12, 14-18, path_quests
- [x] romance_scenes, ending_scenes, mental_state
- [x] random_events (базовый), system_check
- [x] **FactionManager** — сохранение/загрузка репутации фракций
- [x] **ResonanceSystem** — триггеры в геймплее (конфликты, артефакты, случайные события)
- [x] **PathSystem** — вызов choose_path() из экрана выбора пути
- [x] **relationship_enhancements.py** — менеджер создан
- [x] **quests_ch6_10.py** — зарегистрированы в new_game()
- [x] **banters_v5.py** — trigger_crew_banter() интегрирован
- [x] **random_events_v5.py** — trigger_random_event() интегрирован
- [x] **achievements_v5.py** — check_achievements() вызывается в achievements_screen()
- [x] **backstories_v5.py** — backstories_screen() работает
- [x] **entity_lore_v5.py** — codex_screen() работает

### Исправленные баги
- [x] `save_system.py:519` — check_ending_unlock(): empathy рассчитывается через _calculate_empathy()
- [x] `scenes_ch14_18.py:147` — лояльность команды вычисляется динамически (уже было исправлено)
- [x] `abilities.py` — добавлен метод add_xp() для прогрессии способностей
- [x] `main.py` — все проверки None для get_character() исправлены
- [x] `main.py` — добавлен Optional import для _find_char_id_by_name

### Новый функционал (v5.1)
- [x] trigger_crew_banter() — случайные бантеры экипажа
- [x] trigger_random_event() — случайные события с эффектами
- [x] path_choice_screen() — экран выбора Пути
- [x] ending_preview_screen() — экран предпросмотра концовок
- [x] faction reputation changes в сценах (пираты, артефакт)
- [x] resonance experience в сценах (конфликты, артефакты, события)
- [x] _calculate_empathy() — расчёт эмпатии для концовок
- [x] _collect_ending_abilities() — сбор способностей для концовок
- [x] Статус фракций и Пути в конце глав

---

## ПЛАН ДАЛЬНЕЙШЕЙ ИНТЕГРАЦИИ (по приоритету)

### Этап 1: Контент
1. [ ] **items_v5.py** — интегрировать базу предметов в ItemDatabase
2. [ ] **locations_v5.py** — система локаций + исследование в геймплее
3. [ ] **new_characters_dialogues.py** — загрузить диалоги новых персонажей
4. [ ] **path_quests_v5.py** — заменить/дополнить path_quests.py

### Этап 2: Системы геймплея
5. [ ] **quests_ch11_18.py** — конвертировать dict-формат в Quest objects
6. [ ] **abilities_advanced_v5.py** — подключить к AdvancedAbilitiesManager
7. [ ] **romance_extended_v5.py** — 5 новых романтических линий
8. [ ] **romance_scenes_extended_v5.py** — расширенные сцены

### Этап 3: Улучшения
9. [ ] **relationship_enhancements.py** — подарочно-миссионная система
10. [ ] **scenes_ch1_2.py** — перенести в inline методы Game
11. [ ] Добавить больше триггеров бантеров в сцены
12. [ ] Добавить больше случайных событий в главы

### Этап 4: Тестирование
13. [ ] Пройти все 3 пути (Альянс/Наблюдатель/Независимость)
14. [ ] Проверить все 3 финала
15. [ ] Проверить романтические концовки
16. [ ] Протестировать способности 50-100 уровня

---

## Git-статус
- Ветки: **master** (единственная, origin/master)
- dev удалена, всё в main
- Последний коммит: `f407506` — merge FactionManager

---

## Заметки

### Архив с дополнениями
Была папка `Star_Courier_Project_Complete_EXTRACTED/` с файлами:
- `python_files/` — исходные Python-файлы (диалоги, квесты, способности)
- `documents/` — docx сценарии
- `documentation/` — README_DEVELOPERS.md, Star_Courier_New_Mechanics.md

Многие файлы из архива были скопированы в `src/` как `_v5` версии,
и **большая часть теперь интегрирована в геймплей**.

### Структура src/ (49 файлов)
Ядро: config, gameplay, save_system, utils, characters, abilities, items, quests, dialogues
Главы: chapters_1_5, dialogues_ch6_10, dialogues_ch11_18, dialogues_ch14_18, quests_ch11_12, quests_ch14_18, path_quests
Системы: resonance, path_system, ending_system, mental_state, random_events, advanced_abilities, faction_manager
V5: factions_v5, items_v5, locations_v5, path_quests_v5, random_events_v5, abilities_advanced_v5,
    achievements_v5, backstories_v5, entity_lore_v5, banters_v5, adult_romance_v5,
    romance_extended_v5, romance_scenes_extended_v5
Утилиты: ascii_art, colors, system_check
Интегрировано: quests_ch6_10, relationship_enhancements
Неиспользуемые: scenes_ch1_2, quests_ch11_18 (dict format), new_characters_dialogues
