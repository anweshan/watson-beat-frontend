// Scripts for Watson Beat Web Demo
MOODS = ["EDM", "Space", "anthematic", "bommarch", "chill", "inspire",
         "popfunk", "propulsion", "reggaepop"];
COMPLEXITIES = ["simple", "super_simple", "semi_complex"];


// Component for a text input
Vue.component('text-input', {
  props: ['name', 'id', 'help', 'value'],
  template: `
<div class="form-group mx-1">
  <label :for="id">
    {{name}}
    <a href="#" :title="help">
      ?
    </a>
  </label>
  <input type="text" class="form-control"
         :aria-described-by="id + '-help'"
         :id="id"
         :name="id"
         :value="value">
  </input>
</div>
`
});


// Component for a select input
Vue.component('select-input', {
  props: ['name', 'id', 'help', 'options'],
  template: `
<div class="form-group mx-1">
  <label :for="id">
    {{name}}
    <a href="#" :title="help">
      ?
    </a>
  </label>
  <select :id="id" class="form-control"
          :aria-described-by="id+ '-help'"
          :name="id">
    <option v-for="opt in options">{{ opt }}</option>
  </select>
</div>
`
});


// Component for a section
Vue.component('wb-section', {
  props: ['movementId', 'sectionId'],
  template: `
<section>
  <h5>section {{ sectionId }}</h5>
  <div class="d-flex">
    <text-input
      name="Time signature"
      :id="getId('tse')"
      help="Time signature, e.g. '4/4'"
      value="4/4">
    </text-input>
    <select-input
      name="Energy"
      :id="getId('energy')"
      help="The number of layers in a range playing during a section (low, medium, high). Each of these categories represents a range of layers that can be playing. For instance, 'low' can be 1-4 layers while 'high' can be 3-12 layers."
      :options="['low', 'medium', 'high']">
    </select-input>
    <text-input
      name="Beats per minute"
      :id="getId('bpm')"
      help="Tempo in beats per minute (e.g. '100')"
      value="100">
    </text-input>
    <text-input
      name="Duration"
      :id="getId('duration')"
      help="Min and max number of seconds a section can be (e.g. '10 to 20 seconds')"
      value="10 to 20 seconds">
    </text-input>
    <text-input
      name="Duration in measures"
      :id="getId('durationInMeasures')"
      help="Number of measures a section can be. Can be one or two options to choose between (e.g. '4', '2 or 4')"
      value="4">
    </text-input>
    <select-input
      name="Slope"
      :id="getId('slope')"
      help="The rate of change in the density level of a section"
      :options="['stay', 'gradual', 'steep']">
    </select-input>
    <select-input
      name="Direction"
      :id="getId('direction')"
      help="Determines whether layers will be added or removed during a section ('up' - adds layers, 'down' - removes layers)"
      :options="['up', 'down']">
    </select-input>
  </div>
</section>
`,
  methods: {
    getId: function(name) {
      return ('movement-' + this.movementId + '-section-' + this.sectionId +
              '-' + name);
    }
  }
});



// Component for a movement
Vue.component('movement', {
  props: ['movementId'],
  data: function() {
    return {
      numSections: 1
    };
  },
  template: `
<section>
  <h3>movement {{ movementId }}</h3>
  <div class="d-flex">
    <text-input
      name="movementDuration"
      :id="getId('movementDuration')"
      help="Duration of the movement in seconds (e.g. 60)"
      value="60">
    </text-input>
    <select-input
      name="mood"
      :id="getId('mood')"
      help="'mood' for the movement"
      :options="getMoods()">
    </select-input>
    <select-input
      name="complexity"
      :id="getId('complexity')"
      help="Determines the complexity of the chord progressions"
      :options="getComplexities()">
    </select-input>
  </div>
  <section class="border p-2 m-2">
    <wb-section
      v-for="i in numSections"
      :key="i - 1"
      :movementId="movementId"
      :sectionId="i - 1">
    </wb-section>
    <button @click.stop.prevent="numSections += 1">Add a section</button>
  </section>
</section> 
`,
  methods: {
    getId: function(name) {
      return 'movement-' + this.movementId + '-' + name;
    },
    getMoods: function() {
      return MOODS;
    },
    getComplexities: function() {
      return COMPLEXITIES;
    }
  }
});


Vue.component('composition', {
  data: function() {
    return {
      numMovements: 1
    };
  },
  template: `
<section class="border p-2 mb-2">
  <movement
    v-for="i in numMovements"
    :key="i - 1"
    :movementId="i - 1">
  </movement>
  <button @click.stop.prevent="numMovements += 1">Add a movement</button>
</section>
`
});

var app = new Vue({
  el: '#app',
  data: {}
});
