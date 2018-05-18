// Scripts for Watson Beat Web Demo
MOODS = ["EDM", "Space", "anthematic", "bommarch", "chill", "inspire",
         "popfunk", "propulsion", "reggaepop"];
COMPLEXITIES = ["simple", "super_simple", "semi_complex"];
MIDIS = ["Custom", "entertainer.mid","greensleeves.mid","happy1.mid","hungarian_dance_no5.mid","jingle1.mid","mary.mid","new_mel.mid","new_mel2.mid","new_world_symphony2.mid","new_world_symphony_largo.mid","ode_to_joy.mid","polish_melody.mid"];
INIS = ["Custom", "Anthematic.ini","BomMarch.ini","Chill.ini","EDM.ini","Inspire.ini","MoodChange.ini","PopFunk.ini","Propulsion.ini","ReggaePop.ini","ReggaePopSeconds.ini","ReggaePop_Time_Space.ini","Space.ini","changeMoods.ini","moods.ini","moods1.ini","moods2.ini","moods3.ini","moods4.ini"];


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
          :name="id"
          @change="$emit('change')">
    <option v-for="opt in options">{{ opt }}</option>
  </select>
</div>
`
});

// Component for a file input
Vue.component('file-input', {
  props: ['name', 'id', 'help'],
  template: `
<div class="form-group mx-1">
  <label :for="id">
    {{name}}
    <a href="#" :title="help">
      ?
    </a>
  </label>
  <input type="file" class="form-control" accept=".mid, .midi"
         :aria-described-by="id + '-help'"
         :id="id"
         :name="id"
         :value="value">
  </input>
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

Vue.component('midi-selector', {
  data: function() {
    return {
      isCustom: true 
    }
  },
  template: `
<section class="border p-2 mb-2">
  <h2>Input melody</h2>
  <p>
    Pick a 10-20 second midi file to inspire Watson Beat or upload your own
  </p>
  <select-input
    name="Select a .midi file"
    id="input-midi"
    help="Pick 'Custom' to upload your own .midi file or select one of the defaults"
    :options="getMidis()"
    @change="checkCustom()">
  </select-input>
  <file-input
    name="Upload a .midi file"
    id="input-midi-file"
    help="Upload a midi file"
    v-if="isCustom"></file-input>
</section>
`,
  methods: {
    getMidis: function() {
      return MIDIS;
    },
    checkCustom: function() {
      selector = document.getElementById('input-midi');
      this.isCustom = selector && selector.value == "Custom";
    }
  }
});


Vue.component('ini-selector', {
  data: function() {
    return {
      isCustom: true,
      numMovements: 1
    }
  },
  template: `
<section class="border p-2 mb-2">
  <h2>Parameters for the creativity engine</h2>
  <p>
    Input parameters for the creativity engine for each movement and section, or pick one of the default configurations.
  </p>
  <select-input
    name="Pick parameters"
    id="input-ini"
    help="Choose 'Custom' to pick your own parameters for the creativity engine or select one of the default configurations"
    :options="getInis()"
    @change="checkCustom()">
  </select-input>
  <div v-if="isCustom">
    <movement\
      v-for="i in numMovements"\
      :key="i - 1"\
      :movementId="i - 1">\
    </movement>\
    <button @click.stop.prevent="numMovements += 1">Add a movement</button>\
  </div>
</section>
`,
  methods: {
    getInis: function() {
      return INIS;
    },
    checkCustom: function() {
      selector = document.getElementById('input-ini');
      this.isCustom = selector && selector.value == "Custom";
      // No way to preserve the custom parameters right now so just
      // reset to the initial configuration
      if (!this.isCustom) {
        this.numMovements = 1;
      }
    }
  }
});


Vue.component('composition', {
  template: `
<div>
  <midi-selector></midi-selector>
  <ini-selector></ini-selector>
</div>
`
});

var app = new Vue({
  el: '#app',
  data: {}
});
