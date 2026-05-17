# Star Courier: Рабочие заметки

## Статус на 17.05.2026

---

## АУДИТ ИНТЕГРАЦИИ (17.05.2026) — РЕАЛЬНОЕ ПОЛОЖЕНИЕ ДЕЛ

### Полностью интегрировано (работает в геймплее)
- [x] config, gameplay, save_system, utils, colors, ascii_art
- [x] characters, dialogues, abilities, items, quests
- [x] Диалоги глав 1-5, 6-10, 11-13, 14-18
- [x] Квесты глав 11-12, 14-18, path_quests
- [x] romance_scenes, ending_scenes, mental_state
- [x] random_events (базовый), system_check
- [x] **FactionManager** — сохранение/загрузка репутации фракций (исправлено 17.05.2026)

### Частично интегрировано (инициализировано, но не вызывается в сценах)
- [ ] **FactionManager** — репутация не меняется ни в одной сцене геймплея
- [ ] **ResonanceSystem** — сохранён в сейвах, но нет триггеров в геймплее
- [ ] **PathSystem** — сохранён в сейвах, choose_path() есть, но не вызывается
- [ ] **relationship_enhancements.py** — менеджер создан, не вызывается
- [ ] **ending_system.py** — TODO-баг: abilities захардкожены в `[]`

### Мёртвые импорты (импортируются в main.py, но НЕ используются)
- [ ] **random_events_v5.py** — SPACE_EVENTS, STATION_EVENTS не передаются в систему
- [ ] **abilities_advanced_v5.py** — ALCHEMY/BIOTICS/PSYCHIC_ADVANCED не подключены
- [ ] **achievements_v5.py** — 49 ачивок без системы трекинга
- [ ] **backstories_v5.py** — 6 предысторий не применяются
- [ ] **entity_lore_v5.py** — лор без системы просмотра (кодекс)
- [ ] **banters_v5.py** — бантеры экипажа не вызываются
- [ ] **adult_romance_v5.py** — 15 линий + интимные сцены не подключены
- [ ] **dialogues_ch11_18.py** — CHAPTER_11/12_DIALOGUES (сырые dicts) не используются

### НЕ интегрировано (файлы существуют, но НИГДЕ не импортируются)
- [ ] **quests_ch6_10.py** — квесты глав 6-10 (~20 квестов)
- [ ] **quests_ch11_18.py** — квесты глав 11-18 (несовместимый dict-формат)
- [ ] **items_v5.py** — ~600 строк: оружие, броня, предметы, крафт
- [ ] **locations_v5.py** — ~550 строк: 15+ локаций, 8 секторов, события
- [ ] **new_characters_dialogues.py** — 5+ персонажей (Zara, Marcus, Volkov...)
- [ ] **path_quests_v5.py** — ~800 строк: 5 путей вместо текущих 3
- [ ] **romance_extended_v5.py** — ~870 строк: 5 дополнительных романтических линий
- [ ] **romance_scenes_extended_v5.py** — расширенные интимные сцены
- [ ] **scenes_ch1_2.py** — дублирует inline-методы Game класса

### Известные баги
- [ ] `save_system.py:510` — `check_ending_unlock()`: abilities = `[]` вместо реальных
- [ ] `scenes_ch14_18.py:147` — лояльность команды захаркожена `True`

---

## ПЛАН ИНТЕГРАЦИИ (по приоритету)

### Этап 1: Критичный контент (~4000 строк)
1. [ ] **quests_ch6_10.py** — подключить квесты глав 6-10 в new_game()
2. [ ] **items_v5.py** — интегрировать базу предметов в ItemDatabase
3. [ ] **locations_v5.py** — система локаций + исследование в геймплее
4. [ ] **new_characters_dialogues.py** — загрузить диалоги новых персонажей

### Этап 2: Системы геймплея
5. [ ] **faction_manager** — вызовы в сценах (репутация за действия)
6. [ ] **random_events_v5.py** — подключить события к RandomEventsManager
7. [ ] **path_quests_v5.py** — заменить/дополнить path_quests.py
8. [ ] **abilities_advanced_v5.py** — подключить к AdvancedAbilitiesManager
9. [ ] **achievements_v5.py** — создать AchievementManager, трекинг

### Этап 3: Контент и улучшения
10. [ ] **backstories_v5.py** — экран выбора предыстории при новой игре
11. [ ] **entity_lore_v5.py** — система кодекса (просмотр лора)
12. [ ] **banters_v5.py** — триггеры бантеров при путешествиях
13. [ ] **romance_extended_v5.py** — 5 новых романтических линий
14. [ ] **romance_scenes_extended_v5.py** — расширенные сцены

### Этап 4: Исправления
15. [ ] **save_system.py:510** — исправить check_ending_unlock()
16. [ ] **scenes_ch14_18.py:147** — проверить реальную лояльность
17. [ ] **quests_ch11_18.py** — конвертировать dict-формат в Quest objects

### Этап 5: Тестирование
18. [ ] Пройти все 3 пути (Альянс/Наблюдатель/Независимость)
19. [ ] Проверить все 3 финала
20. [ ] Проверить романтические концовки
21. [ ] Протестировать способности 50-100 уровня

---

## Git-статус
- Ветки: **master** (единственная, origin/master)
- dev удалена, всё в main
- Последний коммит: `f407506` — merge FactionManager

---

## Заметки

### Архив с дополнениями
Был архив `Star_Courier_Project_Complete_EXTRACTED/` с файлами:
- `python_files/` — исходные Python-файлы (диалоги, квесты, способности)
- `documents/` — docx сценарии
- `documentation/` — README_DEVELOPERS.md, Star_Courier_New_Mechanics.md

Многие файлы из архива были скопированы в `src/` как `_v5` версии,
но **не все были подключены к геймплею**. См. раздел «НЕ интегрировано» выше.

### Структура src/ (49 файлов)
Ядро: config, gameplay, save_system, utils, characters, abilities, items, quests, dialogues
Главы: chapters_1_5, dialogues_ch6_10, dialogues_ch11_18, dialogues_ch14_18, quests_ch11_12, quests_ch14_18, path_quests
Системы: resonance, path_system, ending_system, mental_state, random_events, advanced_abilities, faction_manager
V5: factions_v5, items_v5, locations_v5, path_quests_v5, random_events_v5, abilities_advanced_v5,
    achievements_v5, backstories_v5, entity_lore_v5, banters_v5, adult_romance_v5,
    romance_extended_v5, romance_scenes_extended_v5
Утилиты: ascii_art, colors, system_check
Неиспользуемые: scenes_ch1_2, quests_ch6_10, quests_ch11_18, new_characters_dialogues
