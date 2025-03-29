# 
# Этот файл содержит определения моделей данных для базы данных.
# Модели описывают структуру таблиц и связи между ними.
#

# Импортируем необходимые компоненты из SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Date  # Типы данных для колонок
from sqlalchemy.orm import relationship  # Для создания связей между таблицами
from database import Base  # Базовый класс для моделей

class Team(Base):
    """
    Модель команды.
    Описывает таблицу команд в базе данных.
    """
    # Указываем имя таблицы в базе данных
    __tablename__ = "teams"

    # Определяем колонки таблицы
    id = Column(Integer, primary_key=True, index=True)  # Уникальный идентификатор команды
    name = Column(String, index=True)  # Название команды

    # Создаем связь с таблицей гонщиков
    # back_populates указывает на обратную связь в модели Driver
    drivers = relationship("Driver", back_populates="team")

class Driver(Base):
    """
    Модель гонщика.
    Описывает таблицу гонщиков в базе данных.
    """
    __tablename__ = "drivers"

    # Определяем колонки таблицы
    id = Column(Integer, primary_key=True, index=True)  # Уникальный идентификатор гонщика
    name = Column(String, index=True)  # Имя гонщика
    points = Column(Integer, default=0)  # Количество очков (по умолчанию 0)
    
    # Внешний ключ для связи с таблицей команд
    # ForeignKey указывает на колонку id в таблице teams
    team_id = Column(Integer, ForeignKey("teams.id"))
    
    # Создаем связь с таблицей команд
    # back_populates указывает на обратную связь в модели Team
    team = relationship("Team", back_populates="drivers")

class Race(Base):
    """
    Модель гонки.
    Описывает таблицу гонок в базе данных.
    """
    __tablename__ = "races"

    # Определяем колонки таблицы
    id = Column(Integer, primary_key=True, index=True)  # Уникальный идентификатор гонки
    name = Column(String, index=True)  # Название гонки
    date = Column(Date)  # Дата проведения гонки
    location = Column(String)  # Место проведения гонки 