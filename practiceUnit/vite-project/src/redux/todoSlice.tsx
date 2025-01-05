import {createSlice, PayloadAction} from "@reduxjs/toolkit";

interface Task{
    id:number,
    title:string
}

interface TodoState{
    tasks:Task[]
}

const initialState : TodoState={
    tasks :[]
}

const todoSlice =createSlice({
    name:"todos",
    initialState,
    reducers :{
        addTask:(state, action: PayloadAction<string>)=>{
            state.tasks.push({id:Date.now(), title:action.payload})
            console.log("workingg")
        },
        editTask:(state, action: PayloadAction<{id:number ; title:string}>) =>{
            const task = state.tasks.find((task)=>task.id === action.payload.id);
            if (task){
                task.title = action.payload.title;
            }
        },
        deleteTask:(state,action:PayloadAction<number>) => {
            state.tasks=state.tasks.filter((task)=>task.id !==action.payload)
        },
    }
});

export const {addTask, editTask, deleteTask} = todoSlice.actions;
export default todoSlice.reducer;