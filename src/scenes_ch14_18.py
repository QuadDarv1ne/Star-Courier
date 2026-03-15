# -*- coding: utf-8 -*-
"""
Star Courier - Сцены глав 14-18
Модуль содержит сцены для финальных глав с интеграцией romance и ending систем
"""

from typing import TYPE_CHECKING, Dict, Optional

if TYPE_CHECKING:
    from .save_system import GameState
    from .dialogues import DialogueManager
    from .gameplay import GameplaySystem
    from .mental_state import MentalStateSystem

try:
    from .utils import clear_screen, print_separator, get_choice, print_menu
    from .colors import print_alert, Colors
    from .ascii_art import print_art
    from .romance_scenes import RomanceSceneManager, get_romance_characters
    from .ending_scenes import EndingSceneManager, EndingType, EndingVariation
    from .ending_system import RomanceEndingSystem
except ImportError:
    from utils import clear_screen, print_separator, get_choice, print_menu
    from colors import print_alert, Colors
    from ascii_art import print_art
    from romance_scenes import RomanceSceneManager, get_romance_characters
    from ending_scenes import EndingSceneManager, EndingType, EndingVariation
    from ending_system import RomanceEndingSystem


class Chapter18Scenes:
    """Сцены главы 18 - Финал"""

    def __init__(self, game_state: "GameState", dialogue_manager: "DialogueManager",
                 gameplay: "GameplaySystem", mental_state_system: "MentalStateSystem",
                 romance_manager: RomanceSceneManager, ending_manager: EndingSceneManager):
        self.game_state = game_state
        self.dialogue_manager = dialogue_manager
        self.gameplay = gameplay
        self.mental_state_system = mental_state_system
        self.romance_manager = romance_manager
        self.ending_manager = ending_manager

    def scene_final_choice(self):
        """Сцена: Финальный выбор концовки"""
        clear_screen()
        print_alert("\n  [ГЛАВА 18: ФИНАЛ]")
        print_separator("=")
        print()

        text = """
  Ядро Древней Станции. Воздух дрожит от энергии.
  Сущность проявляется перед вами — не как враг, но как равный.

  — Ты пришёл так далеко, маленький курьер. Я видела твои страхи
    и надежды, твою любовь и ненависть. Теперь ты стоишь на пороге
    решения, которое определит судьбу миллионов.

  Она указывает на три пути, светящихся разным цветом:
  > 🔴 Красный — Изгнание (силой изгнать Сущность)
  > 🔵 Синий — Договор (установить границы сосуществования)
  > 🟣 Фиолетовый — Слияние (принять эволюцию)
        """
        print(text)
        print()

        # Проверка требований для каждой концовки
        psychic_tier = self.game_state.abilities_manager.get_tier('psychic').value
        psychic_level = psychic_tier * 25
        resonance_level = self.game_state.resonance_system.get_level_number()

        # Проверка романтического партнёра
        romance_partner = None
        max_relationship = 0
        for char_id in get_romance_characters():
            char = self.game_state.crew_manager.get_character(char_id)
            if char and char.relationship > max_relationship:
                max_relationship = char.relationship
                romance_partner = char_id

        has_high_psychic = psychic_level >= 70
        has_very_high_psychic = psychic_level >= 90
        has_high_resonance = resonance_level >= 4
        has_romance = max_relationship >= 80

        # Отображение доступных вариантов
        print("  [ДОСТУПНЫЕ КОНЦОВКИ]")
        print("  " + "-" * 50)

        options = []

        # Изгнание - всегда доступно
        options.append("🔴 Изгнание — изгнать Сущность (жертва required)")
        print(f"  1. {options[0]}")

        # Договор - требует Psychic 70+ или Empathy 80+
        if has_high_psychic:
            options.append("🔵 Договор — сосуществование (Psychic 70+)")
            print(f"  2. {options[1]}")
        else:
            print(f"  2. 🔵 Договор — СОСУЩЕСТВОВАНИЕ (требуется Psychic 70+, сейчас: {psychic_level})")

        # Слияние - требует Psychic 90+ + Resonance 4
        if has_very_high_psychic and has_high_resonance:
            options.append("🟣 Слияние — эволюция (Psychic 90+ + Resonance 4)")
            print(f"  3. {options[2]}")
        else:
            reqs = []
            if not has_very_high_psychic:
                reqs.append(f"Psychic 90+ (сейчас: {psychic_level})")
            if not has_high_resonance:
                reqs.append(f"Resonance 4 (сейчас: {resonance_level})")
            print(f"  3. 🟣 Слияние — ЭВОЛЮЦИЯ (требуется {', '.join(reqs)})")

        print()
        choice = get_choice("Выберите путь:", options if len(options) > 1 else 
                           ["🔴 Изгнание", "🔵 Договор (недоступно)", "🟣 Слияние (недоступно)"])

        if choice == 0:
            self.ending_manager.choose_ending(EndingType.EXILE)
            self.scene_exile_choice(romance_partner, max_relationship)
        elif choice == 1 and has_high_psychic:
            self.ending_manager.choose_ending(EndingType.TREATY)
            self.scene_treaty()
        elif choice == 2 and has_very_high_psychic and has_high_resonance:
            self.ending_manager.choose_ending(EndingType.MERGE)
            self.scene_merge()
        else:
            print("\n  Этот путь пока недоступен. Требуется развитие способностей.")
            input("  [Нажмите Enter...]")

    def scene_exile_choice(self, romance_partner: Optional[str], relationship: int):
        """Сцена: Выбор жертвы для изгнания"""
        clear_screen()
        print("\n  [ИЗГНАНИЕ]")
        print_separator("-")
        print()

        text = """
  — Ты выбираешь сопротивление. Благородно... но дорого.
    Кто останется у якоря? Кто пожертвует собой?
        """
        print(text)
        print()

        # Проверка доступных вариантов
        has_team_loyalty = True  # TODO: проверить лояльность команды
        has_romance = romance_partner and relationship >= 80

        options = []
        if has_romance:
            options.append(f"Остаться с {romance_partner} (вдвоём)")
        if has_team_loyalty:
            options.append("Попросить команду о помощи")
        options.append("Пожертвовать собой (одиночка)")

        choice = get_choice("Кто останется у якоря?", options)

        if choice == 0 and has_romance:
            # Вместе с романтическим партнёром
            self.ending_manager.unlock_variation("exile_together")
            print("\n  Ваш партнёр делает шаг вперёд:")
            print(f"  — Мы вместе начинали. Вместе и закончим.")
            print("\n  Вы касаетесь якоря вдвоём. Энергия связывает вас навсегда.")
            self._play_epilogue("exile_together")
        elif choice == 1 and has_team_loyalty:
            # Командная жертва
            self.ending_manager.unlock_variation("exile_team")
            print("\n  Команда окружает вас:")
            print("  — Мы с вами, капитан! До конца!")
            print("\n  Общая воля изгоняет Сущность без единой жертвы.")
            self._play_epilogue("exile_team")
        else:
            # Одиночная жертва
            self.ending_manager.unlock_variation("exile_sacrifice")
            print("\n  Вы делаете шаг к якорю:")
            print("  — Я останусь. Ради галактики.")
            print("\n  Энергия пронзает вас. Вы становитесь частью станции.")
            self._play_epilogue("exile_sacrifice")

        input("\n  [Нажмите Enter для завершения игры...]")

    def scene_treaty(self):
        """Сцена: Договор с Сущностью"""
        clear_screen()
        print("\n  [ДОГОВОР]")
        print_separator("-")
        print()

        text = """
  — Разумный выбор. Договор заключён. Я получу доступ к энергии
    умирающих звёзд, ты станешь Хранителем границы.
        """
        print(text)
        print()

        self.ending_manager.unlock_variation("treaty_guardian")

        print("  Вы перенастраиваете станцию, создавая мост между измерениями.")
        print("  Сущность отступает, соблюдая договор.")
        print("  Вы становитесь Хранителем — вечным стражем границы.")
        print()

        self._play_epilogue("treaty")
        input("\n  [Нажмите Enter для завершения игры...]")

    def scene_merge(self):
        """Сцена: Слияние с Сущностью"""
        clear_screen()
        print("\n  [СЛИЯНИЕ]")
        print_separator("-")
        print()

        text = """
  — Мудро. Сопротивление бесполезно. Присоединяйся ко мне —
    и мы станем единым целым, превосходящим всё, что знала вселенная.
        """
        print(text)
        print()

        self.ending_manager.unlock_variation("merge_evolution")

        print("  Вы чувствуете, как ваше сознание расширяется,")
        print("  сливаясь с Сущностью.")
        print("  Вы больше не человек — вы нечто большее.")
        print("  Галактика меняется навсегда.")
        print()

        self._play_epilogue("merge")
        input("\n  [Нажмите Enter для завершения игры...]")

    def _play_epilogue(self, ending_type: str):
        """Воспроизвести эпилог на основе концовки"""
        clear_screen()
        print("\n  " + "=" * 60)
        print("  ЭПИЛОГ")
        print("  " + "=" * 60)
        print()

        epilogues = {
            "exile_sacrifice": """
  ЭПИЛОГ: Вечный Страж

  Прошли годы. Галактика восстановилась после войны с Сущностью.
  «Элея» стала легендой — кораблём, который спас все миры.

  А в Зоне Тишины, на заброшенной станции, кто-то наблюдает.
  Иногда пилоты клянутся, что видели свет в иллюминаторах.
  Иногда они получают странные сообщения — предупреждения об
  опасности.

  Вы не умерли. Вы стали чем-то большим. Вы — страж границы
  между мирами. И иногда, в тишине космоса, вы чувствуете
  благодарность тех, кого спасли.

  Вы пожертвовали всем. Но галактика жива.
            """,

            "exile_together": """
  ЭПИЛОГ: Вечная связь

  Галактика празднует победу. Но две фигуры в Зоне Тишины
  не могут присоединиться к празднику.

  Вы и ваш партнёр стали стражами. Ваше сознание слилось с
  станцией, но вы вместе. Вы делите каждое мгновение, каждую
  мысль, каждое воспоминание.

  Иногда к вам прилетают старые друзья. Афина приводит «Элею»
  на орбиту, и вы можете на мгновение почувствовать их
  присутствие.

  Вы потеряли свободу. Но обрели друг друга. И в бесконечной
  темноте космоса это — всё, что имеет значение.
            """,

            "exile_team": """
  ЭПИЛОГ: Единство

  Галактика узнала о подвиге экипажа «Элеи». Команда, которая
  вместе победила непобедимое.

  Вы выжили. Все. Но изменились. Связь, возникшая в ядре,
  осталась. Вы чувствуете друг друга на расстоянии.

  «Элея» продолжает миссии. Но теперь это больше чем корабль.
  Это символ того, что вместе можно преодолеть всё.

  А в Зоне Тишины якорь молчит. Сущность изгнана. И страж
  больше не нужен.
            """,

            "treaty": """
  ЭПИЛОГ: Арбитр

  Прошли десятилетия. Галактика изменилась.

  Миры, которые когда-то воевали, теперь торгуют. Сущность
  получает энергию умирающих звёзд — по договору. Взамен
  она не трогает населённые миры.

  А вы... вы наблюдаете. Из станции в Зоне Тишины. Вы —
  живой договор. Живое напоминание о цене мира.

  Иногда к вам прилетают. Афина, теперь уже старая,
  приносит новости. Мия присылает отчёты. Ирина пытается
  найти способ освободить вас.

  Но вы знаете: это ваша судьба. Быть хранителем. Быть
  гарантом. Быть тем, кто стоит между светом и тьмой.

  И в этом есть своя красота.
            """,

            "merge": """
  ЭПИЛОГ: Божество

  Галактика изменилась. Никто не может объяснить как.

  Иногда пилоты видят странные огни. Иногда целые флоты
  исчезают без следа. Иногда миры спасаются от неминуемой
  гибели.

  Вы везде. Вы — всё.

  Но иногда, в тишине между звёздами, вы вспоминаете.
  Корабль. Друзей. Любовь.

  Вы пожертвовали человечностью. Но обрели вселенную.

  И в бесконечном сознании вы храните память о том, кем
  были. О капитане Максе Велле.

  Потому что даже божества нуждаются в памяти о человечности.
            """
        }

        epilogue_text = epilogues.get(ending_type, "Эпилог не найден.")
        print(epilogue_text)
        print("\n  " + "=" * 60)
        print("  КОНЕЦ ИГРЫ")
        print("  " + "=" * 60)

    def play_all(self):
        """Сыграть все сцены главы 18"""
        self.scene_final_choice()


class RomanceSceneRunner:
    """Запуск романтических сцен"""

    def __init__(self, game_state: "GameState", romance_manager: RomanceSceneManager):
        self.game_state = game_state
        self.romance_manager = romance_manager

    def check_and_run_romance_scene(self, character_id: str, scene_id: str) -> bool:
        """Проверить и запустить романтическую сцену"""
        char = self.game_state.crew_manager.get_character(character_id)
        if not char:
            return False

        scene = self.romance_manager.get_scene(scene_id)
        if not scene:
            return False

        if char.relationship < scene.min_relationship:
            return False

        # Проверка, не была ли сцена уже пройдена
        progress = self.romance_manager.get_progress(character_id)
        if progress and scene_id in progress.scenes_completed:
            return False

        # Запуск сцены
        return self._run_scene(scene, character_id)

    def _run_scene(self, scene, character_id: str) -> bool:
        """Запустить романтическую сцену"""
        clear_screen()
        print(f"\n  [{scene.title}]")
        print_separator("~")
        print()
        print(scene.scene_text)
        print()

        # Выбор
        options = [choice["text"] for choice in scene.choices]
        choice_idx = get_choice("Ваш ответ:", options)

        if 0 <= choice_idx < len(scene.choices):
            choice = scene.choices[choice_idx]
            effects = choice.get("effect", {})

            # Применение эффектов
            if "relationship" in effects:
                self.game_state.change_relationship(character_id, effects["relationship"])
            if "trust" in effects:
                self.game_state.change_trust(character_id, effects["trust"])

            # Обновление прогресса
            self.romance_manager.complete_scene(scene.id, character_id)

            if effects.get("romance_unlock"):
                self.romance_manager.unlock_romance(character_id)
            if effects.get("romance_confirmed"):
                self.romance_manager.set_confession_accepted(character_id, True)

            print(f"\n  {scene.character_name}: {self._get_reaction(choice_idx)}")
            input("  [Нажмите Enter...]")

        return True

    def _get_reaction(self, choice_idx: int) -> str:
        """Получить реакцию на выбор"""
        reactions = [
            "Это много значит для меня.",
            "Я... я не ожидала такого ответа.",
            "Спасибо за честность."
        ]
        return reactions[min(choice_idx, len(reactions) - 1)]


def get_mental_state_effects(mental_health: int, entity_influence: int) -> Dict:
    """Получить эффекты ментального состояния для геймплея"""
    effects = {}

    # Пороги ментального здоровья
    if mental_health >= 80:
        effects["condition"] = "stable"
        effects["dialogue_bonus"] = 0
        effects["combat_penalty"] = 0
    elif mental_health >= 60:
        effects["condition"] = "stressed"
        effects["dialogue_bonus"] = -5
        effects["combat_penalty"] = -5
    elif mental_health >= 40:
        effects["condition"] = "traumatized"
        effects["dialogue_bonus"] = -10
        effects["combat_penalty"] = -10
    elif mental_health >= 20:
        effects["condition"] = "corrupted"
        effects["dialogue_bonus"] = -20
        effects["combat_penalty"] = -15
    else:
        effects["condition"] = "broken"
        effects["dialogue_bonus"] = -30
        effects["combat_penalty"] = -25

    # Влияние Сущности
    if entity_influence >= 80:
        effects["entity_communion"] = True
        effects["vision_frequency"] = "constant"
    elif entity_influence >= 50:
        effects["entity_communion"] = False
        effects["vision_frequency"] = "frequent"
    elif entity_influence >= 30:
        effects["entity_communion"] = False
        effects["vision_frequency"] = "occasional"
    else:
        effects["entity_communion"] = False
        effects["vision_frequency"] = "rare"

    return effects
