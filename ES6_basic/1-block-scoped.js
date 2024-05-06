export default function taskBlock(trueOrFalse) {
  const task = false;
  const  task2 = true;
  
  if (trueOrFalse) {
    const task = true;
    const task2 = false;
    // Log values of task and task2 within conditional block
    console.log(task, task2);
  }
  // Returns values of task and task2 at the function level
  return [task, task2];
  }
