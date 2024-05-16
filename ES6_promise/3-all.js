import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((values) => {
      const picture = values[0];
      const user = values[1];
      console.log(`${picture.body} ${user.firstName} ${user.lastName}`);
    }).catch(() => {
      console.log('Signup system offline');
    });
}
