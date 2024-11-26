import React from "react";

const Navbar = ({ tasks }) => {
  const completed = tasks.filter((task) => task.status === "completed");
  const ongoing = tasks.filter((task) => task.status === "ongoing");
  const notStarted = tasks.filter((task) => task.status === "not-started");

  return (
    <div className="navbar">
      <h1>Task Manager</h1>
      <div>
        <span>Completed: {completed.length}</span>
        <span>Ongoing: {ongoing.length}</span>
        <span>Not Started: {notStarted.length}</span>
      </div>
      <div className="task-buckets">
        <div>
          <h3>Completed</h3>
          <ul>
            {completed.map((task) => (
              <li key={task.id}>{task.name}</li>
            ))}
          </ul>
        </div>
        <div>
          <h3>Ongoing</h3>
          <ul>
            {ongoing.map((task) => (
              <li key={task.id}>{task.name}</li>
            ))}
          </ul>
        </div>
        <div>
          <h3>Not Started</h3>
          <ul>
            {notStarted.map((task) => (
              <li key={task.id}>{task.name}</li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
};

export default Navbar;
