# Инструкция по созданию проекта F1 Racing

## Содержание
1. [Подготовка окружения](#подготовка-окружения)
2. [Создание структуры проекта](#создание-структуры-проекта)
3. [Настройка бэкенда](#настройка-бэкенда)
4. [Настройка фронтенда](#настройка-фронтенда)
5. [Запуск проекта](#запуск-проекта)
6. [Структура базы данных](#структура-базы-данных)
7. [API эндпоинты](#api-эндпоинты)
8. [Компоненты фронтенда](#компоненты-фронтенда)

## Пошаговое руководство по созданию приложения

### 1. Планирование проекта
1. Определите цель проекта - создание веб-приложения для отображения информации о гонках Формулы 1
2. Определите основные функции:
   - Просмотр списка команд и их гонщиков
   - Просмотр календаря гонок
   - Просмотр очков гонщиков
3. Определите структуру данных:
   - Команды (название)
   - Гонщики (имя, очки, связь с командой)
   - Гонки (название, дата, место проведения)

### 2. Подготовка окружения
1. Установите необходимые инструменты:
   - Python для бэкенда
   - Node.js и npm для фронтенда
2. Создайте виртуальное окружение Python
3. Создайте структуру директорий проекта

### 3. Разработка бэкенда
1. Настройка базы данных:
   - Создайте файл database.py для настройки подключения к SQLite
   - Настройте SQLAlchemy для работы с базой данных
   - Создайте функцию для получения сессии базы данных

2. Создание моделей данных:
   - Определите модели Team, Driver и Race
   - Настройте связи между моделями
   - Добавьте необходимые поля и их типы

3. Создание API:
   - Настройте FastAPI приложение
   - Добавьте CORS для работы с фронтендом
   - Создайте GET-эндпоинты для получения данных
   - Добавьте функцию инициализации тестовых данных

### 4. Разработка фронтенда
1. Создание проекта Vue.js:
   - Инициализируйте новый проект Vue
   - Настройте Vue Router для навигации
   - Установите необходимые зависимости (Element Plus, Axios)

2. Создание компонентов:
   - TeamList.vue для отображения команд и гонщиков
   - RaceCalendar.vue для отображения календаря гонок
   - DriverPoints.vue для отображения очков гонщиков
   - App.vue для общего макета приложения

3. Настройка маршрутизации:
   - Определите маршруты для каждого компонента
   - Настройте навигацию между страницами

4. Стилизация:
   - Добавьте базовые стили
   - Настройте компоненты Element Plus
   - Сделайте интерфейс привлекательным и удобным

### 5. Интеграция фронтенда и бэкенда
1. Настройка API-запросов:
   - Используйте Axios для отправки запросов к бэкенду
   - Обработайте возможные ошибки
   - Добавьте индикаторы загрузки

2. Тестирование взаимодействия:
   - Проверьте получение данных
   - Убедитесь в корректной работе маршрутизации
   - Проверьте отображение данных в компонентах

### 6. Запуск и тестирование
1. Запуск бэкенда:
   - Активируйте виртуальное окружение
   - Запустите сервер FastAPI
   - Проверьте работу API-эндпоинтов

2. Запуск фронтенда:
   - Установите зависимости
   - Запустите сервер разработки
   - Откройте приложение в браузере

3. Тестирование:
   - Проверьте все функции приложения
   - Убедитесь в корректном отображении данных
   - Проверьте работу навигации

### 7. Возможные улучшения
1. Функциональные улучшения:
   - Добавление аутентификации
   - Реализация редактирования данных
   - Добавление поиска и фильтрации
   - Реализация сортировки таблиц

2. Технические улучшения:
   - Добавление кэширования
   - Оптимизация производительности
   - Добавление тестов
   - Улучшение обработки ошибок

3. UI/UX улучшения:
   - Добавление анимаций
   - Улучшение дизайна
   - Добавление адаптивности
   - Улучшение пользовательского опыта

### 8. Рекомендации по разработке
1. Используйте систему контроля версий (Git)
2. Следуйте принципам чистого кода
3. Добавляйте комментарии к сложным участкам кода
4. Регулярно тестируйте изменения
5. Документируйте код и API
6. Следите за безопасностью приложения
7. Оптимизируйте производительность
8. Учитывайте масштабируемость при разработке

## Подготовка окружения

### Установка необходимых инструментов
1. Установите Python (версия 3.8 или выше)
2. Установите Node.js (версия 14 или выше)
3. Установите npm (обычно идет вместе с Node.js)

### Создание виртуального окружения для Python
```bash
# Создаем директорию проекта
mkdir f1_racing
cd f1_racing

# Создаем виртуальное окружение
python -m venv venv

# Активируем виртуальное окружение
# Для Windows:
venv\Scripts\activate
# Для macOS/Linux:
source venv/bin/activate
```

## Создание структуры проекта

### Структура директорий
```
f1_racing/
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   └── requirements.txt
└── frontend/
    ├── src/
    │   ├── components/
    │   │   ├── TeamList.vue
    │   │   ├── RaceCalendar.vue
    │   │   └── DriverPoints.vue
    │   ├── App.vue
    │   └── main.js
    └── package.json
```

## Настройка бэкенда

### Установка зависимостей
```bash
cd backend
pip install fastapi uvicorn sqlalchemy pydantic
```

### Создание файлов бэкенда

1. **database.py** - настройка подключения к базе данных:
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./f1.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

2. **models.py** - определение моделей данных:
```python
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from database import Base

class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    drivers = relationship("Driver", back_populates="team")

class Driver(Base):
    __tablename__ = "drivers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    points = Column(Integer, default=0)
    team_id = Column(Integer, ForeignKey("teams.id"))
    team = relationship("Team", back_populates="drivers")

class Race(Base):
    __tablename__ = "races"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    date = Column(Date)
    location = Column(String)
```

3. **main.py** - создание API:
```python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import models, database
from datetime import date
from pydantic import BaseModel
import logging

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Создание таблиц
models.Base.metadata.create_all(bind=database.engine)

# Определение моделей данных для API
class TeamBase(BaseModel):
    name: str

class Team(TeamBase):
    id: int
    class Config:
        from_attributes = True

class DriverBase(BaseModel):
    name: str
    points: int = 0

class Driver(DriverBase):
    id: int
    team_id: int
    team: Team
    class Config:
        from_attributes = True

class TeamWithDrivers(Team):
    drivers: List[DriverBase] = []
    class Config:
        from_attributes = True

class RaceBase(BaseModel):
    name: str
    date: date
    location: str

class Race(RaceBase):
    id: int
    class Config:
        from_attributes = True

# API эндпоинты
@app.get("/teams/", response_model=List[TeamWithDrivers])
def get_teams(db: Session = Depends(database.get_db)):
    return db.query(models.Team).all()

@app.get("/drivers/", response_model=List[Driver])
def get_drivers(db: Session = Depends(database.get_db)):
    return db.query(models.Driver).all()

@app.get("/races/", response_model=List[Race])
def get_races(db: Session = Depends(database.get_db)):
    return db.query(models.Race).all()

# Инициализация тестовых данных
@app.on_event("startup")
async def startup_event():
    db = next(database.get_db())
    if db.query(models.Team).count() == 0:
        teams = [
            models.Team(name="Red Bull Racing"),
            models.Team(name="Mercedes"),
            models.Team(name="Ferrari"),
            models.Team(name="McLaren"),
            models.Team(name="Aston Martin")
        ]
        for team in teams:
            db.add(team)
        
        drivers = [
            models.Driver(name="Max Verstappen", team_id=1, points=25),
            models.Driver(name="Lewis Hamilton", team_id=2, points=18),
            models.Driver(name="Charles Leclerc", team_id=3, points=15),
            models.Driver(name="Lando Norris", team_id=4, points=12),
            models.Driver(name="Sebastian Vettel", team_id=5, points=10)
        ]
        for driver in drivers:
            db.add(driver)
        
        races = [
            models.Race(name="Australian Grand Prix", date=date(2024, 3, 24), location="Melbourne"),
            models.Race(name="Monaco Grand Prix", date=date(2024, 5, 26), location="Monte Carlo"),
            models.Race(name="British Grand Prix", date=date(2024, 7, 7), location="Silverstone"),
            models.Race(name="Belgian Grand Prix", date=date(2024, 8, 25), location="Spa"),
            models.Race(name="Italian Grand Prix", date=date(2024, 9, 8), location="Monza")
        ]
        for race in races:
            db.add(race)
        
        db.commit()
```

## Настройка фронтенда

### Создание проекта Vue.js
```bash
cd frontend
npm create vue@latest
# Выберите следующие опции:
# - Project name: frontend
# - Add TypeScript? No
# - Add JSX Support? No
# - Add Vue Router? Yes
# - Add Pinia? No
# - Add Vitest? No
# - Add End-to-End Testing? No
# - Add ESLint? Yes
# - Add Prettier? Yes
```

### Установка зависимостей
```bash
cd frontend
npm install
npm install axios element-plus
```

### Создание компонентов

1. **TeamList.vue**:
```vue
<template>
  <div>
    <h2>Команды и гонщики</h2>
    <el-table :data="teams" style="width: 100%">
      <el-table-column prop="name" label="Команда" />
      <el-table-column label="Гонщики">
        <template #default="scope">
          <ul>
            <li v-for="driver in scope.row.drivers" :key="driver.id">
              {{ driver.name }} ({{ driver.points }} очков)
            </li>
          </ul>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TeamList',
  data() {
    return {
      teams: []
    }
  },
  async created() {
    try {
      const response = await axios.get('http://localhost:8000/teams/')
      this.teams = response.data
    } catch (error) {
      console.error('Ошибка при загрузке данных:', error)
    }
  }
}
</script>

<style scoped>
ul {
  list-style: none;
  padding: 0;
  margin: 0;
}
</style>
```

2. **RaceCalendar.vue**:
```vue
<template>
  <div>
    <h2>Календарь гонок</h2>
    <el-table :data="races" style="width: 100%">
      <el-table-column prop="name" label="Название гонки" />
      <el-table-column prop="date" label="Дата" />
      <el-table-column prop="location" label="Место проведения" />
    </el-table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'RaceCalendar',
  data() {
    return {
      races: []
    }
  },
  async created() {
    try {
      const response = await axios.get('http://localhost:8000/races/')
      this.races = response.data
    } catch (error) {
      console.error('Ошибка при загрузке данных:', error)
    }
  }
}
</script>
```

3. **DriverPoints.vue**:
```vue
<template>
  <div>
    <h2>Очки пилотов</h2>
    <el-table :data="drivers" style="width: 100%">
      <el-table-column prop="name" label="Пилот" />
      <el-table-column prop="points" label="Очки" />
    </el-table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'DriverPoints',
  data() {
    return {
      drivers: []
    }
  },
  async created() {
    try {
      const response = await axios.get('http://localhost:8000/drivers/')
      this.drivers = response.data
    } catch (error) {
      console.error('Ошибка при загрузке данных:', error)
    }
  }
}
</script>
```

4. **App.vue**:
```vue
<template>
  <div id="app">
    <el-container>
      <el-header>
        <h1>F1 Racing</h1>
      </el-header>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.el-header {
  background-color: #f56c6c;
  color: white;
  line-height: 60px;
  text-align: center;
}

.el-main {
  padding: 20px;
}
</style>
```

5. **router/index.js**:
```javascript
import { createRouter, createWebHistory } from 'vue-router'
import TeamList from '../components/TeamList.vue'
import RaceCalendar from '../components/RaceCalendar.vue'
import DriverPoints from '../components/DriverPoints.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'teams',
      component: TeamList
    },
    {
      path: '/races',
      name: 'races',
      component: RaceCalendar
    },
    {
      path: '/drivers',
      name: 'drivers',
      component: DriverPoints
    }
  ]
})

export default router
```

6. **main.js**:
```javascript
import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'
import router from './router'

const app = createApp(App)
app.use(ElementPlus)
app.use(router)
app.mount('#app')
```

## Запуск проекта

1. Запуск бэкенда:
```bash
cd backend
uvicorn main:app --reload
```

2. Запуск фронтенда:
```bash
cd frontend
npm run serve
```

3. Откройте браузер и перейдите по адресу: http://localhost:8080

## Структура базы данных

### Таблица teams
- id (Integer, Primary Key) - уникальный идентификатор команды
- name (String) - название команды

### Таблица drivers
- id (Integer, Primary Key) - уникальный идентификатор гонщика
- name (String) - имя гонщика
- points (Integer) - количество очков
- team_id (Integer, Foreign Key) - связь с таблицей teams

### Таблица races
- id (Integer, Primary Key) - уникальный идентификатор гонки
- name (String) - название гонки
- date (Date) - дата проведения
- location (String) - место проведения

## API эндпоинты

### GET /teams/
Возвращает список всех команд с их гонщиками.

### GET /drivers/
Возвращает список всех гонщиков.

### GET /races/
Возвращает список всех гонок.

## Компоненты фронтенда

### TeamList.vue
Отображает список команд и их гонщиков в виде таблицы.

### RaceCalendar.vue
Отображает календарь гонок с датами и местами проведения.

### DriverPoints.vue
Отображает таблицу очков гонщиков.

## Изменения в структуре фронтенда

### Упрощение навигации
Вместо Vue Router теперь используется простое переключение компонентов через переменную состояния:
```javascript
data() {
  return {
    currentPage: 'teams'
  }
}
```

### Обновленная структура компонентов
1. **App.vue**:
   - Простая навигация через переключение состояния
   - Условный рендеринг компонентов
   - Базовые стили для всего приложения

2. **TeamList.vue**:
   - Отображение команд и их гонщиков
   - Индикатор загрузки
   - Обработка ошибок

3. **RaceCalendar.vue**:
   - Отображение календаря гонок
   - Форматирование дат
   - Индикатор загрузки
   - Обработка ошибок

4. **DriverPoints.vue**:
   - Отображение очков пилотов
   - Отображение команды пилота
   - Индикатор загрузки
   - Обработка ошибок

### Основные улучшения
1. Добавлены индикаторы загрузки данных
2. Добавлена обработка ошибок
3. Улучшена читаемость кода через комментарии
4. Упрощена навигация
5. Добавлено форматирование дат
6. Улучшена структура таблиц

### Стилизация
1. Базовые стили для таблиц
2. Стили для навигации
3. Адаптивная верстка
4. Улучшенная читаемость данных

## Возможные улучшения

1. Добавить аутентификацию пользователей
2. Реализовать возможность редактирования данных
3. Добавить поиск и фильтрацию
4. Добавить сортировку таблиц
5. Улучшить дизайн интерфейса
6. Добавить анимации
7. Реализовать кэширование данных
8. Добавить тесты # cars
