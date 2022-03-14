from dataclasses import dataclass
from decimal import Decimal

from uuid import uuid4

users = {}
questions = {}
contests = {}
participants = {}


@dataclass
class User:
    user_name: str


@dataclass
class Question:
    pk: str
    difficulty: str
    value: str


@dataclass
class Contest:
    pk: str
    name: str
    level: str
    creator_user_name: str
    is_live: bool = False


@dataclass
class ContestQuestion:
    pk: str
    contest_id: str
    question_id: str


@dataclass
class Participant:
    pk: str
    user_name: str
    score: Decimal
    contest_id: str
    created_at: str # timestamp
    completed_at: str # timestamp
    is_completed: bool


@dataclass
class ParticipantAnswer:
    pk: str
    question_id: str
    participant_id: str
    answer: str
    created_at: str  # timestamp
    status: bool


def create_user(user_name):
    return User(user_name=user_name)


def create_question(difficulty):
    return Question(difficulty=difficulty, pk=uuid4[:6])


def create_contest(name, level, user_name):
    user = users.get(user_name)

    if user:
        return Contest(
            pk=uuid4[:6], name=name, level=level, creator_user_name=user_name
        )


def list_contests(level):
    result = [
        contest for contest in contests.values() if contest.level == level
    ]
    return result


def create_participant(contest_id, user_name):
    return Participant(
        pk=f"{user_name}_{contest_id}",
        user_name=user_name,
        contest_id=contest_id,
        score=Decimal(0)
    )


def attend_contest(contest_id, user_name):
    user = users.get(user_name)
    contest = contests.get(contest_id)

    if not user or not contest:
        return

    key = f"{user_name}_{contest_id}"

    participant = participants.get(key)

    if participant:
        return True


def run_contest(contest_id, user_name):
    user = users.get(user_name)
    contest = contests.get(contest_id)

    if user and contest and user.user_name == user_name:
        contest.is_live = True


def contest_history(contest_id):
    contest = contests.get(contest_id)

    _participants = [
        for participant in participants
    ]
