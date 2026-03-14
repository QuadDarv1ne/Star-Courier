"""
Диалоги для новых персонажей глав 11-15: Зара, Маркус Рид, Рейнер и Кира, Волков (криминальный)
"""

from typing import Dict
from dialogues import Dialogue, DialogueNode, Choice, ChoiceEffect


def create_zara_dialogues() -> Dict[str, Dialogue]:
    """Диалоги для Зары — наёмника (романтический интерес)"""
    dialogues = {}

    # === Первая встреча ===
    zara_first_meeting = Dialogue(
        id="zara_first_meeting",
        title="Наёмник в баре",
        start_node="start"
    )

    zara_first_meeting.add_node(DialogueNode(
        id="start",
        speaker="Зара",
        text="*сидит в углу бара, не отрываясь от напитка. Замечает ваш взгляд* "
             "Что-то нужно? Или просто любите пялиться?",
        choices=[
            Choice("professional", "Ищу квалифицированного бойца", "zara_interested"),
            Choice("casual", "Просто оцениваю обстановку", "zara_dismissive"),
            Choice("direct", "Вы — Зара? Слышал о вашей репутации", "zara_reputation")
        ]
    ))

    zara_first_meeting.add_node(DialogueNode(
        id="zara_interested",
        speaker="Зара",
        text="*отставляет стакан* Квалифицированного? Хм. Это зависит от того, "
             "что вам нужно. И сколько платите. Я не работаю за «спасибо» "
             "или «благородные цели».",
        choices=[
            Choice("offer_job", "5000 кредитов за миссию", "zara_price"),
            Choice("ask_price", "Какова ваша цена?", "zara_negotiate"),
            Choice("test_skill", "Сначала докажите, что стоите денег", "zara_challenge")
        ]
    ))

    zara_first_meeting.add_node(DialogueNode(
        id="zara_reputation",
        speaker="Зара",
        text="*на мгновение напрягается, потом расслабляется* "
             "Репутацию? Зависит от того, что вы слышали. "
             "Если что-то хорошее — врёт. Если плохое — вероятно, правда. "
             "Что вам нужно?",
        choices=[
            Choice("explain_mission", "Миссия по поиску артефактов", "zara_mission"),
            Choice("ask_about_past", "Почему «плохое — правда»?", "zara_past_hint"),
            Choice("offer_alliance", "Предлагаю союз", "zara_alliance")
        ]
    ))

    zara_first_meeting.add_node(DialogueNode(
        id="zara_price",
        speaker="Зара",
        text="5000. Приемлемо для простой охраны. Но если будет бой — "
             "доплачиваете. Если будет серьёзный бой — ещё больше. "
             "И если мне не понравится ваш «артефакт» — я ухожу с авансом. "
             "Условия?",
        choices=[
            Choice("agree_terms", "Согласен на условия", "zara_hired",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("zara", 5)),
            Choice("negotiate", "Давайте обсудим детали", "zara_negotiate_details"),
            Choice("refuse", "Это слишком", "zara_refused")
        ]
    ))

    zara_first_meeting.add_node(DialogueNode(
        id="zara_past_hint",
        speaker="Зара",
        text="*мрачнеет* Долгая история. И не ваша проблема. "
             "Если нанимаете — я делаю работу. Если нет — "
             "не тратьте моё время вопросами о прошлом.",
        choices=[
            Choice("respect_boundary", "Справедливо. Давайте о деле", "zara_respect",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("zara", 3)),
            Choice("push_further", "Прошлое влияет на настоящее", "zara_annoyed"),
            Choice("offer_understanding", "У каждого есть прошлое", "zara_surprised",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("zara", 8))
        ]
    ))

    zara_first_meeting.add_node(DialogueNode(
        id="zara_surprised",
        speaker="Зара",
        text="*смотрит с любопытством* Интересно. Обычно наниматели "
             "хотят знать всё, чтобы потом использовать. "
             "Вы... другой. Хорошо. 4000, и я ваша на эту миссию.",
        choices=[
            Choice("accept_discount", "Принимаю", "zara_hired_discount",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("zara", 5)),
            Choice("ask_why", "Почему скидка?", "zara_explanation")
        ]
    ))

    zara_first_meeting.add_node(DialogueNode(
        id="zara_explanation",
        speaker="Зара",
        text="*слегка улыбается впервые* Потому что вы не пытаетесь "
             "мной манипулировать. Это... редкость. "
             "Так мы договорились?",
        is_end=True
    ))

    zara_first_meeting.add_node(DialogueNode(
        id="zara_hired",
        speaker="Зара",
        text="Хорошо. Когда выезжаем? И ещё — я не предаю нанимателей. "
             "Даже если предают меня. Это единственное правило.",
        is_end=True
    ))

    zara_first_meeting.add_node(DialogueNode(
        id="zara_hired_discount",
        speaker="Зара",
        text="Договорились. *встаёт* Ваш корабль — «Элея»? "
             "Слышала о нём. Приличное судно. Пойдём.",
        is_end=True
    ))

    dialogues["zara_first_meeting"] = zara_first_meeting

    # === Ночной разговор (развитие романтики) ===
    zara_night_talk = Dialogue(
        id="zara_night_talk",
        title="Ночной разговор с Зарой",
        start_node="start"
    )

    zara_night_talk.add_node(DialogueNode(
        id="start",
        speaker="Зара",
        text="*стоит у иллюминатора в коридоре, смотрит на звёзды. "
             "Не оборачивается, когда вы подходите* "
             "Не спится? Мне тоже.",
        choices=[
            Choice("join_silence", "Присоединиться к молчанию", "zara_silence",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("zara", 5)),
            Choice("ask_thoughts", "О чём думаете?", "zara_thoughts"),
            Choice("offer_company", "Хотел проверить, как вы", "zara_company")
        ]
    ))

    zara_night_talk.add_node(DialogueNode(
        id="zara_silence",
        speaker="Зара",
        text="*после долгой паузы* Знаете... давно не было момента, "
             "когда можно просто стоять и ничего не делать. "
             "Всегда работа. Всегда угроза. *тихо* Спасибо за это.",
        choices=[
            Choice("stay_longer", "Остаться подольше", "zara_moment",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("zara", 10)),
            Choice("say_goodnight", "Спокойной ночи", "zara_goodnight"),
            Choice("touch_hand", "Коснуться её руки", "zara_touch",
                   required_relationship=40)
        ]
    ))

    zara_night_talk.add_node(DialogueNode(
        id="zara_thoughts",
        speaker="Зара",
        text="Думаю о... *пауза* О командире, который продал нас "
             "ради премии. О друзьях, которых я потеряла. "
             "О том, почему я всё ещё здесь, с вами. "
             "Наверное, это глупо.",
        choices=[
            Choice("validate", "Это не глупо. Это человечно", "zara_validated",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("zara", 12)),
            Choice("ask_details", "Расскажи больше", "zara_story"),
            Choice("distract", "Лучше не думать о прошлом", "zara_distracted")
        ]
    ))

    zara_night_talk.add_node(DialogueNode(
        id="zara_validated",
        speaker="Зара",
        text="*поворачивается, в глазах что-то новое* "
             "Вы странный, Макс. Большинство людей хотят использовать меня "
             "как оружие. А вы... *негромко* С вами я чувствую себя человеком. "
             "Это... тревожно. Но приятно.",
        choices=[
            Choice("romantic_hint", "Мне тоже приятно с тобой", "zara_romantic",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("zara", 15),
                   required_relationship=50),
            Choice("friendship", "Друзья — это ценно", "zara_friendship"),
            Choice("stay_silent", "Молча кивнуть", "zara_understanding")
        ]
    ))

    zara_night_talk.add_node(DialogueNode(
        id="zara_touch",
        speaker="Зара",
        text="*вздрагивает от прикосновения, но не отстраняется* "
             "Макс... *голос тише обычного* "
             "Я... не привыкла к этому. К прикосновениям. "
             "К тому, чтобы кто-то был рядом.",
        choices=[
            Choice("continue_touch", "Продолжить держать за руку", "zara_intimate",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("zara", 20),
                   required_relationship=55),
            Choice("let_go", "Отпустить", "zara_disappointed"),
            Choice("ask_permission", "Можно остаться?", "zara_permission")
        ]
    ))

    zara_night_talk.add_node(DialogueNode(
        id="zara_intimate",
        speaker="Зара",
        text="*закрывает глаза* Я не... *перебивает себя* "
             "К чёрту. *делает шаг ближе* "
             "Давно хотела сделать это. *целует*",
        is_end=True
    ))

    zara_night_talk.add_node(DialogueNode(
        id="zara_romantic",
        speaker="Зара",
        text="*смотрит в глаза* Я тоже. Чувствую. "
             "*тихо* Знаешь, я начала думать... может, после этой миссии... "
             "*не договаривает, но смотрит с надеждой*",
        is_end=True
    ))

    dialogues["zara_night_talk"] = zara_night_talk

    # === Боевая сцена: защита Макса ===
    zara_combat_protection = Dialogue(
        id="zara_combat_protection",
        title="Зара защищает Макса",
        start_node="start"
    )

    zara_combat_protection.add_node(DialogueNode(
        id="start",
        speaker="Зара",
        text="*закрывает вас собой от выстрела. Пуля царапает плечо* "
             "Чёрт! *в ответ стреляет и попадает* "
             "Макс, за мной! Я выведу нас!",
        choices=[
            Choice("thank_combat", "Спасибо! Двигаемся!", "zara_combat_continue"),
            Choice("worry_wound", "Ты ранена!", "zara_dismiss_wound"),
            Choice("cover_her", "Прикрою тебя!", "zara_surprised_cover",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("zara", 10))
        ]
    ))

    zara_combat_protection.add_node(DialogueNode(
        id="zara_dismiss_wound",
        speaker="Зара",
        text="Царапина! Я видела worse. *перезаряжает* "
             "Фокус на миссии. Моя работа — вытащить вас живым. "
             "И я выполняю контракты. Всегда.",
        choices=[
            Choice("acknowledge", "Понял. За тобой", "zara_combat_continue"),
            Choice("promise", "После боя — медицинский отсек", "zara_small_smile")
        ]
    ))

    zara_combat_protection.add_node(DialogueNode(
        id="zara_surprised_cover",
        speaker="Зара",
        text="*сюрприз на лице* Вы... прикрываете наёмника? "
             "*редкая улыбка* Я привыкла защищать других. "
             "Но... спасибо. Работаем вместе?",
        is_end=True
    ))

    zara_combat_protection.add_node(DialogueNode(
        id="zara_small_smile",
        speaker="Зара",
        text="*лёгкая улыбка* Заботитесь о сотруднике? Это... непрофессионально. "
             "*с мягкостью* Но мне нравится. Движемся!",
        is_end=True
    ))

    dialogues["zara_combat_protection"] = zara_combat_protection

    return dialogues


def create_marcus_reed_dialogues() -> Dict[str, Dialogue]:
    """Диалоги для Маркуса Рида — наёмника (мужчина, без романтики)"""
    dialogues = {}

    marcus_meeting = Dialogue(
        id="marcus_meeting",
        title="Встреча с Маркусом Ридом",
        start_node="start"
    )

    marcus_meeting.add_node(DialogueNode(
        id="start",
        speaker="Маркус Рид",
        text="*дружелюбно машет* Капитан Велл! Слышал, вы ищете людей. "
             "Маркус Рид, к вашим услугам. Бывший военный, специализация — "
             "тактика и тяжёлое вооружение. И, между нами, я делаю "
             "лучший кофе в галактике.",
        choices=[
            Choice("ask_experience", "Какой опыт?", "marcus_experience"),
            Choice("ask_price_marcus", "Какова цена?", "marcus_price"),
            Choice("joke_coffee", "Кофе — решающий фактор", "marcus_laugh",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("marcus_reed", 5))
        ]
    ))

    marcus_meeting.add_node(DialogueNode(
        id="marcus_experience",
        speaker="Маркус Рид",
        text="Пятнадцать лет в морпехах Альянса. Три года наёмником. "
             "Участвовал в операциях, о которых не могу говорить — "
             "и в нескольких, о которых можете прочитать в новостях. "
             "Моя репутация: я не бросаю команду и не предаю нанимателей.",
        choices=[
            Choice("hire_marcus", "Вы приняты", "marcus_hired"),
            Choice("ask_references", "Есть рекомендации?", "marcus_references"),
            Choice("test_marcus", "Покажите навыки", "marcus_test")
        ]
    ))

    marcus_meeting.add_node(DialogueNode(
        id="marcus_price",
        speaker="Маркус Рид",
        text="3000 за миссию. Не самый дешёвый, но и не самый дорогой. "
             "Зато вы получаете кого-то, кто не сбежит при первых признаках "
             "опасности. *серьёзно* Я видел достаточно, чтобы знать — "
             "надёжность стоит дороже любой суммы.",
        choices=[
            Choice("accept_price", "Справедливая цена", "marcus_hired",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("marcus_reed", 3)),
            Choice("negotiate_marcus", "Можно обсудить?", "marcus_negotiate")
        ]
    ))

    marcus_meeting.add_node(DialogueNode(
        id="marcus_laugh",
        speaker="Маркус Рид",
        text="*смеётся* Наконец-то капитан с приоритетами! "
             "Шучу. Но серьёзно — если работа будет, я в деле. "
             "Команда с чувством юмора — уже полдела.",
        is_end=True
    ))

    marcus_meeting.add_node(DialogueNode(
        id="marcus_hired",
        speaker="Маркус Рид",
        text="*серьёзно кивает* Спасибо за доверие. "
             "Не подведу. И, между прочим, у меня есть информация "
             "о вашем... «сопровождении». Охотники за головами. "
             "Рейнер и Кира. Они на вас охотятся.",
        is_end=True
    ))

    dialogues["marcus_meeting"] = marcus_meeting

    # === Разговор о кодексе ===
    marcus_code = Dialogue(
        id="marcus_code",
        title="Кодекс Маркуса",
        start_node="start"
    )

    marcus_code.add_node(DialogueNode(
        id="start",
        speaker="Макс",
        text="Маркус, вы упомянули кодекс. Что это значит для вас?",
        choices=[
            Choice("ask_code", "Объясните подробнее", "marcus_explain")
        ]
    ))

    marcus_code.add_node(DialogueNode(
        id="marcus_explain",
        speaker="Маркус Рид",
        text="*задумчиво* Простой кодекс. Защищаю тех, кто не может защититься сам. "
             "Не стреляю в спину. Не бросаю раненых. И никогда — слышите, никогда — "
             "не работаю на тех, кто убивает гражданских. "
             "Мог бы сказать «честь», но это звучит пафосно. "
             "Скорее... способ сохранить себя.",
        choices=[
            Choice("respect_code", "Это достойно уважения", "marcus_respect",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("marcus_reed", 8)),
            Choice("ask_history", "Как вы пришли к этому?", "marcus_history"),
            Choice("test_alignment", "Что, если миссия нарушит кодекс?", "marcus_dilemma")
        ]
    ))

    marcus_code.add_node(DialogueNode(
        id="marcus_history",
        speaker="Маркус Рид",
        text="*тяжело вздыхает* Давно... мой командир приказал расстрелять деревню. "
             "Сказал — там повстанцы. Там были женщины и дети. "
             "Я отказался. Он угрожал трибуналом. Я ушёл. "
             "С тех пор — независимый. *смотрит в глаза* "
             "Если ваша миссия потребует чего-то подобного — я уйду. Без обид.",
        choices=[
            Choice("promise_alignment", "Моя миссия не требует невинных жертв", "marcus_aligned",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("marcus_reed", 10)),
            Choice("understand", "Понимаю и уважаю", "marcus_understood")
        ]
    ))

    marcus_code.add_node(DialogueNode(
        id="marcus_aligned",
        speaker="Маркус Рид",
        text="*кивает с облегчением* Хорошо. Тогда мы сработаемся. "
             "И, Макс... спасибо, что не спросили, выполнил ли я тот приказ. "
             "Это важно.",
        is_end=True
    ))

    dialogues["marcus_code"] = marcus_code

    return dialogues


def create_reiner_kira_dialogues() -> Dict[str, Dialogue]:
    """Диалоги для Рейнера и Киры — охотников за головами (антагонисты)"""
    dialogues = {}

    hunter_meeting = Dialogue(
        id="hunter_meeting",
        title="Охотники за головами",
        start_node="start"
    )

    hunter_meeting.add_node(DialogueNode(
        id="start",
        speaker="Кира",
        text="*выходит из тени с улыбкой* Капитан Макс Велл! "
             "Наконец-то. Моё имя Кира, а этот угрюмый тип — Рейнер. "
             "*Рейнер молча кивает* "
             "У нас к вам деловое предложение. Вернее, требование.",
        choices=[
            Choice("ask_business", "Какое предложение?", "kira_offer"),
            Choice("refuse_talk", "Мне неинтересно", "kira_threat"),
            Choice("ask_bounty", "Кто вас нанял?", "kira_client")
        ]
    ))

    hunter_meeting.add_node(DialogueNode(
        id="kira_offer",
        speaker="Кира",
        text="Простое. Вы сдаётесь нам. Мы получаем награду за вашу голову. "
             "200000 кредитов за живого, 150000 за мёртвого. "
             "Предпочтём живого — это дороже. "
             "*смеётся* Выбор за вами, капитан.",
        choices=[
            Choice("negotiate_hunters", "Могу предложить больше", "kira_interested"),
            Choice("fight_hunters", "Попробуйте взять", "kira_fight"),
            Choice("ask_time", "Дайте время подумать", "kira_time")
        ]
    ))

    hunter_meeting.add_node(DialogueNode(
        id="kira_client",
        speaker="Кира",
        text="*хитро улыбается* О, профессиональный интерес? "
             "Скажем так... наш клиент очень хочет заполучить то, "
             "что у вас есть. Артефакты. Ключи. Или вас лично. "
             "Детали не наше дело — мы просто доставляем.",
        choices=[
            Choice("guess_client", "Волков?", "kira_surprise"),
            Choice("ask_more_info", "Могу заплатить за информацию", "kira_consider"),
            Choice("ignore_client", "Не важно. Я не сдамся", "kira_shrug")
        ]
    ))

    hunter_meeting.add_node(DialogueNode(
        id="kira_surprise",
        speaker="Кира",
        text="*вздымаает бровь* Вы умнее, чем кажетесь. Да, Волков. "
             "Он очень настойчив. И очень хорошо платит. "
             "Но знаете что? Он не единственный, кто может платить. "
             "*многозначительно смотрит*",
        choices=[
            Choice("offer_counter", "Предлагаю сделку", "kira_deal"),
            Choice("refuse_bribe", "Не торгуюсь с охотниками", "kira_disappointed")
        ]
    ))

    hunter_meeting.add_node(DialogueNode(
        id="kira_deal",
        speaker="Кира",
        text="*смотрит на Рейнера. Тот едва заметно кивает* "
             "Интересно. 250000, и мы забываем о контракте. "
             "Плюс — информация о других охотниках на вашей тропе. "
             "Вы не единственные, кого нанял Волков.",
        choices=[
            Choice("accept_deal", "Принимаю", "kira_hired",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("reiner_kira", 20)),
            Choice("refuse_deal", "Слишком дорого", "kira_fight"),
            Choice("ask_guarantee", "Как я могу вам доверять?", "kira_guarantee")
        ]
    ))

    hunter_meeting.add_node(DialogueNode(
        id="kira_guarantee",
        speaker="Рейнер",
        text="*впервые говорит* Мы не нарушаем слова. Это плохой бизнес. "
             "*Кира кивает* Контракт с Волковым был на «доставку». "
             "Новый контракт с вами — на «защиту». "
             "Разные контракты. Никакого нарушения.",
        is_end=True
    ))

    hunter_meeting.add_node(DialogueNode(
        id="kira_fight",
        speaker="Кира",
        text="*вздыхает* Жаль. Мне вы нравились. "
             "*достаёт оружие* Рейнер, левый фланг. Я — правый. "
             "Попробуем взять живым. Если получится.",
        is_end=True
    ))

    hunter_meeting.add_node(DialogueNode(
        id="kira_hired",
        speaker="Кира",
        text="*улыбается* Отличный выбор. Рейнер, отмена контракта с Волковым. "
             "У нас новый клиент. *поворачивается к вам* "
             "Добро пожаловать в команду... хотя это странно звучит.",
        is_end=True
    ))

    dialogues["hunter_meeting"] = hunter_meeting

    return dialogues


def create_volkov_criminal_dialogues() -> Dict[str, Dialogue]:
    """Диалоги для Волкова (криминального авторитета) — главного антагониста 2 акта"""
    dialogues = {}

    volkov_meeting = Dialogue(
        id="volkov_criminal_meeting",
        title="Встреча с Волковым",
        start_node="start"
    )

    volkov_meeting.add_node(DialogueNode(
        id="start",
        speaker="Волков",
        text="*сидит в кресле, спиной к двери. Не оборачивается* "
             "Капитан Велл. Прошу, садитесь. *указывает на кресло напротив* "
             "У меня есть предложение, от которого вы не откажетесь. "
             "Но сначала — напиток? Коньяк 2387 года. Редкий.",
        choices=[
            Choice("accept_drink", "Принять напиток", "volkov_drink_accepted"),
            Choice("refuse_drink", "Нет, спасибо", "volkov_no_drink"),
            Choice("get_to_point", "К делу", "volkov_direct")
        ]
    ))

    volkov_meeting.add_node(DialogueNode(
        id="volkov_direct",
        speaker="Волков",
        text="*наконец поворачивается. Лицо в шрамах, глаза ледяные* "
             "Прямолинейность. Ценю. Хорошо. "
             "У вас есть ключи Хранителей. Мне они нужны. "
             "Но я не заберу их силой — предлагаю союз.",
        choices=[
            Choice("ask_why_keys", "Зачем они вам?", "volkov_explanation"),
            Choice("ask_alliance", "Какой союз?", "volkov_proposal"),
            Choice("refuse_alliance", "Я не работаю на криминал", "volkov_threat")
        ]
    ))

    volkov_meeting.add_node(DialogueNode(
        id="volkov_explanation",
        speaker="Волков",
        text="*улыбается без тепла* Потому что я знаю, что такое Сущность. "
             "Я видел её. *пауза* Я был частью проекта «Эхо». "
             "Не как учёный — как спонсор. И я видел, что вышло из портала. "
             "Сущность — не просто угроза. Это... возможность.",
        choices=[
            Choice("ask_opportunity", "Что за возможность?", "volkov_reveal"),
            Choice("ask_portal", "Что вы видели?", "volkov_portal_memory"),
            Choice("accuse_volkov", "Вы создали эту угрозу", "volkov_dismissive")
        ]
    ))

    volkov_meeting.add_node(DialogueNode(
        id="volkov_reveal",
        speaker="Волков",
        text="Сущность может открывать двери. Между мирами, между реальностями. "
             "Семь ключей под контролем одного носителя — "
             "и вы станете богом. Или уничтожите всё. "
             "Я предпочитаю первый вариант. С моим... руководством.",
        choices=[
            Choice="consider", "Почему я?", "volkov_why_you"),
            Choice("reject_power", "Я не хочу такой силы", "volkov_pity"),
            Choice("counter_proposal", "У меня свои планы", "volkov_interested")
        ]
    ))

    volkov_meeting.add_node(DialogueNode(
        id="volkov_why_you",
        speaker="Волков",
        text="Потому что вы — капитан «Элеи». Корабль, созданный Хранителями. "
             "И у вас уже есть команда с потенциалом. "
             "*поднимается* Я могу дать ресурсы, информацию, защиту. "
             "В обмен — когда наступит момент, вы прислушаетесь к моему совету. "
             "Один совет. Один раз. Разве не честно?",
        choices=[
            Choice("accept_alliance", "Принимаю", "volkov_alliance_accepted"),
            Choice("refuse_alliance", "Отказываюсь", "volkov_war"),
            Choice("ask_time", "Мне нужно время", "volkov_deadline")
        ]
    ))

    volkov_meeting.add_node(DialogueNode(
        id="volkov_alliance_accepted",
        speaker="Волков",
        text="*улыбается искренне* Мудрый выбор. "
             "Мои ресурсы — ваши. Информация о других ключах — ваша. "
             "Защита от Альянса и пиратов — ваша. "
             "*серьёзно* Но помните: когда придёт время, "
             "я попрошу об одном. И вы не откажете.",
        is_end=True
    ))

    volkov_meeting.add_node(DialogueNode(
        id="volkov_war",
        speaker="Волков",
        text="*лицо каменеет* Жаль. Я надеялся на разумное решение. "
             "*нажимает кнопку* Теперь вы — враг. "
             "Мои люди будут охотиться на вас везде. "
             "Мои деньги будут течь к вашим врагам. "
             "*тихо* Не говорите, что я не предупреждал.",
        is_end=True
    ))

    volkov_meeting.add_node(DialogueNode(
        id="volkov_threat",
        speaker="Волков",
        text="*холодно* «Криминал». Интересное слово. "
             "Корпорации убивают миллионы ради прибыли — это «бизнес». "
             "Правительства уничтожают планеты — это «политика». "
             "А я — криминал? *встаёт* "
             "Я предлагаю спасение. Вы отказываетесь из гордости. "
             "Напомните мне, сколько людей умрёт из-за вашей морали?",
        is_end=True
    ))

    dialogues["volkov_criminal_meeting"] = volkov_meeting

    # === Финальная конфронтация ===
    volkov_final = Dialogue(
        id="volkov_final_confrontation",
        title="Финальная битва с Волковым",
        start_node="start"
    )

    volkov_final.add_node(DialogueNode(
        id="start",
        speaker="Волков",
        text="*окружён охраной, но спокоен* "
             "Вы дошли до конца, Велл. Впечатляет. "
             "Но вы не понимаете, с чем играете. "
             "Ключи — это не оружие. Это дверь. "
             "И она уже приоткрыта.",
        choices=[
            Choice("fight_volkov", "Бой!", "volkov_combat"),
            Choice("talk_volkov", "Ещё не поздно остановиться", "volkov_last_chance"),
            Choice("surrender_volkov", "Что вы хотите?", "volkov_final_demand")
        ]
    ))

    volkov_final.add_node(DialogueNode(
        id="volkov_last_chance",
        speaker="Волков",
        text="*смеётся* Остановиться? После всего? "
             "Я потратил тридцать лет на этот момент. "
             "Видел, как друзья сходили с ума от контакта с Сущностью. "
             "Потерял семью ради ключей. "
             "Нет, Велл. Я не остановлюсь. "
             "Вопрос в том — вы со мной или против меня?",
        choices=[
            Choice("join_final", "С вами", "volkov_together"),
            Choice("fight_to_end", "Против", "volkov_combat"),
            Choice("offer_alternative", "Есть третий путь", "volkov_alternative")
        ]
    ))

    volkov_final.add_node(DialogueNode(
        id="volkov_together",
        speaker="Волков",
        text="*кивает с уважением* Вы умнее, чем я думал. "
             "Вместе мы откроем дверь. И галактика изменится навсегда. "
             "*протягивает руку* Договор?",
        is_end=True
    ))

    volkov_final.add_node(DialogueNode(
        id="volkov_combat",
        speaker="Волков",
        text="*достаёт оружие* Тогда посмотрим, насколько вы хороши. "
             "Мои люди — лучшие. Я — лучше их. "
             "*ухмыляется* Докажите, что заслуживаете ключи.",
        is_end=True
    ))

    volkov_final.add_node(DialogueNode(
        id="volkov_alternative",
        speaker="Волков",
        text="*заинтересован* Третий путь? Говорите. "
             "Я слушаю. Но предупреждаю — "
             "если ваше предложение глупое, это будет ваш последний разговор.",
        choices=[
            Choice("propose_seal", "Запечатать дверь навсегда", "volkov_refuses"),
            Choice("propose_control", "Контроль без вас", "volkov_angry"),
            Choice("propose_negotiate", "Найти компромисс", "volkov_listens")
        ]
    ))

    volkov_final.add_node(DialogueNode(
        id="volkov_listens",
        speaker="Волков",
        text="*садится* Компромисс. *задумывается* "
             "Что вы предлагаете?",
        is_end=True
    ))

    dialogues["volkov_final_confrontation"] = volkov_final

    return dialogues


def create_all_new_character_dialogues() -> Dict[str, Dialogue]:
    """Создать все диалоги для новых персонажей"""
    all_dialogues = {}
    all_dialogues.update(create_zara_dialogues())
    all_dialogues.update(create_marcus_reed_dialogues())
    all_dialogues.update(create_reiner_kira_dialogues())
    all_dialogues.update(create_volkov_criminal_dialogues())
    return all_dialogues
