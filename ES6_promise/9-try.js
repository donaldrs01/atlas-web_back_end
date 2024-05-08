export default function guardrail(mathFunction) {
  // create empty array
  const queue = [];
  try {
    // perform math operation and append the answer to the queue array
    const answer = mathFunction();
    queue.push(answer);
  } catch (error) {
    queue.push(`Error: ${error.message}`);
  }
  // Outside of this block, append guardrail message
  // Will log in every case
  queue.push('Guardrail was processed');
  // Return the queue will all messages stacked
  return queue;
}
