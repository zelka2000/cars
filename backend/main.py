# 
# Этот файл является главным файлом нашего бэкенда (серверной части приложения).
# Здесь мы создаем API (интерфейс для взаимодействия с данными) и настраиваем базу данных.
#

# Импортируем необходимые библиотеки
from fastapi import FastAPI, Depends, HTTPException  # FastAPI - фреймворк для создания API
from fastapi.middleware.cors import CORSMiddleware   # Для настройки CORS (доступа с фронтенда)
from sqlalchemy.orm import Session                  # Для работы с базой данных
from typing import List                            # Для типизации данных
import models, database                            # Наши локальные модули
from datetime import date                          # Для работы с датами
from pydantic import BaseModel                     # Для валидации данных
import logging                                     # Для логирования (записи действий)

# Настраиваем систему логирования
# Это поможет нам отслеживать, что происходит в приложении
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Настраиваем CORS (Cross-Origin Resource Sharing)
# Это позволяет нашему фронтенду (работающему на порту 8080) 
# обращаться к бэкенду (работающему на порту 8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Разрешаем запросы только с нашего фронтенда
    allow_credentials=True,                   # Разрешаем передачу учетных данных
    allow_methods=["*"],                      # Разрешаем все HTTP методы (GET, POST, PUT, DELETE)
    allow_headers=["*"],                      # Разрешаем все заголовки
)

# Создаем таблицы в базе данных
# Это создаст все необходимые таблицы, если они еще не существуют
models.Base.metadata.create_all(bind=database.engine)

# Определяем модели данных для API
# Эти классы описывают структуру данных, которые мы будем получать и отправлять

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

# API для получения данных
# Эти эндпоинты позволяют получать данные из базы данных

@app.get("/teams/", response_model=List[TeamWithDrivers])
def get_teams(db: Session = Depends(database.get_db)):
    """
    Получаем список всех команд с их гонщиками
    - response_model указывает, что мы возвращаем список команд с гонщиками
    - db: Session = Depends(database.get_db) получает подключение к базе данных
    """
    try:
        # Получаем все команды из базы данных
        teams = db.query(models.Team).all()
        logger.info(f"Получено {len(teams)} команд")
        return teams
    except Exception as e:
        # Если произошла ошибка, логируем её и возвращаем ошибку клиенту
        logger.error(f"Ошибка при получении команд: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/drivers/", response_model=List[Driver])
def get_drivers(db: Session = Depends(database.get_db)):
    """
    Получаем список всех гонщиков
    - response_model указывает, что мы возвращаем список гонщиков
    """
    try:
        drivers = db.query(models.Driver).all()
        logger.info(f"Получено {len(drivers)} гонщиков")
        return drivers
    except Exception as e:
        logger.error(f"Ошибка при получении гонщиков: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/races/", response_model=List[Race])
def get_races(db: Session = Depends(database.get_db)):
    """
    Получаем список всех гонок
    - response_model указывает, что мы возвращаем список гонок
    """
    try:
        races = db.query(models.Race).all()
        logger.info(f"Получено {len(races)} гонок")
        return races
    except Exception as e:
        logger.error(f"Ошибка при получении гонок: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# Функция для инициализации тестовых данных при первом запуске
@app.on_event("startup")
async def startup_event():
    """
    Эта функция запускается при старте приложения
    - Проверяет, есть ли данные в базе
    - Если база пуста, добавляет тестовые данные
    - Создает команды, гонщиков и гонки
    """
    try:
        # Получаем подключение к базе данных
        db = next(database.get_db())
        
        # Проверяем, есть ли данные в базе
        if db.query(models.Team).count() == 0:
            # Создаем список тестовых команд
            teams = [
                models.Team(name="Red Bull Racing"),
                models.Team(name="Mercedes"),
                models.Team(name="Ferrari"),
                models.Team(name="McLaren"),
                models.Team(name="Aston Martin")
            ]
            
            # Добавляем команды в базу
            for team in teams:
                db.add(team)
                logger.info(f"Добавлена команда: {team.name}")
            
            # Создаем список тестовых гонщиков
            drivers = [
                models.Driver(name="Max Verstappen", team_id=1, points=25),
                models.Driver(name="Lewis Hamilton", team_id=2, points=18),
                models.Driver(name="Charles Leclerc", team_id=3, points=15),
                models.Driver(name="Lando Norris", team_id=4, points=12),
                models.Driver(name="Sebastian Vettel", team_id=5, points=10)
            ]
            
            # Добавляем гонщиков в базу
            for driver in drivers:
                db.add(driver)
                logger.info(f"Добавлен гонщик: {driver.name}")
            
            # Создаем список тестовых гонок
            races = [
                models.Race(name="Australian Grand Prix", date=date(2024, 3, 24), location="Melbourne"),
                models.Race(name="Monaco Grand Prix", date=date(2024, 5, 26), location="Monte Carlo"),
                models.Race(name="British Grand Prix", date=date(2024, 7, 7), location="Silverstone"),
                models.Race(name="Belgian Grand Prix", date=date(2024, 8, 25), location="Spa"),
                models.Race(name="Italian Grand Prix", date=date(2024, 9, 8), location="Monza")
            ]
            
            # Добавляем гонки в базу
            for race in races:
                db.add(race)
                logger.info(f"Добавлена гонка: {race.name}")
            
            # Сохраняем все изменения в базе
            try:
                db.commit()
                logger.info("Данные успешно добавлены")
            except Exception as e:
                # Если произошла ошибка, отменяем все изменения
                db.rollback()
                logger.error(f"Ошибка при добавлении данных: {str(e)}")
                raise
        else:
            logger.info("Данные уже есть в базе")
    except Exception as e:
        logger.error(f"Ошибка при инициализации: {str(e)}")
        raise 