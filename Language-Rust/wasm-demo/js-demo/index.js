let squarer;

function loadWebAssembly(fileName) {
  return fetch(fileName)
    .then(response => response.arrayBuffer())
    .then(buffer => WebAssembly.compile(buffer))
    .then(module => {return new WebAssembly.Instance(module) });
};
  
loadWebAssembly('wasm_hello_bg.wasm')
  .then(instance => {
    squarer = instance.exports.fib(12);
    console.log('Finished compiling! Ready when you are...',squarer);
  }); 