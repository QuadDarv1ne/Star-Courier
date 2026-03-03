#!/usr/bin/env python3
"""
Star Courier — Текстовая RPG-игра
Главный файл запуска
"""

import sys
from pathlib import Path

# Добавляем src в путь импорта
sys.path.insert(0, str(Path(__file__).parent))

from src.config import GAME_TITLE, VERSION, TEXT_WIDTH
from src.utils import (
    clear_screen, print_header, print_separator,
    print_menu, get_choice, confirm
)
from src.save_system import GameState, SaveManager
from src.characters import CrewManager, Role
from src.dialogues import DialogueManager, create_chapter1_dialogues
from src.abilities import AbilitiesManager, AbilityType, AbilityTier


class Game:
    """Основной класс игры"""
    
    def __init__(self):
        self.game_state = GameState()
        self.dialogue_manager = DialogueManager()
        self.current_chapter = 1
        self.current_scene = "start"
        self.running = True
    
    def start(self):
        """Запуск игры"""
        clear_screen()
        self.show_title_screen()
        self.main_menu()
    
    def show_title_screen(self):
        """Показать заглавный экран"""
        print()
        print_header(f"★ {GAME_TITLE} ★", TEXT_WIDTH + 4)
        print(f"\n  Версия: {VERSION}")
        print("\n  Интерактивная текстовая RPG в космической тематике")
        print()
        print_separator("—", TEXT_WIDTH + 4)
        print()
        input("Нажмите Enter для продолжения...")
    
    def main_menu(self):
        """Главное меню"""
        while self.running:
            clear_screen()
            print_header("ГЛАВНОЕ МЕНЮ", TEXT_WIDTH + 4)
            
            save_manager = SaveManager()
            saves = save_manager.list_saves()
            
            options = ["Новая игра", "Загрузить игру", "Об игре", "Выход"]
            
            if saves:
                print(f"\n  Доступные сохранения ({len(saves)}):")
                for i, save in enumerate(saves[:3], 1):
                    print(f"    {i}. {save['timestamp']} — Глава {save['chapter']}")
                print()
            
            choice = print_menu("Меню", options)
            
            if choice == 0:
                self.new_game()
            elif choice == 1:
                self.load_game_menu()
            elif choice == 2:
                self.about_screen()
            elif choice == 3:
                self.quit_game()
    
    def new_game(self):
        """Новая игра"""
        clear_screen()
        print_header("НОВАЯ ИГРА", TEXT_WIDTH + 4)
        
        if self.game_state.save_data and confirm("Текущий прогресс будет потерян. Продолжить?"):
            pass
        
        self.game_state.new_game()
        
        # Инициализация диалогов первой главы
        dialogues = create_chapter1_dialogues()
        for dialogue in dialogues.values():
            self.dialogue_manager.add_dialogue(dialogue)
        
        print("\n  Начало новой миссии...")
        print("\n  Вы — капитан Макс Велл, командир звездолёта «Элея».")
        print("  Вам предстоит доставить загадочный артефакт и раскрыть его тайны.")
        print()
        
        input("Нажмите Enter для начала главы 1...")
        
        self.play_chapter_1()
    
    def load_game_menu(self):
        """Меню загрузки игры"""
        save_manager = SaveManager()
        saves = save_manager.list_saves()
        
        if not saves:
            print("\n  Нет сохранений!")
            input("Нажмите Enter...")
            return
        
        clear_screen()
        print_header("ЗАГРУЗКА ИГРЫ", TEXT_WIDTH + 4)
        
        for i, save in enumerate(saves, 1):
            print(f"  {i}. {save['timestamp']}")
            print(f"     Глава {save['chapter']}, Сцена: {save['scene']}")
            print()
        
        print("  0. Назад")
        print()
        
        try:
            choice = int(input("Выберите сохранение: ").strip())
            if choice == 0:
                return
            if 1 <= choice <= len(saves):
                filename = saves[choice - 1]["filename"]
                if self.game_state.load_game(filename):
                    print("\n  Игра загружена!")
                    input("Нажмите Enter...")
                    self.play_chapter_1()  # TODO: продолжить с нужной сцены
                else:
                    print("\n  Ошибка загрузки!")
                    input("Нажмите Enter...")
        except ValueError:
            pass
    
    def about_screen(self):
        """Экран «Об игре»"""
        clear_screen()
        print_header("ОБ ИГРЕ", TEXT_WIDTH + 4)
        
        about_text = """
  Star Courier — это интерактивная текстовая RPG в космической тематике.
  
  Вы управляете капитаном Максом Веллом и его командой на борту
  звездолёта «Элея». Ваша задача — доставить загадочный артефакт,
  раскрывая тайны, сражаясь с врагами и развивая отношения.
  
  ОСОБЕННОСТИ:
  
  • Три ветви способностей: Алхимия, Биотика, Психика
  • Интерактивные диалоги с развилками сюжета
  • Развитие отношений с членами экипажа
  • Комбинированные способности в боях и диалогах
  
  РАЗРАБОТЧИК: QuadDarv1ne
  ЛИЦЕНЗИЯ: MIT
        """
        
        print(about_text)
        input("\n  Нажмите Enter для возврата в меню...")
    
    def quit_game(self):
        """Выход из игры"""
        if confirm("Выйти из игры?"):
            self.running = False
            print("\n  До встречи в космосе, капитан! o7")
    
    def play_chapter_1(self):
        """Глава 1: Нежданная встреча"""
        clear_screen()
        print_header("ГЛАВА 1: НЕЖДАННАЯ ВСТРЕЧА", TEXT_WIDTH + 4)
        
        # Сцена 1: Утро на Элее
        self.scene_morning()
        
        if not self.running:
            return
        
        # Сцена 2: Мостик
        self.scene_bridge()
        
        if not self.running:
            return
        
        # Сцена 3: Контакт с пиратами
        self.scene_pirate_contact()
        
        if not self.running:
            return
        
        # Сцена 4: Саботаж
        self.scene_sabotage()
        
        # Конец главы
        self.chapter_end()
    
    def scene_morning(self):
        """Сцена: Утро в каюте"""
        clear_screen()
        print("\n  [Утро на «Элее»]")
        print_separator()
        print()
        
        text = """
  Макс Велл открыл глаза и потянулся, ощущая лёгкую усталость после
  короткого сна. Звук тихого гудения приборов и приглушённое свечение
  панели навигации напоминали, что он снова на мостике своего корабля.
        """
        print(text)
        
        # Диалог с Афиной
        self.dialogue_manager.start_dialogue("morning_briefing")
        self.run_dialogue()
        
        # Установка флага
        self.game_state.set_flag("chapter1_started", True)
        
        input("Нажмите Enter для продолжения...")
    
    def scene_bridge(self):
        """Сцена: Мостик"""
        clear_screen()
        print("\n  [Мостик]")
        print_separator()
        print()
        
        text = """
  Команда собирается для утреннего брифинга.
  
  Рина Мирай: Мы приближаемся к станции Орбис-9. Станция сейчас под
  наблюдением флотского патруля.
  
  Ирина Лебедева: Артефакт стабильно хранится в защитной камере.
  Я продолжаю изучать его свойства.
        """
        print(text)
        print()
        
        # Развитие отношений с Ириной
        choice = get_choice(
            "Как ответить Ирине?",
            ["Продолжай исследования", "Будь осторожна", "Нужна помощь?"]
        )
        
        if choice == 1:
            self.game_state.change_relationship("irina_lebedeva", 5)
            print("\n  Ирина оценила вашу заботу.")
        
        input("Нажмите Enter...")
    
    def scene_pirate_contact(self):
        """Сцена: Контакт с пиратами"""
        clear_screen()
        print("\n  [НЕОЖИДАННЫЙ КОНТАКТ]")
        print_separator()
        print()
        
        text = """
  Внезапно на связь выходит пиратский фрегат «Сирена». На экране
  появляется капитан Селена Ро — обаятельная и уверенная в себе женщина.
  
  Селена Ро: Капитан Велл, у нас есть общее дело. Ваш артефакт
  заинтересовал многих. Может, обсудим условия?
        """
        print(text)
        print()
        
        # Запуск диалога с пиратами
        self.dialogue_manager.start_dialogue("pirate_contact")
        self.run_dialogue()
        
        self.game_state.set_flag("pirate_contact_made", True)
        
        input("Нажмите Enter...")
    
    def scene_sabotage(self):
        """Сцена: Саботаж на корабле"""
        clear_screen()
        print("\n  [ПРОБЛЕМЫ С СИСТЕМОЙ]")
        print_separator()
        print()
        
        text = """
  После контакта с пиратами в техническом отсеке происходит серьёзный
  сбой — система охлаждения выходит из строя.
  
  Алия (по связи): Макс, ситуация серьёзная. Нам нужна ваша помощь.
        """
        print(text)
        print()
        
        # Запуск диалога о саботаже
        self.dialogue_manager.start_dialogue("sabotage_discussion")
        self.run_dialogue()
        
        self.game_state.set_flag("sabotage_discovered", True)
        
        input("Нажмите Enter...")
    
    def run_dialogue(self):
        """Запустить текущий диалог"""
        if not self.dialogue_manager.current_dialogue:
            return
            
        while not self.dialogue_manager.is_finished():
            try:
                text = self.dialogue_manager.get_current_text()
                if text:
                    print(f"\n  {text}\n")

                choices = self.dialogue_manager.get_available_choices(
                    self.game_state.save_data.stats if self.game_state.save_data else {},
                    self.game_state.save_data.inventory if self.game_state.save_data else []
                )

                if not choices:
                    break

                choice_texts = [c.text for c in choices]
                idx = get_choice("Ваш выбор:", choice_texts)

                selected_choice = choices[idx]
                self.dialogue_manager.make_choice(selected_choice.id)

                # Применение эффектов
                if selected_choice.effect_value and selected_choice.effect.name.startswith("RELATIONSHIP"):
                    char_id, amount = selected_choice.effect_value
                    self.game_state.change_relationship(char_id, amount)
                    
            except (IndexError, KeyError, TypeError) as e:
                print(f"\n  [Ошибка диалога: {e}]")
                break
    
    def chapter_end(self):
        """Конец главы"""
        clear_screen()
        print_header("ГЛАВА 1 ЗАВЕРШЕНА", TEXT_WIDTH + 4)
        
        print("\n  Вы успешно завершили первую главу!")
        print("\n  Статистика:")
        print(f"    • Найдено улик саботажа: 1")
        print(f"    • Отношения с экипажем:")
        
        for char in self.game_state.crew_manager.get_all_crew():
            if char.role != Role.CAPTAIN and char.relationship > 0:
                print(f"      — {char.name}: {char.get_relationship_status()}")
        
        print()
        
        # Автосохранение
        self.game_state.save_game("autosave.json")
        print("  Игра автоматически сохранена.")
        
        print("\n  Продолжение следует...")
        input("\n  Нажмите Enter для возврата в меню...")
    
    def save_game(self):
        """Сохранить игру"""
        if self.game_state.save_game():
            print("  Игра сохранена!")
        else:
            print("  Ошибка сохранения!")


def main():
    """Точка входа"""
    try:
        game = Game()
        game.start()
    except KeyboardInterrupt:
        print("\n\n  Игра прервана. До встречи!")
    except Exception as e:
        print(f"\n  Критическая ошибка: {e}")
        if confirm("Сохранить лог ошибки?"):
            with open("error.log", "w", encoding="utf-8") as f:
                import traceback
                traceback.print_exc(file=f)
            print("  Лог сохранён в error.log")


if __name__ == "__main__":
    main()
