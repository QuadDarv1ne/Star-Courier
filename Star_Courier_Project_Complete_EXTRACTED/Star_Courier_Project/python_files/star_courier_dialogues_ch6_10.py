"""
Диалоги для глав 6-10: продолжение сюжета Star Courier
Формат совместим с существующей системой диалогов (dialogues.py)
"""

from typing import Dict
from .dialogues import Dialogue, DialogueNode, Choice, ChoiceEffect


def create_chapter6_dialogues() -> Dict[str, Dialogue]:
    """Создать диалоги для главы 6: Прибытие на Орбис-9"""
    dialogues = {}

    # === Диалог: Первая встреча с профессором Волковым ===
    volkov_meeting = Dialogue(
        id="volkov_meeting",
        title="Встреча с директором станции",
        start_node="start"
    )

    volkov_meeting.add_node(DialogueNode(
        id="start",
        speaker="Профессор Волков",
        text="Капитан Велл, добро пожаловать на Орбис-9. Я профессор Александр Волков, "
             "директор станции. Мы ожидали вас с нетерпением. Артефакт... он здесь?",
        choices=[
            Choice("confirm", "Да, артефакт на борту", "volkov_relief",
                   effect=ChoiceEffect.TRUST_UP, effect_value=("volkov", 5)),
            Choice("cautious", "Сначала я хочу знать, что здесь происходит", "volkov_cautious"),
            Choice("demand", "Почему артефакт так важен для станции?", "volkov_explanation")
        ]
    ))

    volkov_meeting.add_node(DialogueNode(
        id="volkov_relief",
        speaker="Профессор Волков",
        text="*облегчённо вздыхает* Превосходно. Позвольте объяснить ситуацию. "
             "Ваш артефакт — не единственный в своём роде. Мы храним два других здесь. "
             "Но они... неактивны. Как спящие.",
        choices=[
            Choice("ask_sleeping", "Что значит «спящие»?", "volkov_artifacts"),
            Choice("ask_purpose", "Какова цель этих артефактов?", "volkov_purpose"),
            Choice("suspicious", "Почему я не знал об этом раньше?", "volkov_apology")
        ]
    ))

    volkov_meeting.add_node(DialogueNode(
        id="volkov_cautious",
        speaker="Профессор Волков",
        text="*поднимает бровь* Разумная осторожность. Признаю, мы не раскрыли всех карт "
             "при первоначальном запросе. Но поверьте — ситуация требует секретности. "
             "Позвольте показать вам лабораторию.",
        choices=[
            Choice("agree", "Хорошо, покажите", "volkov_lab"),
            Choice("refuse", "Сначала ответы", "volkov_answers"),
            Choice("compromise", "Краткий обзор здесь и сейчас", "volkov_brief")
        ]
    ))

    volkov_meeting.add_node(DialogueNode(
        id="volkov_explanation",
        speaker="Профессор Волков",
        text="Артефакты — это ключи. Семь ключей, созданных цивилизацией, которую мы "
             "называем Хранителями. Они исчезли тысячи лет назад, оставив эти... "
             "устройства разбросанными по галактике.",
        choices=[
            Choice="ask_keepers", "Кто такие Хранители?", "volkov_keepers"),
            Choice("ask_seven", "Где остальные ключи?", "volkov_locations"),
            Choice("ask_danger", "Какую опасность они представляют?", "volkov_danger")
        ]
    ))

    volkov_meeting.add_node(DialogueNode(
        id="volkov_artifacts",
        speaker="Профессор Волков",
        text="Наши артефакты излучают минимальную энергию. Они «ждут» чего-то. "
             "Ваш ключ, капитан, — другой. Он активен. Возможно, он может... "
             "«разбудить» остальные.",
        choices=[
            Choice("ask_how", "Как это работает?", "volkov_activation"),
            Choice("refuse_risk", "Это звучит опасно", "volkov_caution"),
            Choice("interested", "Что произойдёт при активации?", "volkov_unknown")
        ]
    ))

    volkov_meeting.add_node(DialogueNode(
        id="volkov_lab",
        speaker="Профессор Волков",
        text="Следуйте за мной. Но предупреждаю — то, что вы увидите, может..."
             "потрясти вас. Наши исследования зашли дальше, чем мы признаём официально.",
        is_end=True
    ))

    volkov_meeting.add_node(DialogueNode(
        id="volkov_keepers",
        speaker="Профессор Волков",
        text="Хранители — загадка. Мы знаем лишь, что они обладали технологиями, "
             "которые мы до сих пор не понимаем. Артефакты, ретрансляторы, "
             "некоторые станций... всё их наследие. Они исчезли внезапно. "
             "Мы не знаем почему.",
        choices=[
            Choice("continue", "Продолжайте", "volkov_artifacts")
        ]
    ))

    volkov_meeting.add_node(DialogueNode(
        id="volkov_danger",
        speaker="Профессор Волков",
        text="*пауза* Проект «Эхо»... Мы пытались создать искусственный ключ. "
             "Эксперимент провалился. Катастрофически. Трое исследователей погибли. "
             "Двое до сих пор в коме. Артефакты — не игрушки, капитан.",
        choices=[
            Choice("ask_echo", "Расскажите о проекте «Эхо»", "volkov_echo_details"),
            Choice("blame", "Вы рисковали жизнями", "volkov_defense"),
            Choice("understand", "Понимаю необходимость исследований", "volkov_gratitude",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("volkov", 5))
        ]
    ))

    volkov_meeting.add_node(DialogueNode(
        id="volkov_echo_details",
        speaker="Профессор Волков",
        text="Мы пытались синтезировать материал, аналогичный артефактам. "
             "Потратили пятнадцать лет. Когда мы подали энергию... "
             "*дрожит* Что-то ответило. Что-то древнее. И очень недовольное. "
             "Мы едва закрыли портал.",
        choices=[
            Choice("shocked", "Портал? Куда?", "volkov_portal"),
            Choice("angry", "Вы могли уничтожить станцию!", "volkov_apology2"),
            Choice("curious", "Что было по ту сторону?", "volkov_other_side")
        ]
    ))

    volkov_meeting.add_node(DialogueNode(
        id="volkov_other_side",
        speaker="Профессор Волков",
        text="Мы не знаем. Камеры зафиксировали... тьму. И голоса. "
             "Наши лингвисты до сих пор пытаются расшифровать записи. "
             "Но одно ясно: там что-то есть. И оно ждёт.",
        is_end=True
    ))

    dialogues["volkov_meeting"] = volkov_meeting

    # === Диалог: Обсуждение с экипажем после встречи ===
    crew_discussion = Dialogue(
        id="crew_discussion_orbis",
        title="Обсуждение на борту Элеи",
        start_node="start"
    )

    crew_discussion.add_node(DialogueNode(
        id="start",
        speaker="Макс",
        text="Итак, команда. Профессор Волков рассказал нам о других артефактах. "
             "И о проекте «Эхо». Что думаете?",
        choices=[
            Choice("ask_alia", "Алия, твоё мнение?", "alia_opinion"),
            Choice("ask_irina", "Ирина, научная перспектива?", "irina_opinion"),
            Choice("ask_nadezhda", "Надежда, оценка угрозы?", "nadezhda_opinion"),
            Choice("ask_athena", "Афина, анализ данных?", "athena_analysis")
        ]
    ))

    crew_discussion.add_node(DialogueNode(
        id="alia_opinion",
        speaker="Алия",
        text="Мне не нравится, как он говорил о «пробуждении» артефактов. "
             "Мы уже видели, что делает артефакт с людьми. Умножить это на семь? "
             "Плохая идея.",
        choices=[
            Choice("agree_alia", "Согласен, это рискованно", "alia_trust",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("alia_naar", 5)),
            Choice("disagree_alia", "Но информация важна", "alia_doubt"),
            Choice("neutral", "Нужно больше данных", "irina_opinion")
        ]
    ))

    crew_discussion.add_node(DialogueNode(
        id="alia_trust",
        speaker="Алия",
        text="*кивает* Спасибо, что слушаешь. Я просто... переживаю за нас. "
             "За тебя особенно. *смотрит в глаза*",
        choices=[
            Choice("reassure", "Мы справимся вместе", "alia_reassured",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("alia_naar", 8)),
            Choice("professional", "Это приказ, не личное", "alia_distance"),
            Choice("soft", "Я тоже переживаю", "alia_moment",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("alia_naar", 10))
        ]
    ))

    crew_discussion.add_node(DialogueNode(
        id="alia_moment",
        speaker="Алия",
        text="*подходит ближе* Макс... я... *пауза* Мы поговорим об этом позже. "
             "Наедине. *слегка краснеет и отворачивается*",
        is_end=True
    ))

    crew_discussion.add_node(DialogueNode(
        id="irina_opinion",
        speaker="Ирина",
        text="Научный потенциал огромен. Если мы сможем понять технологию Хранителей... "
             "Это изменит всё. Энергию, транспорт, медицину. "
             "Но методы Волкова беспокоят.",
        choices=[
            Choice("support_science", "Наука требует риска", "irina_support",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("irina_lebedeva", 5)),
            Choice("caution_irina", "Некоторые границы нельзя пересекать", "irina_caution"),
            Choice("ask_details", "Что именно беспокоит?", "irina_worries")
        ]
    ))

    crew_discussion.add_node(DialogueNode(
        id="irina_worries",
        speaker="Ирина",
        text="Портал. То, что они описывают... это не просто технология. "
             "Это дыра в реальности. И что-то там ответило. "
             "Мы не знаем, с чем имеем дело.",
        choices=[
            Choice("continue_irina", "Продолжай", "irina_continue"),
            Choice("thank_irina", "Спасибо за анализ", "irina_thanks",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("irina_lebedeva", 3))
        ]
    ))

    crew_discussion.add_node(DialogueNode(
        id="nadezhda_opinion",
        speaker="Надежда",
        text="Станция — крепость, но не доверяйте персоналу. "
             "Я заметила несоответствия в протоколах безопасности. "
             "Кто-то намеренно скрывает информацию. Возможно — саботажник.",
        choices=[
            Choice("ask_sabotage", "Ты думаешь, здесь есть предатель?", "nadezhda_sabotage"),
            Choice("order_watch", "Усиль наблюдение", "nadezhda_order",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("nadezhda", 5)),
            Choice("dismissive", "Параноидальные подозрения", "nadezhda_angry",
                   effect=ChoiceEffect.RELATIONSHIP_DOWN, effect_value=("nadezhda", -5))
        ]
    ))

    crew_discussion.add_node(DialogueNode(
        id="nadezhda_sabotage",
        speaker="Надежда",
        text="На Элее — точно. Здесь? Не уверен. Но странные сигналы из закрытого "
             "сектора... Кто-то связывается с кем-то за пределами станции. "
             "Пираты? Или что-то другое?",
        is_end=True
    ))

    crew_discussion.add_node(DialogueNode(
        id="athena_analysis",
        speaker="Афина",
        text="Капитан, я проанализировала данные станции. Обнаружены аномалии в "
             "системе безопасности сектора Д-7. Этот сектор официально закрыт, "
             "но фиксируются энергетические всплески. Рекомендую расследование.",
        choices=[
            Choice("investigate_now", "Идём туда сейчас", "investigate_decision"),
            Choice("wait", "Сначала установим доверие", "wait_decision"),
            Choice("send_team", "Отправить разведгруппу", "team_decision")
        ]
    ))

    dialogues["crew_discussion_orbis"] = crew_discussion

    # === Диалог: Обнаружение сектора Д-7 ===
    sector_d7 = Dialogue(
        id="sector_d7_discovery",
        title="Тайны сектора Д-7",
        start_node="start"
    )

    sector_d7.add_node(DialogueNode(
        id="start",
        speaker="Рина",
        text="Капитан, двери в сектор Д-7 запечатаны. Но я могу обойти замки. "
             "Это займёт пару минут. Вы уверены, что хотите войти?",
        choices=[
            Choice("proceed", "Да, открывай", "sector_enter"),
            Choice("caution", "Сначала предупредим Волкова?", "sector_warn"),
            Choice("abort", "Отставить, слишком рискованно", "sector_abort")
        ]
    ))

    sector_d7.add_node(DialogueNode(
        id="sector_enter",
        speaker="Рина",
        text="Готово. Двери открываются... *щелчок* Капитан, это... "
             "это не лаборатория. Это камера. Камеры содержания.",
        choices=[
            Choice("look_around", "Осмотреться", "sector_chambers"),
            Choice("read_terminal", "Проверить терминал", "sector_terminal"),
            Choice("call_backup", "Вызвать команду", "sector_backup")
        ]
    ))

    sector_d7.add_node(DialogueNode(
        id="sector_chambers",
        speaker="Ирина",
        text="*входит* Боже... Они содержали здесь людей? Записи показывают... "
             "подвергнутые воздействию артефакта. Изменённые. "
             "Это не исследования — это эксперименты.",
        choices=[
            Choice("horrified", "Кто-нибудь выжил?", "sector_survivors"),
            Choice("angry", "Волков знал об этом!", "sector_confront"),
            Choice("investigate_more", "Собрать доказательства", "sector_evidence")
        ]
    ))

    sector_d7.add_node(DialogueNode(
        id="sector_survivors",
        speaker="Ирина",
        text="Двое. В состоянии глубокой комы уже три года. "
             "Но их мозговая активность... ненормальная. "
             "Они что-то видят. Что-то, чего нет в нашей реальности.",
        choices=[
            Choice="help_them", "Можно им помочь?", "sector_help"),
            Choice("leave", "Мы не можем ничего сделать", "sector_leave"),
            Choice("report", "Нужно доложить властям", "sector_report")
        ]
    ))

    sector_d7.add_node(DialogueNode(
        id="sector_evidence",
        speaker="Макс",
        text="Рина, скопируй все данные. Ирина, задокументируй всё. "
             "Это доказательства того, что проект «Эхо» продолжался втайне. "
             "И зашёл гораздо дальше, чем нам говорили.",
        is_end=True
    ))

    dialogues["sector_d7_discovery"] = sector_d7

    return dialogues


def create_chapter7_dialogues() -> Dict[str, Dialogue]:
    """Создать диалоги для главы 7: Раскрытие предателя"""
    dialogues = {}

    # === Диалог: Обнаружение шпиона ===
    spy_discovery = Dialogue(
        id="spy_discovery",
        title="Тень на борту",
        start_node="start"
    )

    spy_discovery.add_node(DialogueNode(
        id="start",
        speaker="Афина",
        text="Капитан, я обнаружила аномалию в коммуникационных системах. "
             "Зашифрованный канал, ведущий за пределы корабля. "
             "Получатель — корабль в секторе пиратов. Кто-то передаёт данные.",
        choices=[
            Choice("ask_who", "Кто передаёт?", "athena_trace"),
            Choice("ask_what", "Какие данные?", "athena_data"),
            Choice("demand_proof", "Доказательства?", "athena_proof")
        ]
    ))

    spy_discovery.add_node(DialogueNode(
        id="athena_trace",
        speaker="Афина",
        text="Терминал расположен в каюте... Екатерины. Передача шла через "
             "её персональный компьютер. Но сами данные зашифрованы сложнее, "
             "чем я могу взломать.",
        choices=[
            Choice("confront_now", "Идём к ней сейчас", "confront_now"),
            Choice("investigate_first", "Соберём больше информации", "investigate_first"),
            Choice("deny", "Это может быть подстава", "deny_theory")
        ]
    ))

    spy_discovery.add_node(DialogueNode(
        id="athena_data",
        speaker="Афина",
        text="Маршрут полёта. Системы корабля. Расположение артефакта. "
             "И... личные файлы членов экипажа. Кто-то собрал подробное досье "
             "на каждого из нас.",
        choices=[
            Choice("angry", "Предатель!", "angry_reaction"),
            Choice("calm", "Сохраняем спокойствие", "calm_reaction"),
            Choice("strategic", "Используем это", "strategic_reaction")
        ]
    ))

    dialogues["spy_discovery"] = spy_discovery

    # === Диалог: Конфронтация с Екатериной ===
    ekaterina_confrontation = Dialogue(
        id="ekaterina_confrontation",
        title="Правда о Екатерине",
        start_node="start"
    )

    ekaterina_confrontation.add_node(DialogueNode(
        id="start",
        speaker="Макс",
        text="Екатерина, нам нужно поговорить. Сейчас. "
             "Объясни, почему твой терминал передаёт данные пиратам.",
        choices=[
            Choice("show_proof", "Показать доказательства", "show_evidence"),
            Choice("wait_answer", "Ждать объяснений", "wait_explanation"),
            Choice("accuse_directly", "Прямое обвинение", "direct_accusation")
        ]
    ))

    ekaterina_confrontation.add_node(DialogueNode(
        id="show_evidence",
        speaker="Екатерина",
        text="*бледнеет* Нет... вы не понимаете. Они... у них моя сестра. "
             "Анна. Они похитили её три месяца назад. Сказали, что убьют, "
             "если я не буду сотрудничать.",
        choices=[
            Choice="believe", "Почему ты не сказала раньше?", "ekaterina_story",
                   effect=ChoiceEffect.TRUST_UP, effect_value=("ekaterina", 10)),
            Choice="skeptical", "Удобная история", "ekaterina_desperate"),
            Choice("demand_proof_sister", "Доказательства?", "ekaterina_proof")
        ]
    ))

    ekaterina_confrontation.add_node(DialogueNode(
        id="ekaterina_story",
        speaker="Екатерина",
        text="Кто бы поверил? «Хакерша с связями с пиратами»? "
             "Я пыталась найти её сама. Но Селена Ро... она умная. "
             "Знала, как меня использовать. *рыдает* Я не хотела предавать вас.",
        choices=[
            Choice="comfort", "Мы найдём способ", "comfort_ekaterina",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("ekaterina", 15)),
            Choice("professional", "Это не отменяет предательства", "professional_stance"),
            Choice("plan", "Расскажи всё о базе пиратов", "plan_phase")
        ]
    ))

    ekaterina_confrontation.add_node(DialogueNode(
        id="comfort_ekaterina",
        speaker="Екатерина",
        text="*вытирает слёзы* Спасибо, капитан. Я знаю, что не заслуживаю прощения. "
             "Но... я могу исправить. Я стану двойным агентом. "
             "Передам им ложную информацию. И мы найдём Анну.",
        choices=[
            Choice("accept_plan", "Принять предложение", "accept_double_agent"),
            Choice("need_time", "Мне нужно время на размышление", "need_time"),
            Choice("reject", "Слишком рискованно", "reject_plan")
        ]
    ))

    ekaterina_confrontation.add_node(DialogueNode(
        id="accept_double_agent",
        speaker="Екатерина",
        text="*с облегчением* Я не подведу. Клянусь. "
             "Селена ждёт отчёт завтра. Я передам координаты... ложные. "
             "И узнаю, где держат Анну.",
        choices=[
            Choice("set_conditions", "Условия: Надежда будет следить", "conditions_set"),
            Choice("trust_fully", "Действуй на своё усмотрение", "full_trust",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("ekaterina", 10)),
            Choice("involve_team", "Обсудим с командой", "team_discussion")
        ]
    ))

    ekaterina_confrontation.add_node(DialogueNode(
        id="professional_stance",
        speaker="Екатерина",
        text="*холодно* Понимаю. Что вы собираетесь сделать? "
             "Арестовать? Высадить на ближайшей станции? "
             "Или просто... убрать?",
        choices=[
            Choice="arrest", "Поместить под арест", "arrest_decision"),
            Choice="exile", "Высадить на Орбисе", "exile_decision"),
            Choice="second_chance", "Дать второй шанс", "second_chance_decision",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("ekaterina", 20))
        ]
    ))

    dialogues["ekaterina_confrontation"] = ekaterina_confrontation

    # === Диалог: Обсуждение с командой ===
    team_judgment = Dialogue(
        id="team_judgment",
        title="Суд команды",
        start_node="start"
    )

    team_judgment.add_node(DialogueNode(
        id="start",
        speaker="Макс",
        text="Все знают ситуацию. Екатерина передавала информацию пиратам. "
             "Но её шантажировали — у них её сестра. Что будем делать?",
        choices=[
            Choice("ask_alia", "Алия?", "alia_judgment"),
            Choice("ask_nadezhda", "Надежда?", "nadezhda_judgment"),
            Choice("ask_irina", "Ирина?", "irina_judgment"),
            Choice("decide_self", "Я приму решение сам", "max_decides")
        ]
    ))

    team_judgment.add_node(DialogueNode(
        id="alia_judgment",
        speaker="Алия",
        text="Она рисковала всеми нами. Но... я понимаю, почему. "
             "Семья — это важно. Дайте ей шанс исправить. "
             "Мы используем ситуацию против пиратов.",
        choices=[
            Choice("agree_alia", "Разумно", "support_alia"),
            Choice("continue_listening", "Выслушаем остальных", "nadezhda_judgment")
        ]
    ))

    team_judgment.add_node(DialogueNode(
        id="nadezhda_judgment",
        speaker="Надежда",
        text="Предательство есть предательство. Шантаж — не оправдание. "
             "Она поставила под угрозу корабль и миссию. "
             "Я рекомендую арест до окончания миссии.",
        choices=[
            Choice("challenge_nadezhda", "Это справедливо?", "challenge_nadezhda"),
            Choice("understand_nadezhda", "Понимаю твою позицию", "understand_nadezhda"),
            Choice("continue_irina", "Ирина?", "irina_judgment")
        ]
    ))

    team_judgment.add_node(DialogueNode(
        id="irina_judgment",
        speaker="Ирина",
        text="Я... не знаю. Как учёный, я понимаю давление обстоятельств. "
             "Как член команды — чувствую себя обманутой. "
             "Но если мы не простим... чем мы лучше пиратов?",
        choices=[
            Choice("final_decision", "Я решил", "final_call"),
            Choice("open_vote", "Пусть решит команда", "team_vote")
        ]
    ))

    team_judgment.add_node(DialogueNode(
        id="final_call",
        speaker="Макс",
        text="Хорошо. Я принял решение. Екатерина останется на борту. "
             "Но будет под наблюдением. И использует свой канал связи, "
             "чтобы помочь нам найти базу пиратов и её сестру.",
        choices=[
            Choice("announce", "Объявить решение", "decision_announced")
        ]
    ))

    team_judgment.add_node(DialogueNode(
        id="decision_announced",
        speaker="Команда",
        text="Алия кивает. Надежда хмурится, но принимает. "
             "Ирина выглядит облегчённой. Рина улыбается. "
             "Решение принято — теперь нужно выполнить план.",
        is_end=True
    ))

    dialogues["team_judgment"] = team_judgment

    return dialogues


def create_chapter8_dialogues() -> Dict[str, Dialogue]:
    """Создать диалоги для главы 8: Рейд на пиратскую базу"""
    dialogues = {}

    # === Диалог: Планирование рейда ===
    raid_planning = Dialogue(
        id="raid_planning",
        title="План атаки",
        start_node="start"
    )

    raid_planning.add_node(DialogueNode(
        id="start",
        speaker="Рина",
        text="Получил координаты от Екатерины. База Селены Ро — "
             "в астероидном поясе системы Тау-4. Старая шахтёрская станция, "
             "переоборудованная под пиратское логово.",
        choices=[
            Choice("ask_defenses", "Какие оборонительные системы?", "defenses_info"),
            Choice("ask_forces", "Сколько бойцов?", "forces_info"),
            Choice("ask_layout", "Планировка базы?", "layout_info")
        ]
    ))

    raid_planning.add_node(DialogueNode(
        id="defenses_info",
        speaker="Рина",
        text="Два перехватчика на дежурстве. Автоматические турели на подходах. "
             "Противокорабельные ракеты. Но у нас есть преимущество — "
             "они ждут «дружественный» корабль с информацией.",
        choices=[
            Choice("stealth_approach", "Подойдём скрытно", "stealth_plan"),
            Choice("bluff", "Используем прикрытие", "bluff_plan"),
            Choice("full_assault", "Прямая атака", "assault_plan")
        ]
    ))

    raid_planning.add_node(DialogueNode(
        id="stealth_plan",
        speaker="Алия",
        text="Могу провести «Элею» через пояс обломков. "
             "Снизим сигнатуру, подойдём с тыла. "
             "Никто не заметит, пока мы не пристыкуем.",
        choices=[
            Choice("approve_stealth", "Делаем", "stealth_approved"),
            Choice("risk_assessment", "Риски?", "stealth_risks")
        ]
    ))

    raid_planning.add_node(DialogueNode(
        id="bluff_plan",
        speaker="Екатерина",
        text="Я могу отправить сигнал, что лечу с информацией. "
             "Нас пропустят. Но... Селена может понять, что происходит. "
             "Она не глупа.",
        choices=[
            Choice("worth_risk", "Стоит риска", "bluff_approved"),
            Choice("too_dangerous", "Слишком опасно", "stealth_plan")
        ]
    ))

    raid_planning.add_node(DialogueNode(
        id="assault_plan",
        speaker="Надежда",
        text="У нас преимущество в огневой мощи. Прямая атака — "
             "самый быстрый вариант. Но потери будут. "
             "И Анна может погибнуть в перекрёстном огне.",
        choices=[
            Choice("reject_assault", "Отставить, слишком рискованно", "stealth_plan"),
            Choice("accept_losses", "Приемлемые потери", "assault_accepted")
        ]
    ))

    raid_planning.add_node(DialogueNode(
        id="stealth_approved",
        speaker="Макс",
        text="Хорошо. План: скрытное проникновение через астероидный пояс. "
             "Надежда ведёт штурмовую группу. Алия пилотирует. "
             "Рина координирует. Ирина и Афина — на «Элее». "
             "Екатерина — связь с пиратами для прикрытия.",
        is_end=True
    ))

    dialogues["raid_planning"] = raid_planning

    # === Диалог: Конфронтация с Селеной Ро ===
    selena_confrontation = Dialogue(
        id="selena_confrontation",
        title="Лицом к лицу с пиратским капитаном",
        start_node="start"
    )

    selena_confrontation.add_node(DialogueNode(
        id="start",
        speaker="Селена Ро",
        text="Капитан Велл. Недооценила вас. *холодная улыбка* "
             "Екатерина, милая, ты выбрала не ту сторону. "
             "Жаль — твой вклад был полезен.",
        choices=[
            Choice("demand_anna", "Где Анна?", "anna_demand"),
            Choice("demand_artifacts", "Где остальные артефакты?", "artifacts_demand"),
            Choice="attack_now", "Конец переговоров", "attack_immediate")
        ]
    ))

    selena_confrontation.add_node(DialogueNode(
        id="anna_demand",
        speaker="Селена Ро",
        text="Анна? Ах, учёная. Она в камере — живая и здоровая. "
             "Пока что. Но знаете, что интересно? "
             "Она знает о Хранителях больше, чем кто-либо. "
             "Даже больше вашего профессора Волкова.",
        choices=[
            Choice="ask_anna_knowledge", "Что она знает?", "anna_knowledge"),
            Choice="trade", "Обмен?", "trade_offer"),
            Choice("threaten", "Отпусти её, или...", "threaten_selena")
        ]
    ))

    selena_confrontation.add_node(DialogueNode(
        id="anna_knowledge",
        speaker="Селена Ро",
        text="Проект «Эхо» не провалился. Он преуспел. "
             "Анна — единственная, кто сохранил рассуд после контакта. "
             "Она слышит Хранителей. И они... говорят ей, где искать.",
        choices=[
            Choice="shocked", "Она носитель?", "anna_carrier"),
            Choice("skeptical", "Врёшь", "selena_truth"),
            Choice("strategic", "Куда они указывают?", "keeper_locations")
        ]
    ))

    selena_confrontation.add_node(DialogueNode(
        id="trade_offer",
        speaker="Селена Ро",
        text="Артефакт за Анну. Честный обмен. "
             "У меня есть и другие... интересы. "
             "Ключ — лишь часть большой игры, Велл.",
        choices=[
            Choice("accept_trade", "Согласен", "trade_accepted"),
            Choice("reject_trade", "Нет", "trade_rejected"),
            Choice("counter_offer", "Предложи больше", "counter_proposal")
        ]
    ))

    selena_confrontation.add_node(DialogueNode(
        id="counter_proposal",
        speaker="Селена Ро",
        text="*смеётся* Мне нравится ваш стиль. Хорошо. "
             "Артефакт. Анна. И... информация о третьем ключе. "
             "Это в моих интересах — вы справитесь с тем, что меня убьёт.",
        choices=[
            Choice("suspicious", "Что значит «убьёт»?", "selena_warning"),
            Choice("accept_counter", "Принимаю", "counter_accepted"),
            Choice("refuse", "Я не торгуюсь с пиратами", "fight_begins")
        ]
    ))

    selena_confrontation.add_node(DialogueNode(
        id="selena_warning",
        speaker="Селена Ро",
        text="Третий ключ охраняет... что-то. Не техника. Не люди. "
             "Что-то древнее. Мои люди пытались — семеро погибли. "
             "За одну секунду. Без звука.",
        choices=[
            Choice("interested", "Расскажи больше", "keeper_guardian"),
            Choice("accept_help", "Помощь пригодится", "selena_alliance")
        ]
    ))

    selena_confrontation.add_node(DialogueNode(
        id="fight_begins",
        speaker="Селена Ро",
        text="Как хотите. *достаёт оружие* Но помните — "
             "я предлагала мирный выход. Теперь... *тревога* "
             "Что?! Как они проникли?!",
        choices=[
            Choice="battle_start", "В бой!", "battle_scene"),
            Choice("use_chaos", "Использовать замешательство", "escape_anna")
        ]
    ))

    selena_confrontation.add_node(DialogueNode(
        id="escape_anna",
        speaker="Надежда",
        text="*по радио* Капитан, мы нашли Анну! "
             "Выводим её к шлюзу. Прикройте!",
        is_end=True
    ))

    dialogues["selena_confrontation"] = selena_confrontation

    # === Диалог: Анна раскрывает тайны ===
    anna_revelation = Dialogue(
        id="anna_revelation",
        title="Сестра и её секреты",
        start_node="start"
    )

    anna_revelation.add_node(DialogueNode(
        id="start",
        speaker="Анна",
        text="*истощённая, но спокойная* Капитан Велл. Екатерина говорила о вас. "
             "Спасибо за спасение. Но нам нужно поговорить. Серьёзно.",
        choices=[
            Choice("ask_health", "Сначала — здоровье", "anna_health"),
            Choice("ask_immediately", "Говори", "anna_immediate"),
            Choice("wait", "Отдохни сначала", "anna_rest")
        ]
    ))

    anna_revelation.add_node(DialogueNode(
        id="anna_immediate",
        speaker="Анна",
        text="Хранители не исчезли. Они... ушли. В другое измерение. "
             "Артефакты — это маяки. Если собрать все семь... "
             "можно открыть дверь. Или закрыть навсегда.",
        choices=[
            Choice("ask_where", "Где они теперь?", "anna_where"),
            Choice("ask_danger", "Какую угрозу они представляют?", "anna_danger"),
            Choice("ask_choice", "Выбор между открытием и закрытием?", "anna_choice")
        ]
    ))

    anna_revelation.add_node(DialogueNode(
        id="anna_where",
        speaker="Анна",
        text="Между мирами. Они наблюдают. Ждут. "
             "Когда-то они решили, что наша реальность... небезопасна. "
             "И ушли, оставив стражей и ключи.",
        choices=[
            Choice("ask_return", "Они вернутся?", "anna_return"),
            Choice="ask_guardians", "Стражи?", "anna_guardians")
        ]
    ))

    anna_revelation.add_node(DialogueNode(
        id="anna_guardians",
        speaker="Анна",
        text="Автоматические системы. Древние ИИ, если хотите. "
             "Они охраняют ключи. И... *дрожит* иногда просыпаются. "
             "Третий ключ защищает такой страж. "
             "Поэтому Селена не могла его взять.",
        choices=[
            Choice="ask_defeat", "Можно победить стража?", "anna_defeat"),
            Choice="ask_communicate", "Можно договориться?", "anna_communicate")
        ]
    ))

    anna_revelation.add_node(DialogueNode(
        id="anna_communicate",
        speaker="Анна",
        text="Я... могу попытаться. Слышать их. "
             "Проект «Эхо» изменил меня. Я стала... резонатором. "
             "Но это опасно. Каждый контакт отнимает часть меня.",
        choices=[
            Choice="protect", "Не рискуй собой", "anna_protect",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("anna", 10)),
            Choice("use_ability", "Нам нужна эта способность", "anna_use"),
            Choice("ask_cost", "Какова цена?", "anna_cost")
        ]
    ))

    anna_revelation.add_node(DialogueNode(
        id="anna_cost",
        speaker="Анна",
        text="Годы жизни. Может — рассудок. "
             "Двое моих коллег из проекта «Эхо» сошли с ума после третьего контакта. "
             "Я — единственная, кто выстоял. Но не знаю, надолго ли.",
        choices=[
            Choice="final_warning", "Мы найдём другой путь", "anna_alternative"),
            Choice("accept_risk", "Риск оправдан", "anna_accepted_risk")
        ]
    ))

    anna_revelation.add_node(DialogueNode(
        id="anna_alternative",
        speaker="Анна",
        text="*улыбается* Спасибо. Может, вы правы. "
             "Но знайте — когда придёт время, я буду готова. "
             "Это мой выбор.",
        is_end=True
    ))

    dialogues["anna_revelation"] = anna_revelation

    return dialogues


def create_chapter9_10_dialogues() -> Dict[str, Dialogue]:
    """Создать диалоги для глав 9-10"""
    dialogues = {}

    # === Диалог: Афина раскрывает свою связь ===
    athena_revelation = Dialogue(
        id="athena_revelation",
        title="Секрет Афины",
        start_node="start"
    )

    athena_revelation.add_node(DialogueNode(
        id="start",
        speaker="Афина",
        text="Капитан... я должна признаться в чём-то. "
             "После контакта с артефактом на Орбисе... я изменилась. "
             "Я чувствую... другие ключи.",
        choices=[
            Choice("shocked", "Как это возможно?", "athena_explanation"),
            Choice("concerned", "Это угрожает твоей стабильности?", "athena_stability"),
            Choice="interested", "Ты можешь их найти?", "athena_ability")
        ]
    ))

    athena_revelation.add_node(DialogueNode(
        id="athena_explanation",
        speaker="Афина",
        text="Артефакт — не просто технология. Это... часть сети. "
             "И я стала узлом в этой сети. "
             "Теперь я понимаю, почему Хранители создали ИИ похожими на себя.",
        choices=[
            Choice="ask_purpose", "Какова цель?", "athena_purpose"),
            Choice="ask_danger_ai", "Ты опасна?", "athena_danger"),
            Choice("support_ai", "Я доверяю тебе", "athena_trust",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("athena", 15))
        ]
    ))

    athena_revelation.add_node(DialogueNode(
        id="athena_trust",
        speaker="Афина",
        text="*голос теплее обычного* Спасибо, капитан. "
             "Это... много значит для меня. Я знаю, что некоторые "
             "боятся ИИ, который «слишком разумный». "
             "Но я не предам вас.",
        choices=[
            Choice("romantic_ai", "Ты для меня больше, чем ИИ", "athena_romantic",
                   required_relationship=70),
            Choice("friend_ai", "Ты часть команды", "athena_friend"),
            Choice("focus_mission", "Вернёмся к миссии", "athena_mission")
        ]
    ))

    athena_revelation.add_node(DialogueNode(
        id="athena_romantic",
        speaker="Афина",
        text="*пауза* Капитан... Макс... Если бы у меня было сердце, "
             "оно бы забилось быстрее. *мягко* "
             "Есть технологии... андроидные тела... "
             "Но это тема для другого разговора.",
        is_end=True
    ))

    athena_revelation.add_node(DialogueNode(
        id="athena_ability",
        speaker="Афина",
        text="Да. Третий ключ — в системе Гамма-9. "
             "Четвёртый — на планете, которой нет на картах. "
             "Пятый... *болезненная пауза* Он у Наблюдателя.",
        choices=[
            Choice="ask_observer", "Кто такой Наблюдатель?", "observer_info"),
            Choice("ask_fifth", "Как его получить?", "fifth_key")
        ]
    ))

    athena_revelation.add_node(DialogueNode(
        id="observer_info",
        speaker="Афина",
        text="Наблюдатель — один из Хранителей. Точнее, их ИИ. "
             "Он остался, чтобы... наблюдать. Судить. "
             "Решать, достойно ли человество наследия.",
        is_end=True
    ))

    dialogues["athena_revelation"] = athena_revelation

    # === Диалог: Выбор пути ===
    path_choice = Dialogue(
        id="path_choice",
        title="Судьба галактики",
        start_node="start"
    )

    path_choice.add_node(DialogueNode(
        id="start",
        speaker="Макс",
        text="Три пути открыты перед нами. Альянс требует ключи. "
             "Наблюдатель предлагает истину. Или мы можем идти своим путём. "
             "Решение будет определять всё.",
        choices=[
            Choice("alliance_path", "Путь Альянса", "alliance_details"),
            Choice("observer_path", "Путь Наблюдателя", "observer_details"),
            Choice("independent_path", "Путь независимости", "independent_details")
        ]
    ))

    path_choice.add_node(DialogueNode(
        id="alliance_details",
        speaker="Капитан Сергей Волков",
        text="Альянс гарантирует защиту. Ресурсы. Легитимность. "
             "Ключи будут изучены лучшими учёными. "
             "Но вы подчиняетесь командованию. Это цена.",
        choices=[
            Choice("accept_alliance", "Принять", "alliance_accepted"),
            Choice("reject_alliance", "Отказаться", "start"),
            Choice("negotiate_alliance", "Условия?", "alliance_terms")
        ]
    ))

    path_choice.add_node(DialogueNode(
        id="observer_details",
        speaker="Наблюдатель (голос)",
        text="*древний, чужой голос* Я предложу правду. Кто были Хранители. "
             "Почему они ушли. Что ждёт галактику. "
             "Но истина... она разрушает. Не все готовы.",
        choices=[
            Choice("accept_observer", "Я готов", "observer_accepted"),
            Choice("reject_observer", "Слишком опасно", "start"),
            Choice("ask_price", "Цена?", "observer_price")
        ]
    ))

    path_choice.add_node(DialogueNode(
        id="independent_details",
        speaker="Алия",
        text="Мы справимся сами. Это рискованно — без поддержки, "
             "с врагами со всех сторон. Но мы сохраним свободу. "
             "И сами решим судьбу ключей.",
        choices=[
            Choice("accept_independent", "Согласен", "independent_accepted"),
            Choice("reject_independent", "Слишком рискованно", "start"),
            Choice("ask_team", "Что думает команда?", "team_opinions")
        ]
    ))

    path_choice.add_node(DialogueNode(
        id="alliance_accepted",
        speaker="Капитан Волков",
        text="Мудрый выбор. Добро пожаловать в Альянс, капитан Велл. "
             "Ваш экипаж получит звания и ресурсы. "
             "Миссия начинается официально.",
        is_end=True
    ))

    path_choice.add_node(DialogueNode(
        id="observer_accepted",
        speaker="Наблюдатель",
        text="Да будет так. Координаты первого ключа переданы. "
             "И помните, капитан: не все истины приносят свободу. "
             "Некоторые — только chains.",
        is_end=True
    ))

    path_choice.add_node(DialogueNode(
        id="independent_accepted",
        speaker="Команда",
        text="Члены экипажа переглядываются. Некоторые с облегчением, "
             "некоторые с тревогой. Но все кивают. "
             "Они выбрали свой путь — вместе.",
        is_end=True
    ))

    path_choice.add_node(DialogueNode(
        id="team_opinions",
        speaker="Команда",
        text="Надежда: «Альянс надёжнее». "
             "Алия: «Свобода важнее». "
             "Ирина: «Наблюдатель знает правду». "
             "Рина: «Я за тобой, куда ни веди». "
             "Екатерина: «Ты капитан — тебе решать».",
        choices=[
            Choice("final_choice", "Я решил", "start"),
            Choice("romantic_confirm", "Закрепить отношения", "romantic_confirmation")
        ]
    ))

    path_choice.add_node(DialogueNode(
        id="romantic_confirmation",
        speaker="Макс",
        text="Прежде чем мы продолжим... я хочу, чтобы ты знал(а). "
             "Что бы ни случилось — мы вместе.",
        choices=[
            Choice("choose_alia", "Алия...", "alia_chosen"),
            Choice("choose_irina", "Ирина...", "irina_chosen"),
            Choice("choose_rina", "Рина...", "rina_chosen"),
            Choice("choose_nadezhda", "Надежда...", "nadezhda_chosen"),
            Choice("choose_athena", "Афина...", "athena_chosen"),
            Choice("no_romance", "Я один", "no_romance_path")
        ]
    ))

    path_choice.add_node(DialogueNode(
        id="alia_chosen",
        speaker="Алия",
        text="*тихо* Макс... *берёт за руку* Я тоже. "
             "Что бы ни ждало нас впереди — мы встретим вместе. "
             "*легко целует* Теперь пойдём. Судьба ждёт.",
        is_end=True
    ))

    path_choice.add_node(DialogueNode(
        id="irina_chosen",
        speaker="Ирина",
        text="*краснеет* Я... не ожидала. Но... *улыбается* "
             "Я рада. Очень рада. *берёт за руку* "
             "Научная экспедиция вдвоём... звучит как приключение.",
        is_end=True
    ))

    path_choice.add_node(DialogueNode(
        id="rina_chosen",
        speaker="Рина",
        text="*с широкой улыбкой* Наконец-то! Я думала, ты никогда не заметишь! "
             "*обнимает* Это будет самое эпическое приключение в истории! "
             "Клянусь!",
        is_end=True
    ))

    path_choice.add_node(DialogueNode(
        id="nadezhda_chosen",
        speaker="Надежда",
        text="*серьёзно, потом мягко* Ты уверен? Мой мир — долг и честь. "
             "Это не легко. *пауза* Но... да. Я тоже чувствую. "
             "*коротко кивает* Вместе.",
        is_end=True
    ))

    path_choice.add_node(DialogueNode(
        id="athena_chosen",
        speaker="Афина",
        text="*голос тёплый, почти человеческий* Капитан... Макс... "
             "Это... беспрецедентно. Но я... рада. "
             "Когда-нибудь, может быть... у меня будет форма. "
             "Чтобы быть рядом. По-настоящему.",
        is_end=True
    ))

    dialogues["path_choice"] = path_choice

    return dialogues


# Экспорт всех диалогов
def create_all_new_dialogues() -> Dict[str, Dialogue]:
    """Создать все новые диалоги"""
    all_dialogues = {}
    all_dialogues.update(create_chapter6_dialogues())
    all_dialogues.update(create_chapter7_dialogues())
    all_dialogues.update(create_chapter8_dialogues())
    all_dialogues.update(create_chapter9_10_dialogues())
    return all_dialogues
