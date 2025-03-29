<template>
  <div id="app">
    <!-- Шапка приложения -->
    <header>
      <!-- Заголовок приложения -->
      <h1>F1 Racing</h1>
      <!-- Навигационное меню -->
      <nav>
        <!-- Ссылки для переключения между страницами -->
        <!-- @click.prevent предотвращает стандартное поведение ссылки -->
        <a href="#" @click.prevent="currentPage = 'teams'">Команды</a> |
        <a href="#" @click.prevent="currentPage = 'races'">Гонки</a> |
        <a href="#" @click.prevent="currentPage = 'drivers'">Пилоты</a>
      </nav>
    </header>
    <!-- Основное содержимое -->
    <main>
      <!-- Условный рендеринг компонентов в зависимости от выбранной страницы -->
      <TeamList v-if="currentPage === 'teams'" />
      <RaceCalendar v-if="currentPage === 'races'" />
      <DriverPoints v-if="currentPage === 'drivers'" />
    </main>
  </div>
</template>

<script>
// Импортируем компоненты для каждой страницы
import TeamList from './components/TeamList.vue'
import RaceCalendar from './components/RaceCalendar.vue'
import DriverPoints from './components/DriverPoints.vue'

export default {
  // Имя компонента
  name: 'App',
  
  // Регистрируем дочерние компоненты
  components: {
    TeamList,
    RaceCalendar,
    DriverPoints
  },
  
  // Определяем начальное состояние
  data() {
    return {
      // По умолчанию показываем страницу команд
      currentPage: 'teams'
    }
  }
}
</script>

<style>
/* Основные стили приложения */
#app {
  /* Настройка шрифта */
  font-family: Arial, sans-serif;
  /* Выравнивание текста по центру */
  text-align: center;
  /* Максимальная ширина контента */
  max-width: 1200px;
  /* Центрирование контента */
  margin: 0 auto;
  /* Внутренние отступы */
  padding: 20px;
}

/* Стили для шапки */
header {
  /* Цвет фона */
  background-color: #2c3e50;
  /* Цвет текста */
  color: white;
  /* Внутренние отступы */
  padding: 20px;
  /* Отступ снизу */
  margin-bottom: 20px;
}

/* Стили для навигации */
nav {
  /* Отступ сверху */
  margin-top: 10px;
}

/* Стили для ссылок в навигации */
nav a {
  /* Цвет текста */
  color: white;
  /* Убираем подчеркивание */
  text-decoration: none;
  /* Внутренние отступы */
  padding: 5px 10px;
}

/* Стили для ссылок при наведении */
nav a:hover {
  /* Добавляем подчеркивание */
  text-decoration: underline;
}

/* Стили для таблиц */
table {
  /* Ширина на всю доступную область */
  width: 100%;
  /* Убираем двойные границы */
  border-collapse: collapse;
  /* Отступ сверху */
  margin-top: 20px;
}

/* Стили для ячеек таблицы */
th, td {
  /* Границы ячеек */
  border: 1px solid #ddd;
  /* Внутренние отступы */
  padding: 8px;
  /* Выравнивание текста */
  text-align: left;
}

/* Стили для заголовков таблицы */
th {
  /* Цвет фона */
  background-color: #f2f2f2;
}

/* Стили для четных строк таблицы */
tr:nth-child(even) {
  /* Цвет фона */
  background-color: #f9f9f9;
}
</style>
