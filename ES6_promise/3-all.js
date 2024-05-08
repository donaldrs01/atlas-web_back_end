import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  // Receive all promise requests from uploadPhoto / createUser
  Promise.all([uploadPhoto(), createUser()])
    .then((resolvedPromises) => {
      const photoObject = resolvedPromises[0];
      const userObject = resolvedPromises[1];
      console.log(`body ${userObject.firstName} ${userObject.lastName}`);
    })
    .catch((error) => {
      console.log('Signup system offline', error);
    });
}
