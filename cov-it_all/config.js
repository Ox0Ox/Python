import firebase from 'firebase'

var firebaseConfig = {
    apiKey: "AIzaSyDvjozxDj9_EeWJ_FKFKDeG7zY4AsTR1zY",
    authDomain: "newsletterapp-9c10b.firebaseapp.com",
    databaseURL: "https://newsletterapp-9c10b-default-rtdb.firebaseio.com",
    projectId: "newsletterapp-9c10b",
    storageBucket: "newsletterapp-9c10b.appspot.com",
    messagingSenderId: "254451300892",
    appId: "1:254451300892:web:050cab0778e7752a0d3dd9"
  };
  // Initialize Firebase
  if(!firebase.apps.length)
    firebase.initializeApp(firebaseConfig);

export default firebase.database() ; 