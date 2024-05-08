import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  // Receive all promise requests from uploadPhoto / createUser
  return Promise.all([uploadPhoto(), createUser()])
    .then((resolvedPromises) => {
      // Extract resolved values from photo/user objects and put them into array
      const [photoObject, userObject] = resolvedPromises;
      console.log(`${photoObject.body} ${userObject.firstName} ${userObject.lastName}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
