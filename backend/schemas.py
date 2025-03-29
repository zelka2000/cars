from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class TeamBase(BaseModel):
    """Базовая модель команды"""
    name: str  # Название команды


class Team(TeamBase):
    """Полная модель команды с ID"""
    id: int  # Уникальный идентификатор команды

    class Config:
        from_attributes = True  # Позволяет создавать объекты из ORM моделей


class DriverBase(BaseModel):
    """Базовая модель гонщика"""
    name: str  # Имя гонщика
    points: int = 0  # Количество очков (по умолчанию 0)


class Driver(DriverBase):
    """Полная модель гонщика с ID и связью с командой"""
    id: int  # Уникальный идентификатор гонщика
    team_id: int  # ID команды, в которой выступает гонщик
    team: Team  # Связь с командой

    class Config:
        from_attributes = True


class TeamWithDrivers(Team):
    """Расширенная модель команды со списком гонщиков"""
    drivers: List[DriverBase] = []  # Список гонщиков команды

    class Config:
        from_attributes = True


class RaceBase(BaseModel):
    """Базовая модель гонки"""
    name: str  # Название гонки
    date: date  # Дата проведения
    location: str  # Место проведения


class Race(RaceBase):
    """Полная модель гонки с ID"""
    id: int  # Уникальный идентификатор гонки

    class Config:
        from_attributes = True