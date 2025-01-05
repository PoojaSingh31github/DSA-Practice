import { configureStore } from "@reduxjs/toolkit";
import todoReducer from "./todoSlice"; // Path to your todoSlice file

const store = configureStore({
    reducer: {
        todos: todoReducer,
    },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
export default store;
