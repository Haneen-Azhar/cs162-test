import React, { useEffect, useState } from 'react';
import './KanbanBoard.css';

const KanbanBoard = () => {
    const [notStartedTasks, setNotStartedTasks] = useState([]);
    const [inProgressTasks, setInProgressTasks] = useState([]);
    const [doneTasks, setDoneTasks] = useState([]);
    const [newTaskTitle, setNewTaskTitle] = useState('');
    const [newTaskDescription, setNewTaskDescription] = useState('');

    useEffect(() => {
        fetch('/api/tasks')
            .then(response => response.json())
            .then(data => {
                // Filter tasks by status
                setNotStartedTasks(data.not_started_tasks || []);
                setInProgressTasks(data.in_progress_tasks || []);
                setDoneTasks(data.done_tasks || []);
            });
    }, []);

    const handleAddTask = () => {
        // Logic to handle adding a task (this can be further connected to your backend later)
        console.log('New task added:', newTaskTitle, newTaskDescription);
        setNewTaskTitle('');
        setNewTaskDescription('');
    };

    return (
        <div className="kanban-board">
            {/* Column for Not Started tasks */}
            <div className="column">
                <h2>Not Started</h2>
                {notStartedTasks.map(task => (
                    <div key={task.id} className="task-card">
                        <h3>{task.title}</h3>
                        <p>{task.description}</p>
                    </div>
                ))}
            </div>

            {/* Column for In Progress tasks */}
            <div className="column">
                <h2>In Progress</h2>
                {inProgressTasks.map(task => (
                    <div key={task.id} className="task-card">
                        <h3>{task.title}</h3>
                        <p>{task.description}</p>
                    </div>
                ))}
            </div>

            {/* Column for Done tasks */}
            <div className="column">
                <h2>Completed</h2>
                {doneTasks.map(task => (
                    <div key={task.id} className="task-card">
                        <h3>{task.title}</h3>
                        <p>{task.description}</p>
                    </div>
                ))}
            </div>

            {/* Task form to add new tasks */}
            <div className="task-form">
                <h3>Add a New Task</h3>
                <input 
                    type="text" 
                    placeholder="Task Title" 
                    value={newTaskTitle} 
                    onChange={(e) => setNewTaskTitle(e.target.value)} 
                />
                <textarea 
                    placeholder="Task Description" 
                    value={newTaskDescription} 
                    onChange={(e) => setNewTaskDescription(e.target.value)} 
                />
                <button onClick={handleAddTask}>Add Task</button>
            </div>
        </div>
    );
};

export default KanbanBoard;
