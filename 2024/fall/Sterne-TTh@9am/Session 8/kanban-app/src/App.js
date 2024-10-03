import React, { useState } from 'react';
import './App.css';
import TaskColumn from './components/TaskColumn';
import TaskForm from './components/TaskForm';

function App() {
  const [todoTasks, setTodoTasks] = useState(['Task 1', 'Task 2']);
  const [inProgressTasks, setInProgressTasks] = useState(['Task 3']);
  const [doneTasks, setDoneTasks] = useState(['Task 4', 'Task 5']);

  const addTask = (newTask) => {
    setTodoTasks([...todoTasks, newTask]);
  };

  return (
    <div className="App">
      <h1>Kanban Board</h1>
      <TaskForm addTask={addTask} />
      <div style={{ display: 'flex', justifyContent: 'space-around' }}>
        <TaskColumn title="To-Do" tasks={todoTasks} />
        <TaskColumn title="In Progress" tasks={inProgressTasks} />
        <TaskColumn title="Done" tasks={doneTasks} />
      </div>
    </div>
  );
}

export default App;