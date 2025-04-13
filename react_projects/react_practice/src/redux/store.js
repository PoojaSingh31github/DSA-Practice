import { createStore } from "redux";
import { inputReducer } from "./reducer";
import { persistStore, persistReducer } from 'redux-persist'
import storage from 'redux-persist/lib/storage'

const persistConfig = {
    key: 'root',
    storage,
    whitelist: ["cart"],
}

const persistedReducer = persistReducer(persistConfig, inputReducer)

export let store = createStore(persistedReducer)
export let persistor = persistStore(store)
