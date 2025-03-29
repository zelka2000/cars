<!-- 
  Компонент RaceCalendar.vue отвечает за отображение календаря гонок.
  Здесь мы показываем список всех предстоящих гонок с их датами и местами проведения.
  Компонент получает данные с бэкенда и отображает их в виде таблицы.
-->
<template>
  <div>
    <!-- Заголовок компонента -->
    <h2>Календарь гонок</h2>
    <!-- Индикатор загрузки -->
    <div v-if="loading">Загрузка...</div>
    <!-- Сообщение об ошибке -->
    <div v-else-if="error">{{ error }}</div>
    <!-- Таблица с данными -->
    <table v-else>
      <thead>
        <tr>
          <th>Название гонки</th>
          <th>Дата</th>
          <th>Место проведения</th>
        </tr>
      </thead>
      <tbody>
        <!-- Перебираем все гонки -->
        <tr v-for="race in races" :key="race.id">
          <td>{{ race.name }}</td>
          <td>{{ formatDate(race.date) }}</td>
          <td>{{ race.location }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
// Импортируем axios для HTTP-запросов
import axios from 'axios'

export default {
  // Имя компонента
  name: 'RaceCalendar',
  
  // Определяем начальное состояние
  data() {
    return {
      // Массив для хранения гонок
      races: [],
      // Флаг загрузки данных
      loading: false,
      // Текст ошибки
      error: null
    }
  },
  
  // Методы компонента
  methods: {
    // Форматирование даты в локальный формат
    formatDate(dateStr) {
      const date = new Date(dateStr)
      return date.toLocaleDateString('ru-RU')
    }
  },
  
  // Хук mounted вызывается после монтирования компонента
  async mounted() {
    // Устанавливаем флаг загрузки
    this.loading = true
    try {
      // Запрашиваем данные с бэкенда
      const response = await axios.get('http://localhost:8000/races/')
      // Сохраняем полученные данные
      this.races = response.data
    } catch (error) {
      // В случае ошибки сохраняем её текст
      console.error('Ошибка при загрузке гонок:', error)
      this.error = 'Не удалось загрузить данные о гонках'
    } finally {
      // Снимаем флаг загрузки
      this.loading = false
    }
  }
}
</script> 