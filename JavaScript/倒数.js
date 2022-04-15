let length = 1000000;
let rand_array = [];
let output = [];
for(var i=0;i<length;i++){
    rand_array[i] = Math.floor(Math.random()*10);
    console.log(rand_array);
}
let start = (new Date()).getMilliseconds();
for(var i=0;i<length;i++){
    output[i] = 1.0/rand_array[i];
    // console.log(output);
}
let end = (new Date()).getMilliseconds();
console.log(end - start);