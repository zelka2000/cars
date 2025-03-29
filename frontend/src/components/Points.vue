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