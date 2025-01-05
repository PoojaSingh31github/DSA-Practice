import React, { useState } from "react";

interface Task {
    id: number,
    title: string
}

export const Todo: React.FC = () => {
    const [input, setinput] = useState<string>("");
    const [task, setTask] = useState<Task[]>([]);
    const [editTaskId, seteditTaskId] = useState<number|null>(null)

    const handleAddtask = (e: React.FormEvent) => {
        e.preventDefault()
        if (input.trim()) {
            if(editTaskId !==null){
                setTask((prevtask)=>
                    prevtask.map((ele)=>
                        ele.id ===editTaskId ? {...ele,title:input}:ele)
                )
                seteditTaskId(null)
            }else{
                setTask([...task, {
                    id: Date.now(),
                    title :input
                }])
                setinput("")
            }
        }
    }

    const handleDeleteRTask =(taskId:number)=>{
       setTask(task.filter((ele)=>(ele.id != taskId)))
    }

    const editTask =(taskId:number) =>{
        const taskToEdit = task.find((ele)=>ele.id ===taskId)
        if (taskToEdit){
            setinput(taskToEdit.title)
            seteditTaskId(taskId)
        }

    }
    return (
        <div>
            <h1>todo app</h1>
            <form action="" onSubmit={handleAddtask}>
                <input type="text" placeholder="enter title of todo" name="title" value={input} onChange={(e) => setinput(e.target.value)} />
                <button type="submit">{editTaskId !== null ? "Update Task" : "Add Task"}</button>
            </form>

            <ul>
                {
                    task && task.map((ele) => (
                        <li key={ele.id}>
                            <span>id :{ele.id} <span>title : {ele.title}</span></span>
                            <button onClick={()=>handleDeleteRTask(ele.id)}>del</button>
                            <button onClick={()=>editTask(ele.id)}>edit</button>
                        </li>
                    ))
                }
            </ul>
        </div>
    )
}
