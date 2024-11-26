import React, { useState, useEffect } from "react";
import {
  collection,
  addDoc,
  getDocs,
  updateDoc,
  deleteDoc,
  doc,
} from "firebase/firestore";
import { db } from "./components/firebase-config";
import Navbar from "./components/navbar";

const App = () => {
  const [tasks, setTasks] = useState([]);
  const [taskName, setTaskName] = useState("");
  const [editingTaskId, setEditingTaskId] = useState(null);

  const fetchTasks = async () => {
    const querySnapshot = await getDocs(collection(db, "tasks"));
    const fetchedTasks = querySnapshot.docs.map((doc) => ({
      id: doc.id,
      ...doc.data(),
    }));
    setTasks(fetchedTasks);
  };

  const addTask = async () => {
    if (!taskName) return;
    await addDoc(collection(db, "tasks"), { name: taskName, status: "not-started" });
    setTaskName("");
    fetchTasks();
  };

  const editTask = async (id, name) => {
    await updateDoc(doc(db, "tasks", id), { name });
    setEditingTaskId(null);
    fetchTasks();
  };

  const deleteTask = async (id) => {
    await deleteDoc(doc(db, "tasks", id));
    fetchTasks();
  };

  const updateStatus = async (id, status) => {
    await updateDoc(doc(db, "tasks", id), { status });
    fetchTasks();
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  return (
    <div>
      <Navbar tasks={tasks} />
      <div>
        <input
          type="text"
          value={taskName}
          onChange={(e) => setTaskName(e.target.value)}
          placeholder="Enter task"
        />
        <button onClick={addTask}>Add Task</button>
      </div>
      <div className="tasks-list">
        {tasks.map((task) => (
          <div key={task.id} className="task-card">
            {editingTaskId === task.id ? (
              <input
                type="text"
                defaultValue={task.name}
                onBlur={(e) => editTask(task.id, e.target.value)}
              />
            ) : (
              <p>{task.name}</p>
            )}
            <button onClick={() => setEditingTaskId(task.id)}>Edit</button>
            <button onClick={() => deleteTask(task.id)}>Delete</button>
            <select
              value={task.status}
              onChange={(e) => updateStatus(task.id, e.target.value)}
            >
              <option value="not-started">Not Started</option>
              <option value="ongoing">Ongoing</option>
              <option value="completed">Completed</option>
            </select>
          </div>
        ))}
      </div>
    </div>
  );
};

export default App;
