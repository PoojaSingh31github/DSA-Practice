import {createStore} from "redux";

const initialState = {
    count:0
}

// reducer 

function counterReducer(state:any= initialState, action:any) {
    switch (action.type) {
        case "increment":
            return {...state, count:state.count+1}
    
        case "decrement":
            return {...state, count:state.count-1}
    
        default:
            return state;
    }
}

// store

const store= createStore(counterReducer)
export default store;