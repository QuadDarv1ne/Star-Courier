# -*- coding: utf-8 -*-
"""
Star Courier - Сцены глав 1-2
Модуль содержит сцены для первой и второй глав
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .save_system import GameState
    from .dialogues import DialogueManager
    from .gameplay import GameplaySystem
    from .mental_state import MentalStateSystem

try:
    from .utils import clear_screen, print_separator, get_choice
    from .colors import print_alert
    from .ascii_art import print_art
except ImportError:
    from utils import clear_screen, print_separator, get_choice
    from colors import print_alert
    from ascii_art import print_art


class Chapter1Scenes:
    """Сцены первой главы"""

    def __init__(self, game_state: "GameState", dialogue_manager: "DialogueManager",
                 gameplay: "GameplaySystem", mental_state_system: "MentalStateSystem"):
        self.game_state = game_state
        self.dialogue_manager = dialogue_manager
        self.gameplay = gameplay
        self.mental_state_system = mental_state_system

    def scene_morning(self):
        """Сцена: Утро в каюте"""
        clear_screen()
        print("\n  [Глава 1: Нежданная встреча]")
        print_separator("-")
        print("\n  [Утро на «Элее»]")
        print()

        text = """
  Тихое гудение систем корабля разбудило Макса Велла раньше, чем должен
  был сработать будилник. Он открыл глаза и несколько секунд смотрел в
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
        self.run_dialogue_loop()

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

        psychic = self.game_state.get_flag("psychic_connection", False)

        if psychic:
            print("  [Психическая связь пульсирует...]")
            print("  Вы чувствуете... любопытство от артефакта?")
            print()

        self.dialogue_manager.start_dialogue("pirate_contact")
        self.run_dialogue_loop()

        self.game_state.set_flag("pirate_contact_made", True)

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

    def scene_discovery(self):
        """Сцена: Обнаружение диверсантов"""
        clear_screen()
        print("\n  [ТЕХНИЧЕСКИЙ ОТСЕК]")
        print_separator("-")
        print()

        text = """
  Технический отсек встретил Макса жаром и запахом озона.
  Система охлаждения дымилась — явно результат саботажа.

  В полумраке мелькнула тень. Не один. Их было несколько.
        """
        print(text)
        print()

        print("  [Ваша реакция:]")
        choice = get_choice(
            "Что делать?",
            ["Атаковать первым", "Спрятаться и наблюдать", "Позвать охрану"]
        )

        if choice == 0:
            print("\n  Вы выхватываете оружие и стреляете.")
            print("  Один из диверсантов падает.")
            self.game_state.change_trust("nadezhda", 5)
        elif choice == 1:
            print("\n  Вы затаились за оборудованием.")
            print("  Диверсанты обсуждают план...")
            self.game_state.set_flag("overheard_saboteurs", True)
        else:
            print("\n  — Надежда, мне нужна поддержка в техническом отсеке!")
            print("  — Уже выдвигаюсь, капитан!")
            self.game_state.change_trust("nadezhda", 8)

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

        has_potion = self.gameplay.has_item("healing_potion")
        has_stim = self.gameplay.has_item("biotic_stim")

        options = ["Атаковать", "Использовать предмет"]
        if has_potion:
            options.append("Лечебный эликсир")
        if has_stim:
            options.append("Биотический стимулятор")

        choice = get_choice("Выберите действие:", options)

        if choice == 0:
            print("\n  Вы выхватываете плазменный пистолет и стреляете.")
            print("  Наёмник падает, сражённый точным выстрелом.")
            self.gameplay.on_enemy_defeated("mercenary")
            self.game_state.change_trust("nadezhda", 5)

        elif choice == 1:
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

        # Интеграция mental_state: последствия боя
        self.mental_state_system.on_combat_end(victory=True, casualties=0)

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

            # Интеграция mental_state: контакт с Сущностью
            self.mental_state_system.on_entity_encounter(intensity=15)

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

    def run_dialogue_loop(self):
        """Запустить цикл диалога"""
        while self.dialogue_manager.current_dialogue:
            node = self.dialogue_manager.get_current_node()
            if not node:
                break

            print(f"\n  {node.speaker}: {node.text}")

            if node.choices:
                choice_texts = [c.text for c in node.choices]
                choice_idx = get_choice("Выбор:", choice_texts)

                if 0 <= choice_idx < len(node.choices):
                    choice = node.choices[choice_idx]
                    self.dialogue_manager.make_choice(choice_idx)

                    if choice.effects:
                        for effect, value in choice.effects.items():
                            if effect == "relationship":
                                pass
                            elif effect == "trust":
                                pass
            else:
                input("  [Нажмите Enter...]")
                break

    def play_all(self):
        """Сыграть все сцены главы 1"""
        self.scene_morning()
        self.scene_lab()
        self.scene_bridge()
        self.scene_pirate_contact()
        self.scene_sabotage()
        self.scene_discovery()
        self.scene_combat()
        self.scene_artifact_examination()


class Chapter2Scenes:
    """Сцены второй главы"""

    def __init__(self, game_state: "GameState", dialogue_manager: "DialogueManager",
                 gameplay: "GameplaySystem", mental_state_system: "MentalStateSystem"):
        self.game_state = game_state
        self.dialogue_manager = dialogue_manager
        self.gameplay = gameplay
        self.mental_state_system = mental_state_system

    def scene_ch2_morning(self):
        """Сцена: Утро после станции"""
        clear_screen()
        print("\n  [Глава 2: После Орбиса]")
        print_separator("-")
        print("\n  [Утро на «Элее»]")
        print()

        text = """
  Макс проснулся от непривычной тишины. Станция осталась позади.
  Корабль шёл через гиперпространство, и это чувствовалось — лёгкая
  вибрация, странный привкус металла во рту.

  Панель у кровати показала:
  > До следующей остановки: 72 часа
  > Статус экипажа: в норме
  > Артефакт: стабилен
        """
        print(text)
        input("\n  [Нажмите Enter...]")

        self.game_state.set_flag("chapter2_started", True)

    def scene_ch2_lab(self):
        """Сцена: Лаборатория - исследование артефакта"""
        clear_screen()
        print("\n  [ЛАБОРАТОРИЯ]")
        print_separator("-")
        print()

        text = """
  Ирина работает с артефактом. Голографические дисплеи показывают
  сложные графики и уравнения.

  — Капитан, у меня есть данные. Артефакт... он реагирует на что-то.
    На сигнал из глубины космоса.
        """
        print(text)
        print()

        choice = get_choice(
            "Что спросить?",
            ["Какой сигнал?", "Это опасно?", "Можно отследить источник?"]
        )

        if choice == 0:
            print("\n  — Неизвестный тип. Не похож на искусственный.")
            print("  — Скорее... биологический.")
            self.game_state.change_trust("irina_lebedeva", 5)
        elif choice == 1:
            print("\n  — Пока не знаю. Но лучше быть готовыми.")
            self.game_state.set_flag("artifact_signal_known", True)
        else:
            print("\n  — Пытаюсь. Но сигнал очень слабый.")
            self.game_state.change_relationship("irina_lebedeva", 3)

        input("\n  [Нажмите Enter...]")

    def scene_ch2_rec_room(self):
        """Сцена: Комната отдыха"""
        clear_screen()
        print("\n  [КОМНАТА ОТДЫХА]")
        print_separator("-")
        print()

        text = """
  Экипаж собрался в комнате отдыха. Необычное явление — обычно
  все заняты своими делами. Но сегодня что-то витает в воздухе.

  Мия заметила вас первой:
  — Капитан! Присоединяйтесь. Мы как раз обсуждаем... будущее.
        """
        print(text)
        print()

        choice = get_choice(
            "Ответить?",
            ["Что за будущее?", "Не мешаю?", "С удовольствием"]
        )

        if choice == 0:
            print("\n  — После всего, что случилось...")
            print("  — Мы думаем о том, куда держим путь.")
            self.game_state.change_trust("mia", 5)
        elif choice == 1:
            print("\n  — Что вы! Наоборот, рада вас видеть.")
            self.game_state.change_relationship("mia", 3)
        else:
            print("\n  Мия улыбается:")
            print("  — Отлично. Нам нужно ваше мнение.")
            self.game_state.change_trust("mia", 8)

        input("\n  [Нажмите Enter...]")

    def scene_ch2_security(self):
        """Сцена: Пост безопасности"""
        clear_screen()
        print("\n  [ПОСТ БЕЗОПАСНОСТИ]")
        print_separator("-")
        print()

        text = """
  Надежда проверяет системы безопасности. На экранах — данные
  со всех датчиков корабля.

  — Капитан, у меня есть кое-что интересное, — говорит она,
    не отрываясь от мониторов.
        """
        print(text)
        print()

        choice = get_choice(
            "Что узнать?",
            ["Что нашла?", "Покажи", "Это связано с артефактом?"]
        )

        if choice == 0:
            print("\n  — После станции кто-то пытался получить доступ")
            print("    к системам корабля. Изнутри.")
            self.game_state.set_flag("internal_threat", True)
        elif choice == 1:
            print("\n  На экране — логи доступа.")
            print("  Один из них... зашифрован.")
            self.game_state.change_trust("nadezhda", 5)
        else:
            print("\n  — Возможно. Артефакт влияет на системы.")
            print("  — Или кто-то использует его как маяк.")
            self.game_state.change_trust("nadezhda", 8)

        input("\n  [Нажмите Enter...]")

    def scene_ch2_bridge(self):
        """Сцена: Мостик - курс"""
        clear_screen()
        print("\n  [МОСТИК]")
        print_separator("-")
        print()

        text = """
  Рина за навигационной консолью. На главном экране — звёздная
  карта с проложенным маршрутом.

  — Капитан, у нас два варианта пути, — говорит она, указывая
    на голограмму. — Быстрый, но опасный. Или долгий, но безопасный.
        """
        print(text)
        print()

        choice = get_choice(
            "Выбрать маршрут?",
            ["Быстрый путь", "Безопасный путь", "Покажи детали"]
        )

        if choice == 0:
            print("\n  — Поняла. Прокладываю курс через Пояс Штормов.")
            print("  — Время в пути: 48 часов.")
            self.game_state.set_flag("route_storm_belt", True)
        elif choice == 1:
            print("\n  — Разумно. Обходим аномалии.")
            print("  — Время в пути: 96 часов.")
            self.game_state.set_flag("route_safe", True)
        else:
            print("\n  — Быстрый: через Пояс Штормов. Риск: 40%.")
            print("  — Безопасный: вокруг аномалий. Риск: 5%.")
            self.game_state.change_trust("rina_mirai", 3)

        input("\n  [Нажмите Enter...]")

    def play_all(self):
        """Сыграть все сцены главы 2"""
        self.scene_ch2_morning()
        self.scene_ch2_lab()
        self.scene_ch2_rec_room()
        self.scene_ch2_security()
        self.scene_ch2_bridge()
