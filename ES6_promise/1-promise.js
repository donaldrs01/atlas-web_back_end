export default function getFullResponseFromAPI(success) {
  // Create new Promise that executes depending on resolution/failure of asyncronous operation
  return new Promise((resolve, reject) => {
    if (success) {
      // On success, resolve with log message
      resolve({
        status: 200,
        body: 'Success',
      });
    } else {
      // Reject promise with error message
      reject(new Error('The fake API is not working currently'));
    }
  });
}
