<template>
  <ul>
    <li v-for="todo in todos" :key='todo.order'>
      {{ todo.title }}
    </li>
  </ul>
</template>

<script>
export default {
  name: 'HelloWorld',
  data: function() {
    return {
      todos: [
        { order: 0, title: "Alamakota", body: "Lotem ipsum" },
        { order: 1, title: "Alamakota2", body: "Lotem ipsum2" }
      ]
    }
  },
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
