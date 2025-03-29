<!-- 
  Компонент TeamList.vue отвечает за отображение списка команд и их пилотов.
  Здесь мы используем Element Plus для создания красивой таблицы с данными.
  Компонент получает данные с бэкенда и отображает их в удобном формате.
-->
<template>
  <div>
    <!-- Заголовок компонента -->
    <h2>Команды и гонщики</h2>
    <!-- Индикатор загрузки -->
    <div v-if="loading">Загрузка...</div>
    <!-- Сообщение об ошибке -->
    <div v-else-if="error">{{ error }}</div>
    <!-- Таблица с данными -->
    <table v-else>
      <thead>
        <tr>
          <th>Команда</th>
          <th>Гонщики</th>
        </tr>
      </thead>
      <tbody>
        <!-- Перебираем все команды -->
        <tr v-for="team in teams" :key="team.id">
          <td>{{ team.name }}</td>
          <td>
            <!-- Список гонщиков команды -->
            <ul>
              <!-- Перебираем всех гонщиков команды -->
              <li v-for="driver in team.drivers" :key="driver.id">
                {{ driver.name }} ({{ driver.points }} очков)
              </li>
            </ul>
          </td>
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
  name: 'TeamList',
  
  // Определяем начальное состояние
  data() {
    return {
      // Массив для хранения команд
      teams: [],
      // Флаг загрузки данных
      loading: false,
      // Текст ошибки
      error: null
    }
  },
  
  // Хук mounted вызывается после монтирования компонента
  async mounted() {
    // Устанавливаем флаг загрузки
    this.loading = true
    try {
      // Запрашиваем данные с бэкенда
      const response = await axios.get('http://localhost:8000/teams/')
      // Сохраняем полученные данные
      this.teams = response.data
    } catch (error) {
      // В случае ошибки сохраняем её текст
      console.error('Ошибка при загрузке команд:', error)
      this.error = 'Не удалось загрузить данные о командах'
    } finally {
      // Снимаем флаг загрузки
      this.loading = false
    }
  }
}
</script>

<style scoped>
/* Стили применяются только к этому компоненту */
ul {
  /* Убираем маркеры списка */
  list-style: none;
  /* Убираем отступы */
  padding: 0;
  margin: 0;
}
</style> 