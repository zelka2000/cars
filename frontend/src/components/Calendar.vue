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