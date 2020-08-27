<template>
  <div id="app">

    <form @submit.prevent="submitForm">
      <div class="form-group row">
        <input type="text" class="form-control col-3 mx-2" placeholder="Name"
               v-model="course.name">
        <input type="text" class="form-control col-3 mx-2" placeholder="Site URL"
               v-model="course.url">
        <input type="text" class="form-control col-3 mx-2" placeholder="Rating"
               v-model="course.rating">
        <button class="btn btn-success">Submit</button>
      </div>
    </form>

    <table class="table">
      <thead>
        <th>Name</th>
        <th>Site</th>
        <th>Rating</th>
      </thead>
      <tbody>
        <tr v-for="course in courses" :key="course.id"
            @dblclick="$data.course=course">
          <td>{{ course.name }}</td>
          <td>{{ course.url }}</td>
          <td>{{ course.rating }}</td>
          <td>
            <button class="btn btn-outline-danger btn-sm mx-1"
            @click="deleteCourse(course)">&#9253;</button>
          </td>
        </tr>
      </tbody>
    </table>
    
  </div>
</template>

<script>

export default {
  name: 'App',
  data() {
    return {
      course: {},
      courses: []
    }
  },
  async created() {
    await this.getCourses();
  },

  methods: {
    submitForm() {
      if (this.course.id === undefined) {
        this.createCourse();
      } else {
        this.editCourse();
      }
    },

    async getCourses() {
      var response = await fetch('http://127.0.0.1:8000/api/courses/');
      this.courses = await response.json();
    },

    async createCourse() {
      await this.getCourses();

      await fetch('http://127.0.0.1:8000/api/courses/', {
        method: 'post',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.course)
      });

      await this.getCourses();
      this.course = {};
    },

    async editCourse() {
      await this.getCourses();

      await fetch(`http://127.0.0.1:8000/api/courses/${this.course.id}/`, {
        method: 'put',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.course)
      });

      await this.getCourses();
      this.course = {};
    },

    async deleteCourse(course) {
      await this.getCourses();

      await fetch(`http://127.0.0.1:8000/api/courses/${course.id}/`, {
        method: 'delete',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.course)
      });

      await this.getCourses();
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
