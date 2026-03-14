# -*- coding: utf-8 -*-
"""
Star Courier - Quests for Chapters 11-12 (Quest Class Format)
Интеграция с существующей системой quests.py
"""

from typing import Dict
from .quests import Quest, QuestType, QuestState, QuestReward, Objective, ObjectiveType


def create_chapter11_quests() -> Dict[str, Quest]:
    """Создать квесты главы 11"""
    quests = {}
    
    q11_01 = Quest(
        id="q11_01",
        title="Пробуждение Эха",
        description="Кристалл из Координаты Нуля начал резонировать. Голос из прошлого пытается установить контакт.",
        quest_type=QuestType.MAIN,
        state=QuestState.AVAILABLE,
        giver="Эхо",
        journal_entry="Древний ИИ Хранителей пытается связаться с вами.",
        prerequisites=["main_002"]
    )
    q11_01.add_objective(Objective(
        id="obj_contact",
        type=ObjectiveType.TALK,
        description="Установите контакт с Эхом",
        target_id="echo_first_contact",
        required=1,
        is_completed=False
    ))
    q11_01.reward = QuestReward(experience=500, credits=200)
    quests["q11_01"] = q11_01
    
    q11_02 = Quest(
        id="q11_02",
        title="След выжившего",
        description="Эхо упомянуло кого-то, кто вернулся из Зоны Тишины.",
        quest_type=QuestType.SIDE,
        state=QuestState.AVAILABLE,
        giver="Эхо",
        prerequisites=["q11_01"]
    )
    q11_02.add_objective(Objective(
        id="obj_witness",
        type=ObjectiveType.TALK,
        description="Найдите свидетеля",
        target_id="old_sailor",
        required=1,
        is_completed=False
    ))
    q11_02.reward = QuestReward(experience=300, credits=150)
    quests["q11_02"] = q11_02
    
    return quests


def create_chapter12_quests() -> Dict[str, Quest]:
    """Создать квесты главы 12"""
    quests = {}
    
    q12_01 = Quest(
        id="q12_01",
        title="Станция Горизонт",
        description="Последняя известная локация экспедиции Альянса.",
        quest_type=QuestType.MAIN,
        state=QuestState.AVAILABLE,
        giver="Альянс",
        prerequisites=["q11_01"]
    )
    q12_01.add_objective(Objective(
        id="obj_dock",
        type=ObjectiveType.EXPLORE,
        description="Пристыковать к станции",
        target_id="horizon_station",
        required=1,
        is_completed=False
    ))
    q12_01.reward = QuestReward(experience=400, credits=300)
    quests["q12_01"] = q12_01
    
    return quests


def create_all_chapter11_12_quests() -> Dict[str, Quest]:
    """Создать все квесты для глав 11-12"""
    all_quests = {}
    all_quests.update(create_chapter11_quests())
    all_quests.update(create_chapter12_quests())
    return all_quests
