<!-- 
  Компонент DriverPoints.vue отвечает за отображение очков пилотов.
  Здесь мы показываем таблицу со всеми пилотами и количеством их очков.
  Компонент получает данные с бэкенда и отображает их в виде таблицы.
-->
<template>
  <div>
    <!-- Заголовок компонента -->
    <h2>Очки пилотов</h2>
    <!-- Индикатор загрузки -->
    <div v-if="loading">Загрузка...</div>
    <!-- Сообщение об ошибке -->
    <div v-else-if="error">{{ error }}</div>
    <!-- Таблица с данными -->
    <table v-else>
      <thead>
        <tr>
          <th>Пилот</th>
          <th>Команда</th>
          <th>Очки</th>
        </tr>
      </thead>
      <tbody>
        <!-- Перебираем всех пилотов -->
        <tr v-for="driver in drivers" :key="driver.id">
          <td>{{ driver.name }}</td>
          <td>{{ driver.team?.name || 'Нет команды' }}</td>
          <td>{{ driver.points }}</td>
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
  name: 'DriverPoints',
  
  // Определяем начальное состояние
  data() {
    return {
      // Массив для хранения пилотов
      drivers: [],
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
      const response = await axios.get('http://localhost:8000/drivers/')
      // Сохраняем полученные данные
      this.drivers = response.data
    } catch (error) {
      // В случае ошибки сохраняем её текст
      console.error('Ошибка при загрузке пилотов:', error)
      this.error = 'Не удалось загрузить данные о пилотах'
    } finally {
      // Снимаем флаг загрузки
      this.loading = false
    }
  }
}
</script> 