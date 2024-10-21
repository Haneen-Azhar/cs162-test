const moveTask = (taskId, newStatus) => {
  fetch(`/api/tasks/${taskId}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ status: newStatus }),
  }).then(() => {
    fetchTasks(); // Refresh the task list after moving
  });
};

return (
  <div>
    <h1>Kanban Board</h1>
    <div className="kanban-columns">
      <div className="column">
        <h2>To Do</h2>
        {tasks.filter(task => task.status === 'To Do').map(task => (
          <div key={task.id} className="task-card">
            {task.title}
            <button onClick={() => moveTask(task.id, 'In Progress')}>Move to In Progress</button>
          </div>
        ))}
      </div>
      <div className="column">
        <h2>In Progress</h2>
        {tasks.filter(task => task.status === 'In Progress').map(task => (
          <div key={task.id} className="task-card">
            {task.title}
            <button onClick={() => moveTask(task.id, 'Done')}>Move to Done</button>
          </div>
        ))}
      </div>
      <div className="column">
        <h2>Done</h2>
        {tasks.filter(task => task.status === 'Done').map(task => (
          <div key={task.id} className="task-card">
            {task.title}
          </div>
        ))}
      </div>
    </div>
  </div>
);
