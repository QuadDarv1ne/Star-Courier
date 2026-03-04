#!/usr/bin/env python3
"""
Star Courier — Текстовая RPG-игра
Главный файл запуска
"""

import sys
import logging
from pathlib import Path

# Настройка логгирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('game.log', encoding='utf-8', mode='a'),
    ]
)
logger = logging.getLogger('main')

# Добавляем src в путь импорта
sys.path.insert(0, str(Path(__file__).parent))

from src.config import GAME_TITLE, VERSION, TEXT_WIDTH
from src.utils import (
    clear_screen, print_header, print_separator,
    print_menu, get_choice, confirm, list_saves_menu
)
from src.colors import Colors, colorize, get_character_color, print_alert
from src.ascii_art import print_art
from src.save_system import GameState
from src.characters import CrewManager
from src.dialogues import DialogueManager, create_chapter1_dialogues, create_chapter2_dialogues
from src.gameplay import GameplaySystem


class Game:
    """Основной класс игры"""

    def __init__(self):
        self.game_state = GameState()
        self.dialogue_manager = DialogueManager()
        self.gameplay = GameplaySystem()
        self.current_chapter = 1
        self.current_scene = "start"
        self.running = True
        self.loaded_scene = None  # Сцена для загрузки из сохранения
    
    def start(self):
        """Запуск игры"""
        clear_screen()
        
        # Проверка поддержки цвета
        if not Colors.supports_color():
            Colors.disable()
        
        self.show_title_screen()
        self.main_menu()
    
    def show_title_screen(self):
        """Показать заглавный экран"""
        print()
        print_art("eleia")
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

            saves = self.game_state.save_manager.list_saves()

            options = ["Новая игра", "Загрузить игру", "Об игре", "Выход"]

            list_saves_menu(saves)
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

        # Инициализация диалогов второй главы
        dialogues_ch2 = create_chapter2_dialogues()
        for dialogue in dialogues_ch2.values():
            self.dialogue_manager.add_dialogue(dialogue)

        # Инициализация игровой системы
        self.gameplay.set_crew_manager(self.game_state.crew_manager)
        self.gameplay.set_game_state(self.game_state)

        # Выдача стартового квеста
        self.gameplay.accept_quest("main_001")

        print("\n  Начало новой миссии...")
        print("\n  Вы — капитан Макс Велл, командир звездолёта «Элея».")
        print("  Вам предстоит доставить загадочный артефакт и раскрыть его тайны.")
        print()

        input("Нажмите Enter для начала главы 1...")

        self.play_chapter_1()
    
    def load_game_menu(self):
        """Меню загрузки игры"""
        saves = self.game_state.save_manager.list_saves()

        if not saves:
            print("\n  Нет сохранений!")
            input("Нажмите Enter...")
            return

        clear_screen()
        print_header("ЗАГРУЗКА ИГРЫ", TEXT_WIDTH + 4)
        list_saves_menu(saves)
        print("\n  0. Назад\n")

        try:
            choice = int(input("Выберите сохранение: ").strip())
            if choice == 0:
                return
            if 1 <= choice <= len(saves):
                filename = saves[choice - 1]["filename"]
                if self.game_state.load_game(filename):
                    print("\n  Игра загружена!")
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
        print_art("station")
        print("\n  Станция Орбис-9. 2187 год.")
        print("  Корабль «Элея» с ценным грузом на борту.")
        input("\n  [Нажмите Enter для начала...]")

        self.scene_morning()
        if not self.running:
            return

        self.scene_bridge()
        if not self.running:
            return

        self.scene_lab()
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

        self.scene_combat()
        if not self.running:
            return

        self.scene_artifact_examination()
        if not self.running:
            return

        self.chapter_end()
    
    def scene_morning(self):
        """Сцена: Утро в каюте"""
        clear_screen()
        print("\n  [Глава 1: Нежданная встреча]")
        print_separator("-")
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

    def scene_lab(self):
        """Сцена: Лаборатория с артефактом"""
        clear_screen()
        print("\n  [ЛАБОРАТОРИЯ]")
        print_separator("-")
        print()

        text = """
  Лаборатория встретила Макса тихим гудением сканеров. Ирина Лебедева
  склонилась над терминалом, её лицо освещалось голубым светом голограммы.

  В центре комнаты, за защитным полем, пульсировал артефакт.
        """
        print(text)
        print_art("artifact")

        print("\n  Ирина обернулась:")
        print("  — Капитан! Я как раз хотела вам доложить...")
        print()

        # Проверяем отношения с Ириной
        irina_rel = self.game_state.crew_manager.get_character("irina_lebedeva").relationship

        if irina_rel >= 40:
            options = ["Что с артефактом?", "Есть опасность?", "Ты сегодня прекрасно выглядишь", "Нужна помощь?"]
        else:
            options = ["Что с артефактом?", "Есть опасность?", "Нужна помощь?"]

        choice = get_choice("Что спросить?", options)

        if choice == 0:
            print("\n  — Энергетические всплески участились. Это... необычно.")
            print("  — Такое ощущение, что он реагирует на что-то.")
            self.game_state.change_relationship("irina_lebedeva", 3)
            self.game_state.set_flag("lab_artifact_discussed", True)
            # Обновляем квест исследования
            self.gameplay.on_explore_location("lab")
        elif choice == 1:
            print("\n  — Пока нет. Но я продолжаю мониторинг.")
            print("  — Если что-то изменится — вы узнаете первым.")
            self.game_state.change_trust("irina_lebedeva", 5)
        elif choice == 2 and irina_rel >= 40:
            print("\n  Ирина слегка покраснела:")
            print("  — Ох, капитан... вы всегда находите нужные слова.")
            print("  — Но спасибо. Мне... приятно.")
            self.game_state.change_relationship("irina_lebedeva", 12)
            self.game_state.change_trust("irina_lebedeva", 5)
            self.game_state.set_flag("irina_flirted", True)
        else:
            idx = 2 if irina_rel >= 40 else 1
            print("\n  — Да, собственно... можете передать Афии, что нужны")
            print("    дополнительные данные по фоновому излучению.")
            self.game_state.change_relationship("irina_lebedeva", 2)
            self.game_state.change_relationship("athena", 2)

        input("\n  [Нажмите Enter...]")
    
    def scene_bridge(self):
        """Сцена: Мостик"""
        clear_screen()
        print("\n  [МОСТИК]")
        print_separator("-")
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

        # Проверяем, была ли уже сцена в лаборатории
        lab_visited = self.game_state.get_flag("lab_artifact_discussed", False)

        if lab_visited:
            options = ["Продолжай исследования", "Будь осторожна", "Ты права насчёт артефакта"]
        else:
            options = ["Продолжай исследования", "Будь осторожна", "Нужна помощь?"]

        choice = get_choice("Как ответить Ирине?", options)

        if choice == 0:
            self.game_state.change_relationship("irina_lebedeva", 5)
            print("\n  Ирина кивнула, не скрывая удовлетворения.")
            print("  — Обязательно. Я близка к открытию.")
        elif choice == 1:
            self.game_state.change_relationship("irina_lebedeva", 3)
            print("\n  — Буду, капитан. Обещаю.")
        else:
            if lab_visited:
                print("\n  — Да... после того, что я видела в лаборатории...")
                print("  — Это сложно объяснить, но артефакт реагирует на нас.")
                self.game_state.change_trust("irina_lebedeva", 8)
                self.game_state.set_flag("bridge_artifact_confirmed", True)
            else:
                print("\n  — Спасибо, но пока всё под контролем.")
                print("  Хотя... если найдёте время, загляните в лабораторию.")
                self.game_state.change_relationship("irina_lebedeva", 2)

        # Взаимодействие с Риной
        print("\n  Рина повернулась:")
        
        rina_rel = self.game_state.crew_manager.get_character("rina_mirai").relationship
        if rina_rel >= 30:
            rina_options = ["Доложи обстановку", "Есть проблемы?", "Ты сегодня особенно хороша", "Хорошая работа"]
        else:
            rina_options = ["Доложи обстановку", "Есть проблемы?", "Хорошая работа"]
        
        rina_choice = get_choice("Что сказать Рине?", rina_options)

        if rina_choice == 0:
            print("\n  — Патруль флота на орбите. Пропуск получен.")
            print("  — Можем стыковаться в любое время.")
            self.game_state.change_trust("rina_mirai", 3)
        elif rina_choice == 1:
            print("\n  — Пока нет. Но я слежу за аномалиями в секторе.")
            print("  — Лучше перестраховаться.")
            self.game_state.change_relationship("rina_mirai", 3)
        elif rina_choice == 2 and rina_rel >= 30:
            print("\n  Рина подняла бровь, улыбаясь:")
            print("  — Капитан, вы отвлекаете меня от работы комплиментами?")
            print("  — Но... спасибо. Мне приятно.")
            self.game_state.change_relationship("rina_mirai", 10)
            self.game_state.change_trust("rina_mirai", 3)
            self.game_state.set_flag("rina_flirted", True)
        else:
            idx = 2 if rina_rel >= 30 else 1
            print("\n  Рина улыбнулась:")
            print("  — Стараюсь, капитан.")
            self.game_state.change_relationship("rina_mirai", 5)
            self.game_state.change_trust("rina_mirai", 3)

        input("\n  [Нажмите Enter...]")
    
    def scene_pirate_contact(self):
        """Сцена: Контакт с пиратами"""
        clear_screen()
        print_alert("\n  [ТРЕВОГА!]")
        print_separator("-")
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

        # Проверяем психическую связь - даёт дополнительные опции
        psychic = self.game_state.get_flag("psychic_connection", False)
        
        if psychic:
            print("  [Психическая связь пульсирует...]")
            print("  Вы чувствуете... любопытство от артефакта?")
            print()

        self.dialogue_manager.start_dialogue("pirate_contact")
        self.run_dialogue()

        self.game_state.set_flag("pirate_contact_made", True)
        
        # Влияние на команду
        print("\n  [Реакция экипажа:]")
        rina_trust = self.game_state.crew_manager.get_character("rina_mirai").trust
        if rina_trust >= 50:
            print("  — Рина: «Капитан, я прикрою с любой стороны.»")
            self.game_state.change_trust("rina_mirai", 3)
        else:
            print("  — Рина выглядит напряжённой.")
        
        nadezhda_trust = self.game_state.crew_manager.get_character("nadezhda").trust
        if nadezhda_trust >= 50:
            print("  — Надежда: «Оружие готово к бою.»")
            self.game_state.change_trust("nadezhda", 3)
        else:
            print("  — Надежда проверяет системы безопасности.")

        input("\n  [Нажмите Enter...]")
    
    def scene_sabotage(self):
        """Сцена: Саботаж на корабле"""
        clear_screen()
        print_alert("\n  [СБОЙ СИСТЕМ]")
        print_art("sabotage")
        print_separator("-")
        print()

        text = """
  Свет на мостике мигнул. На секунду погас, затем вернулся — тусклее.
  Из динамиков донёсся голос Алии, напряжённый, без обычной уверенности:

  — Макс, у нас проблема. Система охлаждения вышла из строя.
    Это не случайность, капитан. Кто-то намеренно вывел её из строя.

  На экране появились данные: температура в техническом отсеке
  росла. Быстрее, чем должна была.

  Рина обернулась:
  — До станции 4 часа. Если температура продолжит расти...
        """
        print(text)
        print()

        # Проверяем доверие к Алии
        alia_trust = self.game_state.crew_manager.get_character("alia_naar").trust
        
        print("  [Ваша реакция:]")
        if alia_trust >= 60:
            choice = get_choice(
                "Что делать?",
                ["Довериться Алие", "Отправить команду", "Лично проверить"]
            )
        else:
            choice = get_choice(
                "Что делать?",
                ["Довериться Алие", "Отправить команду", "Обвинить Алию"]
            )

        if choice == 0:
            print("\n  — Алия, действуй. Докладывай о любых изменениях.")
            print("  — Есть, капитан!")
            self.game_state.change_trust("alia_naar", 8)
            self.game_state.change_relationship("alia_naar", 5)
        elif choice == 1:
            print("\n  — Надежда, отправь команду в технический отсек.")
            print("  — Есть, капитан!")
            self.game_state.change_trust("nadezhda", 5)
            self.game_state.change_trust("alia_naar", -3)
        else:
            if alia_trust >= 60:
                print("\n  — Я проверю лично. Алия, придержи системы.")
                print("  — Поняла, капитан.")
                self.game_state.change_relationship("alia_naar", 5)
                self.game_state.set_flag("personally_checked_sabotage", True)
            else:
                print("\n  — Алия, объяснись. Почему система отказала?")
                print("  — Капитан, я не причём! Клянусь!")
                self.game_state.change_trust("alia_naar", -15)
                self.game_state.change_relationship("alia_naar", -10)
                self.game_state.set_flag("alia_accused", True)

        input("\n  [Нажмите Enter...]")
        
        self.game_state.set_flag("sabotage_discovered", True)

    def scene_discovery(self):
        """Сцена: Находка в техническом отсеке"""
        clear_screen()
        print("\n  [ТЕХНИЧЕСКИЙ ОТСЕК]")
        print_separator("-")
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

        # Проверяем отношения с Алией
        alia_rel = self.game_state.crew_manager.get_character("alia_naar").relationship
        alia_trust = self.game_state.crew_manager.get_character("alia_naar").trust

        choice = get_choice(
            "Ваши действия?",
            ["Взять чип", "Осмотреть панель", "Поговорить с Алией"]
        )

        if choice == 0:
            print("\n  Чип был повреждён, но на нём виден логотип:")
            print("  «НейроТех Индастриз» — производитель систем безопасности.")
            self.game_state.set_flag("found_chip", True)
            # Добавляем предмет и обновляем квест
            self.gameplay.on_item_collected("alien_data_chip", 1)
            self.gameplay.update_quest_objective("side_001", "obj_evidence", 1)
        elif choice == 1:
            print("\n  На панели — следы вскрытия. Профессиональная работа.")
            self.game_state.set_flag("examined_panel", True)
            self.gameplay.update_quest_objective("side_001", "obj_evidence", 1)
        else:
            # Разговор с Алией
            if alia_trust < 30 and alia_rel < 30:
                print("\n  — Я такого раньше не видела, — Алия нахмурилась.")
                print("  — Но кто-то знал, где искать.")
                self.game_state.change_relationship("alia_naar", 2)
            elif alia_rel >= 50:
                print("\n  Алия вздохнула, вытирая пот со лба:")
                print("  — Знаешь, капитан... в такие моменты я рада, что ты рядом.")
                print("  — Мы справимся. Вместе.")
                self.game_state.change_relationship("alia_naar", 8)
                self.game_state.change_trust("alia_naar", 5)
                self.game_state.set_flag("alia_moment", True)
            else:
                print("\n  — Я такого раньше не видела, — Алия нахмурилась.")
                print("  — Но кто-то знал, где искать.")
                self.dialogue_manager.start_dialogue("alia_confrontation")
                self.run_dialogue()
                self.game_state.change_relationship("alia_naar", 2)

        self.game_state.set_flag("discovery_complete", True)
        input("\n  [Нажмите Enter...]")

    def scene_combat(self):
        """Сцена: Бой с пиратами-диверсантами"""
        clear_screen()
        print_alert("\n  [БОЕВАЯ ТРЕВОГА!]")
        print_art("sabotage")
        print_separator("-")
        print()

        text = """
  При выходе из технического отсека вы столкнулись с группой вооружённых
  людей в масках. Это были не просто диверсанты — это наёмники.

  — Сдавайтесь, капитан! — крикнул лидер, поднимая оружие.
        """
        print(text)
        print()

        # Начинаем бой
        self.gameplay.start_combat("Наёмник")

        print("  [ВАШИ ДЕЙСТВИЯ]")
        print("  " + "-" * 40)

        # Проверяем доступные способности
        has_potion = self.gameplay.has_item("healing_potion")
        has_stim = self.gameplay.has_item("biotic_stim")

        options = ["Атаковать", "Использовать предмет"]
        if has_potion:
            options.append("Лечебный эликсир")
        if has_stim:
            options.append("Биотический стимулятор")

        choice = get_choice("Выберите действие:", options)

        if choice == 0:
            # Атака
            print("\n  Вы выхватываете плазменный пистолет и стреляете.")
            print("  Наёмник падает, сражённый точным выстрелом.")
            self.gameplay.on_enemy_defeated("mercenary")
            self.game_state.change_trust("nadezhda", 5)

        elif choice == 1:
            # Предмет
            item_options = []
            if has_potion:
                item_options.append("Лечебный эликсир")
            if has_stim:
                item_options.append("Биотический стимулятор")

            if item_options:
                item_choice = get_choice("Какой предмет использовать?", item_options)
                if item_choice == 0 and has_potion:
                    result = self.gameplay.use_item("healing_potion")
                    if result["success"]:
                        print(f"\n  {result['item_name']}: {result['effects'][0]}")
                elif item_choice == 1 and has_stim:
                    result = self.gameplay.use_item("biotic_stim")
                    if result["success"]:
                        print(f"\n  {result['item_name']}: временный бонус к биотике")

        elif choice >= 2:
            # Использование предмета напрямую
            if has_potion and choice == 2:
                result = self.gameplay.use_item("healing_potion")
                if result["success"]:
                    print(f"\n  {result['item_name']}: {result['effects'][0]}")
            elif has_stim and choice == 3:
                result = self.gameplay.use_item("biotic_stim")
                if result["success"]:
                    print(f"\n  {result['item_name']}: временный бонус к биотике")

        # Завершаем бой
        self.gameplay.end_combat(victory=True)

        print("\n  [После боя]")
        print("  — Надежда: «Отличная работа, капитан!»")
        print("  — Рина: «Я заблокировала их каналы связи.»")

        self.game_state.set_flag("combat_won", True)
        input("\n  [Нажмите Enter...]")

    def scene_artifact_examination(self):
        """Сцена: examination артефакта после саботажа"""
        clear_screen()
        print("\n  [ГРУЗОВОЙ ОТСЕК]")
        print_separator("-")
        print()

        text = """
  После обнаружения саботажа Макс решил лично проверить артефакт.
  Грузовой отсек был почти пуст, кроме защитной камеры в центре.

  Артефакт... пульсировал. Ритмично, как сердце.
        """
        print(text)
        print()

        irina_rel = self.game_state.crew_manager.get_character("irina_lebedeva").relationship

        if irina_rel >= 60:
            options = ["Осмотреть ближе", "Сканировать", "Позвать Ирину", "Пригласить Ирину"]
        else:
            options = ["Осмотреть ближе", "Сканировать", "Позвать Ирину"]

        choice = get_choice("Ваши действия?", options)

        if choice == 0:
            print("\n  Макс приблизился к камере.")
            print("  На мгновение ему показалось, что артефакт...")
            print("  ...посмотрел на него.")
            print("\n  [Психическая связь установлена]")
            self.game_state.set_flag("psychic_connection", True)
            self.game_state.change_trust("athena", -5)
        elif choice == 1:
            print("\n  Сканирование показало аномалию:")
            print("  > Энергия: 847 ТэВ (норма: 150)")
            print("  > Температура: -3°C (внутри камеры)")
            print("  > Психический фон: обнаружен")
            self.game_state.set_flag("artifact_scanned", True)
            self.game_state.change_relationship("irina_lebedeva", 3)
        elif choice == 2 and irina_rel >= 60:
            print("\n  Ирина пришла быстро, в лабораторном халате.")
            print("  — Вы звали, капитан?")
            print()
            subchoice = get_choice(
                "Что сказать?",
                ["Посмотреть вместе", "Ты нужна мне... для исследований", "Просто хотел видеть тебя"]
            )
            if subchoice == 0:
                print("\n  — Конечно. Давайте изучим это вместе.")
                print("  Ирина встала рядом, плечом к плечу.")
                self.game_state.change_trust("irina_lebedeva", 10)
                self.game_state.set_flag("irina_artifact_confirmed", True)
            elif subchoice == 1:
                print("\n  Ирина улыбнулась:")
                print("  — Для исследований? Ну что ж... я к вашим услугам.")
                self.game_state.change_relationship("irina_lebedeva", 12)
                self.game_state.change_trust("irina_lebedeva", 5)
                self.game_state.set_flag("irina_flirted_research", True)
            else:
                print("\n  Ирина слегка покраснела:")
                print("  — Ох, капитан... вы заставили меня прийти.")
                print("  — Но... мне приятно.")
                self.game_state.change_relationship("irina_lebedeva", 15)
                self.game_state.change_trust("irina_lebedeva", 8)
                self.game_state.set_flag("irina_personal_moment", True)
        else:
            idx = 2 if irina_rel >= 60 else 1
            print("\n  Ирина прибыла через несколько минут.")
            print("  — Я тоже это чувствую, капитан.")
            print("  — Он... живой. Или был когда-то.")
            self.game_state.change_trust("irina_lebedeva", 10)
            self.game_state.set_flag("irina_artifact_confirmed", True)

        input("\n  [Нажмите Enter...]")
    
    def run_dialogue(self):
        """Запустить текущий диалог"""
        if not self.dialogue_manager.current_dialogue:
            return

        crew_trust = {}
        crew_relationship = {}
        if self.game_state.save_data:
            crew_trust = self.game_state.save_data.trust_values
            crew_relationship = self.game_state.save_data.relationships

        while not self.dialogue_manager.is_finished():
            try:
                text = self.dialogue_manager.get_current_text()
                if text:
                    if ":" in text:
                        speaker, dialogue = text.split(":", 1)
                        speaker = speaker.strip()
                        char_id = self._find_char_id_by_name(speaker)
                        if char_id:
                            color = get_character_color(char_id)
                            print(f"\n{colorize(speaker + ':', color)}{dialogue}\n")
                        else:
                            print(f"\n{text}\n")
                    else:
                        print(f"\n{text}\n")

                choices = self.dialogue_manager.get_available_choices(
                    self.game_state.save_data.stats if self.game_state.save_data else {},
                    self.game_state.save_data.inventory if self.game_state.save_data else [],
                    crew_trust,
                    crew_relationship
                )

                if not choices:
                    break

                idx = get_choice("Ваш выбор:", [c.text for c in choices])
                selected_choice = choices[idx]
                self.dialogue_manager.make_choice(selected_choice.id)

                if selected_choice.effect_value and isinstance(selected_choice.effect_value, tuple):
                    char_id, amount = selected_choice.effect_value
                    effect_name = selected_choice.effect.name

                    if effect_name.startswith("RELATIONSHIP"):
                        self.game_state.change_relationship(char_id, amount)
                    elif effect_name.startswith("TRUST"):
                        self.game_state.change_trust(char_id, amount)

            except (IndexError, KeyError, TypeError) as e:
                logger.debug(f"Ошибка диалога: {e}")
                break
    
    def _find_char_id_by_name(self, name: str) -> str:
        """Найти ID персонажа по имени"""
        name_map = {
            "Афина": "athena",
            "Алия": "alia_naar",
            "Ирина": "irina_lebedeva",
            "Рина": "rina_mirai",
            "Надежда": "nadezhda",
            "Екатерина": "ekaterina",
            "Макс": "max_well",
            "Селена Ро": "selena_ro",
        }
        return name_map.get(name)

    def show_status(self):
        """Показать статус игрока"""
        clear_screen()
        print_header("СТАТУС ИГРОКА", TEXT_WIDTH + 4)

        self.gameplay.print_status(print)

        print("\n  [КОМАНДА]")
        print("  " + "-" * 40)
        crew = self.game_state.crew_manager.get_all_crew()
        for char in crew[:5]:  # Показываем до 5 персонажей
            rel_status = char.get_relationship_status()
            print(f"  {char.name}: {rel_status}")

        print("\n  Нажмите Enter для возврата...")
        input()

    def chapter_end(self):
        """Конец главы"""
        clear_screen()
        print_header("ГЛАВА 1 ЗАВЕРШЕНА", TEXT_WIDTH + 4)

        print("\n  Вы успешно завершили первую главу!")
        print("\n  ═══════════════════════════════════════")
        print("  СТАТИСТИКА")
        print("  ═══════════════════════════════════════")

        # Показываем найденные улики
        clues_found = sum([
            self.game_state.get_flag("found_chip", False),
            self.game_state.get_flag("examined_panel", False),
        ])
        print(f"\n  [Улики] Найдено улик: {clues_found}/2")

        # Исследование артефакта
        artifact_knowledge = sum([
            self.game_state.get_flag("lab_artifact_discussed", False),
            self.game_state.get_flag("artifact_scanned", False),
            self.game_state.get_flag("irina_artifact_confirmed", False),
        ])
        print(f"  [Артефакт] Изучение: {artifact_knowledge}/3")

        # Психическая связь
        if self.game_state.get_flag("psychic_connection", False):
            print("  [Связь] ⚠ Психическая связь с артефактом")

        # Реакция на саботаж
        print("\n  [Саботаж]:")
        if self.game_state.get_flag("alia_accused", False):
            print("    ⚠ Алия обвинена — доверие потеряно")
        elif self.game_state.get_flag("personally_checked_sabotage", False):
            print("    ✓ Личная проверка саботажа")
        else:
            print("    ✓ Расследование продолжается")

        # Романтические моменты
        flirt_count = sum([
            self.game_state.get_flag("irina_flirted", False),
            self.game_state.get_flag("rina_flirted", False),
            self.game_state.get_flag("alia_moment", False),
            self.game_state.get_flag("irina_flirted_research", False),
            self.game_state.get_flag("irina_personal_moment", False),
        ])
        if flirt_count > 0:
            print(f"\n  [Отношения] Романтических моментов: {flirt_count}")
            if self.game_state.get_flag("irina_flirted", False):
                print("    • Флирт с Ириной в лаборатории")
            if self.game_state.get_flag("rina_flirted", False):
                print("    • Флирт с Риной на мостике")
            if self.game_state.get_flag("alia_moment", False):
                print("    • Особый момент с Алией")
            if self.game_state.get_flag("irina_flirted_research", False):
                print("    • \"Исследования\" с Ириной")
            if self.game_state.get_flag("irina_personal_moment", False):
                print("    • Личный момент с Ириной")

        # Отношения и доверие
        print("\n  ═══════════════════════════════════════")
        print("  ЭКИПАЖ")
        print("  ═══════════════════════════════════════")
        for char in self.game_state.crew_manager.get_all_crew():
            if char.role.value != "Капитан":
                rel = char.relationship
                trust = char.trust
                bar_len = rel // 5
                bar = "█" * bar_len + "░" * (20 - bar_len)
                print(f"\n  {char.name}:")
                print(f"    Отношения: [{bar}] {rel}%")
                print(f"    Доверие: {char.get_trust_level()}")

        # Последствия выборов
        print("\n  ═══════════════════════════════════════")
        print("  ПОСЛЕДСТВИЯ")
        print("  ═══════════════════════════════════════")
        if self.game_state.get_flag("pirate_contact_made", False):
            print("  • Пираты знают о вас. Селена Ро запомнила встречу.")
        if self.game_state.get_flag("discovery_complete", False):
            print("  • Саботаж расследуется. Команда ждёт ваших приказов.")
        if self.game_state.get_flag("psychic_connection", False):
            print("  • Вы чувствуете... что-то в глубине сознания.")
        if self.game_state.get_flag("bridge_artifact_confirmed", False):
            print("  • Ирина доверяет вам в вопросе артефакта.")
        
        # Проверка на потенциальных предателей
        traitors = self.game_state.crew_manager.get_potential_traitors()
        if traitors:
            print("\n  ═══════════════════════════════════════")
            print("  ⚠  ПРЕДУПРЕЖДЕНИЕ")
            print("  ═══════════════════════════════════════")
            for traitor in traitors:
                print(f"  • {traitor.name} может предать вас...")

        # Бонусы за исследования
        print("\n  ═══════════════════════════════════════")
        print("  БОНУСЫ")
        print("  ═══════════════════════════════════════")
        if artifact_knowledge >= 3:
            print("  🎯 Глубокое понимание артефакта")
            print("     +10 к психике в следующей главе")
        
        # Проверка на идеальное прохождение
        if clues_found == 2 and artifact_knowledge >= 2 and not traitors:
            print("  🏆 Идеальное прохождение главы 1!")
            print("     Все улики найдены, экипаж loyal")
        
        if clues_found == 0:
            print("  ⚠ Улики не найдены — расследование затруднено")
        
        if flirt_count >= 3:
            print("  💕 Романтик главы 1")
            print("     Экипаж особенно предан вам")

        print()
        self.game_state.save_game("autosave.json")
        print("  Игра автоматически сохранена.")
        print("\n  ═══════════════════════════════════════")
        print("  ГЛАВА 2: СЛЕД В ПУСТОТЕ")
        print("  Доступно сейчас...")
        print("  ═══════════════════════════════════════")
        input("\n  Нажмите Enter для продолжения...")
        
        self.play_chapter_2()

    def play_chapter_2(self):
        """Глава 2: След в пустоте"""
        clear_screen()
        print_header("ГЛАВА 2: СЛЕД В ПУСТОТЕ", TEXT_WIDTH + 4)
        print("\n  «Элея» в глубоком космосе. 2187 год.")
        input("\n  [Нажмите Enter для начала...]")

        self.scene_ch2_morning()
        if not self.running:
            return

        self.scene_ch2_lab()
        if not self.running:
            return

        self.scene_ch2_rec_room()
        if not self.running:
            return

        self.scene_ch2_security()
        if not self.running:
            return

        self.scene_ch2_bridge()
        if not self.running:
            return

        self.chapter_2_end()

    def scene_ch2_morning(self):
        """Сцена: Утро и выбор романтической линии"""
        clear_screen()
        print("\n  [Глава 2: След в пустоте]")
        print_separator("-")
        print("\n  [Личное время]")
        print()

        text = """
  После событий на станции «Элея» вышла на орбиту глубокого космоса.
  У экипажа появилось немного времени на отдых. Макс стоит перед выбором —
  как провести свободный час?
        """
        print(text)
        print()

        choice = get_choice(
            "Кого навестить?",
            ["Алия (рубка)", "Ирина (лаборатория)", "Рина (комната отдыха)", 
             "Надежда (охрана)", "Афина (частный канал)"]
        )

        if choice == 0:
            self.dialogue_manager.start_dialogue("alia_evening")
            self.run_dialogue()
        elif choice == 1:
            self.dialogue_manager.start_dialogue("irina_lab")
            self.run_dialogue()
        elif choice == 2:
            self.dialogue_manager.start_dialogue("rina_rec_room")
            self.run_dialogue()
        elif choice == 3:
            self.dialogue_manager.start_dialogue("nadezhda_security")
            self.run_dialogue()
        else:
            self.dialogue_manager.start_dialogue("athena_private")
            self.run_dialogue()

        self.game_state.set_flag("ch2_romance_started", True)
        input("\n  [Нажмите Enter...]")

    def scene_ch2_lab(self):
        """Сцена: Лаборатория - исследование артефакта"""
        clear_screen()
        print("\n  [ЛАБОРАТОРИЯ]")
        print_separator("-")
        print()

        text = """
  Ирина работает с артефактом. Голографические дисплеи показывают
  сложные энергетические паттерны.

  — Капитан, у меня есть данные. Артефакт... он реагирует на что-то.
    На внешние сигналы.
        """
        print(text)
        print()

        choice = get_choice(
            "Что спросить?",
            ["Какие сигналы?", "Это опасно?", "Нужна помощь?"]
        )

        if choice == 0:
            print("\n  — Не знаю. Но они исходят из глубины космоса.")
            self.game_state.set_flag("ch2_signal_discovered", True)
        elif choice == 1:
            print("\n  — Пока не могу сказать. Но я продолжаю мониторинг.")
            self.game_state.change_relationship("irina_lebedeva", 3)
        else:
            print("\n  — Спасибо, капитан. Но пока всё под контролем.")
            self.game_state.change_relationship("irina_lebedeva", 5)

        input("\n  [Нажмите Enter...]")

    def scene_ch2_rec_room(self):
        """Сцена: Комната отдыха - разговор с командой"""
        clear_screen()
        print("\n  [КОМНАТА ОТДЫХА]")
        print_separator("-")
        print()

        text = """
  Рина и Алия обсуждают тактику у симулятора. Они замолкают,
  когда входит Макс.

  — Капитан, как раз вовремя. У нас есть идея по улучшению маршрута.
        """
        print(text)
        print()

        choice = get_choice(
            "Ответить",
            ["Слушаю", "Позже", "Присоединиться к разговору"]
        )

        if choice == 0:
            print("\n  Рина показывает новый маршрут на голограмме.")
            self.game_state.change_relationship("rina_mirai", 3)
        elif choice == 1:
            print("\n  — Поняли, капитан. Будем ждать.")
        else:
            print("\n  Начинается оживлённая дискуссия о тактике.")
            self.game_state.change_relationship("alia_naar", 3)
            self.game_state.change_relationship("rina_mirai", 3)

        input("\n  [Нажмите Enter...]")

    def scene_ch2_security(self):
        """Сцена: Оружейная - доклад по безопасности"""
        clear_screen()
        print("\n  [ОРУЖЕЙНАЯ]")
        print_separator("-")
        print()

        text = """
  Надежда проверяет оружие. Она кивает Максу.

  — После саботажа я усилила протоколы. Доступ к критическим
    системам только по биометрии.
        """
        print(text)
        print()

        choice = get_choice(
            "Ответить",
            ["Отлично работаешь", "Есть новости?", "Нужна помощь?"]
        )

        if choice == 0:
            print("\n  — Спасибо, капитан. Это моя работа.")
            self.game_state.change_relationship("nadezhda", 5)
        elif choice == 1:
            print("\n  — Камеры в техническом отсеке заменены.")
            self.game_state.set_flag("ch2_cameras_replaced", True)
        else:
            print("\n  — Нет, но спасибо за предложение.")

        input("\n  [Нажмите Enter...]")

    def scene_ch2_bridge(self):
        """Сцена: Мостик - приближение к аномалии"""
        clear_screen()
        print_alert("\n  [ОБНАРУЖЕНА АНОМАЛИЯ]")
        print_separator("-")
        print()

        text = """
  Тревога звучит мягко. На главном экране — искажение пространства.

  Рина:
  — Гравитационная аномалия впереди. Никогда не видела такой.

  Алия:
  — Корабль цел, но лучше обойти.
        """
        print(text)
        print()

        choice = get_choice(
            "Решение",
            ["Обойти аномалию", "Исследовать", "Спросить Ирину"]
        )

        if choice == 0:
            print("\n  — Прокладываю обходной маршрут, — говорит Алия.")
            self.game_state.set_flag("ch2_avoid_anomaly", True)
        elif choice == 1:
            print("\n  — Рискнём. Алия, медленно вперёд.")
            self.game_state.set_flag("ch2_enter_anomaly", True)
        else:
            print("\n  Ирина изучает данные:")
            print("  — Это не природная аномалия. Кто-то её создал.")
            self.game_state.set_flag("ch2_anomaly_artificial", True)

        input("\n  [Нажмите Enter...]")

    def chapter_2_end(self):
        """Конец второй главы"""
        clear_screen()
        print_header("ГЛАВА 2 ЗАВЕРШЕНА", TEXT_WIDTH + 4)

        print("\n  Вы завершили вторую главу!")
        print("\n  Статистика:")

        # Отношения
        print("    • Отношения с экипажем:")
        for name, status in self.game_state.get_crew_relationships():
            print(f"      — {name}: {status}")

        # Найденные улики
        clues = sum([
            self.game_state.get_flag("ch2_signal_discovered", False),
            self.game_state.get_flag("ch2_cameras_replaced", False),
            self.game_state.get_flag("ch2_anomaly_artificial", False),
        ])
        print(f"\n    • Найдено улик: {clues}/3")

        # Романтическая линия
        print("\n  Романтическая линия:")
        top_char = self.game_state.get_top_relationship()
        if top_char:
            print(f"    • {top_char[0]}: {top_char[1]}")

        print()
        self.game_state.save_game("autosave_ch2.json")
        print("  Игра автоматически сохранена.")
        input("\n  Нажмите Enter для возврата в меню...")
    
    def save_game(self):
        """Сохранить игру"""
        try:
            if self.game_state.save_game():
                logger.info("Игра сохранена успешно")
                print("  Игра сохранена!")
            else:
                logger.warning("Ошибка при сохранении игры")
                print("  Ошибка сохранения!")
        except Exception as e:
            logger.error(f"Критическая ошибка сохранения: {e}")
            print("  Ошибка сохранения!")


def main():
    """Точка входа"""
    try:
        logger.info("Запуск игры Star Courier")
        game = Game()
        game.start()
    except KeyboardInterrupt:
        logger.info("Игра прервана пользователем")
        print("\n\n  Игра прервана. До встречи!")
    except Exception as e:
        logger.exception(f"Критическая ошибка: {e}")
        print(f"\n  Критическая ошибка: {e}")
        if confirm("Сохранить лог ошибки?"):
            with open("error.log", "w", encoding="utf-8") as f:
                import traceback
                traceback.print_exc(file=f)
            print("  Лог сохранён в error.log")


if __name__ == "__main__":
    main()
