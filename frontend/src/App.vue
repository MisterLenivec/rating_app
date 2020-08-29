<template>
  <div id="app">

    <form @submit.prevent="submitForm">
      <div class="form-group row inputWrapper">
        <input type="text" class="form-control col-3 mx-2 inputField"
               placeholder="Name" v-model="course.name">
        <input type="text" class="form-control col-3 mx-2 inputField"
               placeholder="Site URL" v-model="course.url">
<!--        <input type="text" class="form-control col-3 mx-2 inputField"-->
<!--               placeholder="Rating from 0 to 5" v-model="course.rating">-->
        <select class="form-control col-3 mx-2 inputField" v-model="course.rating">
          <option disabled value="">Rating</option>
          <option>0</option>
          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
          <option>5</option>
        </select>
        <button class="btn btn-success">Submit</button>
      </div>
    </form>
    <table class="table">
      <thead>
        <tr>
          <th>Name</th>
          <th>Site</th>
          <th>Rating</th>
        </tr>
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
      courses: [],
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

    async CRUDFunction(method, courseId) {
      await this.getCourses();

      await fetch(`http://127.0.0.1:8000/api/courses/${courseId ? courseId + '/' : ''}`, {
        method: method,
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.course)
      });

      await this.getCourses();
      this.course = {};
    },

    async createCourse() {
      await this.CRUDFunction('post');
    },

    async editCourse() {
      await this.CRUDFunction('put', this.course.id);
    },

    async deleteCourse(course) {
      await this.CRUDFunction('delete', course.id);
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
@media all and (max-width: 500px) {
  #app {
    margin: 0;
  }
}
</style>

<style scoped>
  .inputWrapper {
    display: flex;
    justify-content: center;
  }

  @media all and (max-width: 1000px) {
    .inputWrapper {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: stretch;
      max-width: 100%;
    }
    .inputField {
      max-width: 100%;
      margin: 1px;
    }
    .table {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
  }
</style>
