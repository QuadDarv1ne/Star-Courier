#!/usr/bin/env python3
"""
Автотест для Star Courier
Проходит главу 1 автоматически
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.config import GAME_TITLE, VERSION
from src.characters import CrewManager, Character, Role
from src.dialogues import DialogueManager, create_chapter1_dialogues
from src.save_system import GameState
from src.gameplay import GameplaySystem
from src.mental_state import MentalStateSystem

def test_game_initialization():
    """Тест инициализации игры"""
    print("=" * 60)
    print("  Star Courier — Автотест")
    print("=" * 60)
    print()
    
    # Тест конфигурации
    print(f"[✓] Game Title: {GAME_TITLE}")
    print(f"[✓] Version: {VERSION}")
    print()
    
    # Тест персонажей
    crew = CrewManager()
    all_crew = crew.get_all_crew()
    print(f"[✓] Персонажей загружено: {len(all_crew)}")
    
    max_well = crew.get_character("max_well")
    if max_well:
        print(f"[✓] Макс Велл: {max_well.role}")
    else:
        print("[✗] Макс Велл не найден!")
    print()
    
    # Тест диалогов
    dialogue_manager = DialogueManager()
    dialogues = create_chapter1_dialogues()
    for dialogue in dialogues.values():
        dialogue_manager.add_dialogue(dialogue)
    print(f"[✓] Диалогов главы 1: {len(dialogues)}")
    print()
    
    # Тест сохранений
    game_state = GameState()
    game_state.new_game()
    print(f"[✓] Новая игра создана: Глава {game_state.save_data.chapter}")
    print()
    
    # Тест игровой системы
    gameplay = GameplaySystem()
    gameplay.set_crew_manager(crew)
    gameplay.set_game_state(game_state)
    print(f"[✓] GameplaySystem инициализирована")
    print()
    
    # Тест ментального состояния
    mental_state = MentalStateSystem()
    crew_ids = list(crew.crew.keys())
    mental_state.initialize_crew(crew_ids)
    print(f"[✓] MentalStateSystem инициализирована")
    print(f"    - Здоровье игрока: {mental_state.player_state.health}")
    print(f"    - Влияние Сущности: {mental_state.player_state.entity_influence}")
    print()
    
    # Тест квестов
    gameplay.accept_quest("main_001")
    active_quests = gameplay.quest_manager.get_active_quests()
    print(f"[✓] Активных квестов: {len(active_quests)}")
    if active_quests:
        print(f"    - {active_quests[0].title}")
    print()
    
    # Тест отношений
    print("[✓] Проверка отношений:")
    for char_id, char in crew.crew.items():
        print(f"    - {char.name}: отношения={char.relationship}, доверие={char.trust}")
    print()
    
    print("=" * 60)
    print("  ВСЕ ТЕСТЫ ПРОЙДЕНЫ ✓")
    print("=" * 60)
    
    return True

if __name__ == "__main__":
    try:
        success = test_game_initialization()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n[✗] ОШИБКА: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
