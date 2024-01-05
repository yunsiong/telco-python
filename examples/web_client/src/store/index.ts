import Vue from 'vue';
import Vuex from 'vuex';

import telco from './modules/telco';
import telcoBus from './plugins/telco';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    telco
  },
  plugins: [
    telcoBus()
  ]
});
