function TaskColumn({ title, tasks }) {
    return (
      <div>
        <h2>{title}</h2>
        <ul>
          {tasks.map((task, index) => (
            <li key={index}>{task}</li>
          ))}
        </ul>
      </div>
    );
  }
  
  export default TaskColumn;
  
