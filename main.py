#!/usr/bin/env python3
"""
Star Courier — Текстовая RPG-игра
Главный файл запуска
"""

import sys
from pathlib import Path

# Добавляем src в путь импорта
sys.path.insert(0, str(Path(__file__).parent))

from src.config import GAME_TITLE, VERSION, TEXT_WIDTH, DEFAULT_HP, DEFAULT_ENERGY
from src.utils import (
    clear_screen, print_header, print_separator,
    print_menu, get_choice, confirm
)
from src.save_system import GameState, SaveManager
from src.characters import CrewManager
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
        self.loaded_scene = None  # Сцена для загрузки из сохранения
    
    def start(self):
        """Запуск игры"""
        clear_screen()
        self.show_title_screen()
        self.main_menu()
    
    def show_title_screen(self):
        """Показать заглавный экран"""
        print()
        print_header(f"* {GAME_TITLE} *", TEXT_WIDTH + 4)
        print(f"\n  Версия: {VERSION}")
        print("\n  Интерактивная текстовая RPG в космической тематике")
        print()
        print_separator("-", TEXT_WIDTH + 4)
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
                    # Сохраняем сцену для продолжения
                    self.loaded_scene = self.game_state.save_data.scene if self.game_state.save_data else None
                    input("Нажмите Enter...")
                    self.play_chapter_1()
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
        print("\n  Станция Орбис-9. 2187 год.")
        print("  Корабль «Элея» с ценным грузом на борту.")
        input("\n  [Нажмите Enter для начала...]")

        self.scene_morning()
        if not self.running:
            return

        self.scene_bridge()
        if not self.running:
            return

        self.scene_pirate_contact()
        if not self.running:
            return

        self.scene_sabotage()
        if not self.running:
            return

        self.scene_discovery()
        if not self.running:
            return

        self.chapter_end()
    
    def scene_morning(self):
        """Сцена: Утро в каюте"""
        clear_screen()
        print("\n  [Глава 1: Нежданная встреча]")
        print_separator("—")
        print("\n  [Утро на «Элее»]")
        print()

        text = """
  Тихое гудение систем корабля разбудило Макса Велла раньше, чем должен
  был сработать будильник. Он открыл глаза и несколько секунд смотрел в
  потолок каюты — матовое стекло, за которым медленно перемещались звёзды.

  Корабль спал. Но для капитана это означало лишь одно — что-то не так.
        """
        print(text)
        input("  [Нажмите Enter...]")

        print("\n  Панель у кровати мягко засветилась:")
        print("  > 06:30 по звездному времени")
        print("  > Температура: 22°C")
        print("  > Следующая остановка: станция Орбис-9")
        print("  > Статус груза: в норме")
        print()
        input("  [Нажмите Enter...]")

        # Диалог с Афиной
        self.dialogue_manager.start_dialogue("morning_briefing")
        self.run_dialogue()

        self.game_state.set_flag("chapter1_started", True)
    
    def scene_bridge(self):
        """Сцена: Мостик"""
        clear_screen()
        print("\n  [МОСТИК]")
        print_separator("—")
        print()

        text = """
  Мостик встретил Макса привычным гулом — сдержанным, деловитым.
  Экраны навигации мерцали голубым, отбрасывая тени на лица команды.

  Рина Мирай, не отрываясь от консоли:
  — Капитан, мы приближаемся к станции Орбис-9. Станция сейчас под
    наблюдением флотского патруля.

  Ирина Лебедева повернулась от своего терминала:
  — Артефакт стабильно хранится в защитной камере. Я продолжаю
    изучать его свойства.

  Она помолчала, затем добавила тише:
  — Но там что-то есть, капитан. Что-то... живое.
        """
        print(text)
        print()

        choice = get_choice(
            "Как ответить Ирине?",
            ["Продолжай исследования", "Будь осторожна", "Нужна помощь?"]
        )

        if choice == 0:
            self.game_state.change_relationship("irina_lebedeva", 5)
            print("\n  Ирина кивнула, не скрывая удовлетворения.")
            print("  — Обязательно. Я близка к открытию.")
        elif choice == 1:
            self.game_state.change_relationship("irina_lebedeva", 3)
            print("\n  — Буду, капитан. Обещаю.")
        else:
            print("\n  — Спасибо, но пока всё под контролем.")
            print("  Хотя... если найдёте время, загляните в лабораторию.")

        input("\n  [Нажмите Enter...]")
    
    def scene_pirate_contact(self):
        """Сцена: Контакт с пиратами"""
        clear_screen()
        print("\n  [ТРЕВОГА!]")
        print_separator("—")
        print()

        text = """
  Тревожный сигнал прозвучал внезапно, разрезав тишину мостика.
  На главном экране возникло изображение — женщина в пиратской форме,
  с уверенной улыбкой и холодными глазами.

  Селена Ро, капитан фрегата «Сирена»:
  — Капитан Велл... наконец-то мы на связи. У нас есть общее дело.
    Ваш артефакт заинтересовал многих. Может, обсудим условия,
    прежде чем станем врагами?

  На заднем плане виднелись силуэты вооружённых людей.
        """
        print(text)
        print()

        self.dialogue_manager.start_dialogue("pirate_contact")
        self.run_dialogue()

        self.game_state.set_flag("pirate_contact_made", True)
    
    def scene_sabotage(self):
        """Сцена: Саботаж на корабле"""
        clear_screen()
        print("\n  [СБОЙ СИСТЕМ]")
        print_separator("—")
        print()

        text = """
  Свет на мостике мигнул. На секунду погас, затем вернулся — тусклее.
  Из динадоников донёсся голос Алии, напряжённый, без обычной уверенности:

  — Макс, у нас проблема. Система охлаждения вышла из строя.
    Это не случайность, капитан. Кто-то намеренно вывел её из строя.

  На экране появились данные: температура в техническом отсеке
  росла. Быстрее, чем должна была.

  Рина обернулась:
  — До станции 4 часа. Если температура продолжит расти...
        """
        print(text)
        print()

        self.dialogue_manager.start_dialogue("sabotage_discussion")
        self.run_dialogue()

        self.game_state.set_flag("sabotage_discovered", True)

    def scene_discovery(self):
        """Сцена: Находка в техническом отсеке"""
        clear_screen()
        print("\n  [ТЕХНИЧЕСКИЙ ОТСЕК]")
        print_separator("—")
        print()

        text = """
  Температура в отсеке выросла до 45°C. Аварийное освещение мигало
  красным, отбрасывая длинные тени на металлические стены.

  Алия стояла у открытой панели, её лицо было серьёзным.

  — Капитан, смотрите. Кто-то отключил предохранители вручную.
    И вот это... — она протянула обгоревший чип.
        """
        print(text)
        print()

        choice = get_choice(
            "Ваши действия?",
            ["Взять чип", "Осмотреть панель", "Поговорить с Алией"]
        )

        if choice == 0:
            print("\n  Чип был повреждён, но на нём виден логотип:")
            print("  «НейроТех Индастриз» — производитель систем безопасности.")
            self.game_state.set_flag("found_chip", True)
        elif choice == 1:
            print("\n  На панели — следы вскрытия. Профессиональная работа.")
            self.game_state.set_flag("examined_panel", True)
        else:
            print("\n  — Я такого раньше не видела, — Алия нахмурилась.")
            print("  — Но кто-то знал, где искать.")
            # Запуск диалога конфронтации
            self.dialogue_manager.start_dialogue("alia_confrontation")
            self.run_dialogue()
            self.game_state.change_relationship("alia_naar", 2)

        self.game_state.set_flag("discovery_complete", True)
        input("\n  [Нажмите Enter...]")
    
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

                idx = get_choice("Ваш выбор:", [c.text for c in choices])
                selected_choice = choices[idx]
                self.dialogue_manager.make_choice(selected_choice.id)

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

        # Показываем найденные улики
        clues_found = sum([
            self.game_state.get_flag("found_chip", False),
            self.game_state.get_flag("examined_panel", False),
        ])
        print(f"    • Найдено улик: {clues_found}/2")

        # Отношения
        print("    • Отношения с экипажем:")
        for name, status in self.game_state.get_crew_relationships():
            print(f"      — {name}: {status}")

        # Последствия выборов
        print("\n  Последствия ваших решений:")
        if self.game_state.get_flag("pirate_contact_made", False):
            print("    • Пираты знают о вас. Селена Ро запомнила встречу.")
        if self.game_state.get_flag("discovery_complete", False):
            print("    • Саботаж расследуется. Команда ждёт ваших приказов.")

        print()
        self.game_state.save_game("autosave.json")
        print("  Игра автоматически сохранена.")
        print("\n  ═══════════════════════════════════════")
        print("  ГЛАВА 2: СЛЕД В ПУСТОТЕ")
        print("  Скоро доступна...")
        print("  ═══════════════════════════════════════")
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
