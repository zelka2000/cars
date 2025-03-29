# 
# Этот файл отвечает за настройку подключения к базе данных SQLite.
# Здесь мы создаем подключение к базе данных и настраиваем сессии для работы с ней.
#

# Импортируем необходимые компоненты из SQLAlchemy
from sqlalchemy import create_engine  # Для создания движка базы данных
from sqlalchemy.ext.declarative import declarative_base  # Для создания базового класса моделей
from sqlalchemy.orm import sessionmaker  # Для создания фабрики сессий

# Создаем URL для подключения к базе данных SQLite
# SQLite хранит все данные в файле f1.db в текущей директории
SQLALCHEMY_DATABASE_URL = "sqlite:///./f1.db"

# Создаем движок базы данных
# connect_args={"check_same_thread": False} нужен только для SQLite
# и позволяет использовать базу данных из разных потоков
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

# Создаем фабрику сессий
# Сессия - это единица работы с базой данных
# autocommit=False означает, что изменения не будут автоматически сохраняться
# autoflush=False означает, что изменения не будут автоматически отправляться в базу
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

# Создаем базовый класс для всех моделей
# Все модели будут наследоваться от этого класса
Base = declarative_base()

# Функция для получения сессии базы данных
# Используется как зависимость в FastAPI для внедрения сессии в эндпоинты
def get_db():
    """
    Генератор сессий базы данных.
    - Создает новую сессию
    - Передает её в эндпоинт
    - После завершения работы закрывает сессию
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 