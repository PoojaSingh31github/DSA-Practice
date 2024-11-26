import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
    apiKey: "AIzaSyBSZRQb08FoiumSJ-t_sx-LTB5Nm7TfCd0",
    authDomain: "assignment-aebd2.firebaseapp.com",
    projectId: "assignment-aebd2",
    storageBucket: "assignment-aebd2.firebasestorage.app",
    messagingSenderId: "480143971836",
    appId: "1:480143971836:web:2d8e2b474e3a742f6f8e79"
};


const app = initializeApp(firebaseConfig);
export const db = getFirestore(app);