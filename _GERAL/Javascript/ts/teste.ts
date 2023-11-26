let msg: string = "1";

console.log("hi mom");

const f = () => {
  for (let i: number = 0; i < 10; i++) {
    i = i * i;
    console.log(i);
  }
};

f();

let list: [string, string];

list = ["d", "f"];

console.log(typeof list, typeof msg);
