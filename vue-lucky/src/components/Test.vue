<template>
  <div class="test">
    <head-top></head-top>
    <span style="color: #ff0000;">
      <!--{{msg}}-->
    </span>

    <ul id="test">
      <li v-for="item in items">
        <img width="300" height="300" :src="item.path" alt="">
      </li>

    </ul>
  </div>
</template>

<script>
  import headTop from '../components/headTop'

  export default {
    name: 'Test',
    data () {
      return {
        items: [],
        msg: 'test'
      }
    },
    components: {
      headTop
    },
    created () {
      this.$axios.get('http://127.0.0.1:5000/', {})
        .then(response => {
          this.items = response.data.data
          console.log(this.items)
          this.msg = response.data.data[2].name
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    methods: {

    }
  }
</script>

<style scoped>
  li {
    float: left;
    margin-right: 20px;
    list-style: none;

  }

</style>
