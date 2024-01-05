import { Module } from 'vuex';

interface TelcoState {
  processes: Process[],
}

type Process = [number, string];

const telcoModule: Module<TelcoState, any> = {
  state: {
    processes: []
  },

  mutations: {
  }
};

export default telcoModule;
