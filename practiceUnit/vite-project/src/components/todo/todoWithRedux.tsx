import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { RootState, AppDispatch } from "../../redux/store"; // Import your store types
import { addTask, editTask, deleteTask } from "../../redux/todoSlice";

export const TodoWithRedux: React.FC = () => {
    const [input, setInput] = useState<string>(""); // Input field state
    const [editTaskId, setEditTaskId] = useState<number | null>(null); // ID of task being edited

    const tasks = useSelector((state: RootState) => state.todos.tasks); // Access tasks from Redux store
    const dispatch: AppDispatch = useDispatch(); // Redux dispatch

    const handleAddOrUpdateTask = (e: React.FormEvent) => {
        e.preventDefault();

        if (input.trim()) {
            if (editTaskId !== null) {
                // Dispatch edit action
                dispatch(editTask({ id: editTaskId, title: input }));
                setEditTaskId(null); // Clear edit mode
            } else {
                // Dispatch add action
                dispatch(addTask(input));
            }

            setInput(""); // Clear input field
        }
    };

    const handleEditTask = (taskId: number, taskTitle: string) => {
        setInput(taskTitle); // Set input to the task's title
        setEditTaskId(taskId); // Set edit mode
    };

    const handleDeleteTask = (taskId: number) => {
        dispatch(deleteTask(taskId)); // Dispatch delete action
    };

    return (
        <div>
            <h1>Todo App</h1>
            <form onSubmit={handleAddOrUpdateTask}>
                <input
                    type="text"
                    placeholder="Enter task title"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                />
                <button type="submit">
                    {editTaskId !== null ? "Update Task" : "Add Task"}
                </button>
            </form>

            <ul>
                {tasks.map((task) => (
                    <li key={task.id}>
                        <span>
                            <strong>Title:</strong> {task.title}
                        </span>
                        <button onClick={() => handleEditTask(task.id, task.title)}>
                            Edit
                        </button>
                        <button onClick={() => handleDeleteTask(task.id)}>Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};
