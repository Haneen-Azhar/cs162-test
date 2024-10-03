import './App.css';
import TaskColumn from './components/TaskColumn';
import TaskForm from './components/TaskForm'; // Keeping the form feature

function App() {
  const todoTasks = ['Task 1', 'Task 2'];
  const inProgressTasks = ['Task 3'];
  const doneTasks = ['Task 4', 'Task 5'];

  return (
    <div className="App">
      <h1 className="kanban-header">Kanban Board</h1>
      <TaskForm /> {/* Task form feature */}
      <div className="kanban-board">
        <TaskColumn title="To-Do" tasks={todoTasks} />
        <TaskColumn title="In Progress" tasks={inProgressTasks} />
        <TaskColumn title="Done" tasks={doneTasks} />
      </div>
    </div>
  );
}

export default App;
