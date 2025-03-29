<template>
  <div>
    <h2>Команды и пилоты</h2>
    <el-table :data="teams" style="width: 100%">
      <el-table-column prop="name" label="Команда" />
      <el-table-column label="Пилоты">
        <template #default="scope">
          <ul>
            <li v-for="driver in scope.row.drivers" :key="driver.id">
              {{ driver.name }}
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