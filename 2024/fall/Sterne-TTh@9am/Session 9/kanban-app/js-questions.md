# Pre-class Work: React (Part 2) – Kanban React App

## 1. React Tutorial
For the React tutorial, I worked through chapters 5–6 as required. Here's a summary of the steps taken:

### Key Concepts:
- **State Management**: How to use `useState` and `useEffect` to handle state and lifecycle methods.
- **Mapping over Arrays**: Using `map` to render lists dynamically in JSX.
- **Event Handling**: Handling events such as button clicks to modify state in React components.

---

## 2. Kanban React App Refactor

I have refactored the Flask application to return Python dictionaries instead of HTML. The React app has been modified accordingly to use the new API endpoints provided by Flask. Below are the steps I followed to achieve this:

### Backend (Flask API) Changes:

1. **API Endpoints**:
    - I added endpoints that return Python dictionaries as JSON. Here's an example of how the `/api/tasks` endpoint was structured:

    ```python
    from flask import Flask, jsonify

    app = Flask(__name__)

    @app.route('/api/tasks', methods=['GET'])
    def get_tasks():
        tasks = [
            {'id': 1, 'name': 'Task 1', 'status': 'In Progress'},
            {'id': 2, 'name': 'Task 2', 'status': 'Complete'},
        ]
        return jsonify(tasks)
    
    if __name__ == '__main__':
        app.run(debug=True)
    ```

    - This API serves a list of tasks in JSON format.

2. **File Structure for Flask**:
    - Ensure that `api.py` is created under the `/kanban-app/` directory to contain this backend logic.

3. **Running Flask**:
    - I used the following command to run the Flask server:
    ```bash
    flask run
    ```

---

### Frontend (React) Changes:

1. **API Calls in React**:
    - In the React app, I replaced the static task data with an API call to the Flask backend. Here’s the React code to fetch tasks from the Flask API:

    ```javascript
    import React, { useState, useEffect } from 'react';

    const KanbanBoard = () => {
      const [tasks, setTasks] = useState([]);

      useEffect(() => {
        fetch('/api/tasks')
          .then(response => response.json())
          .then(data => setTasks(data));
      }, []);

      return (
        <div>
          <h1>Kanban Board</h1>
          <ul>
            {tasks.map(task => (
              <li key={task.id}>{task.name} - {task.status}</li>
            ))}
          </ul>
        </div>
      );
    };

    export default KanbanBoard;
    ```

2. **File Structure for React**:
    - The main frontend logic is inside `KanbanBoard.js` under `/src/` directory.

3. **Running the React App**:
    - I used the following command to run the React app:
    ```bash
    npm start
    ```

    - The app now dynamically renders tasks from the Flask API.

---

## 3. OpenAPI Generator

To prepare for the class activities, I installed the OpenAPI generator CLI globally using npm.

### Installation Command:
```bash
npm install @openapitools/openapi-generator-cli -g


## 4. Javascript Questions
While working through the React tutorial, I encountered a few JavaScript concepts and code snippets that were initially confusing. Below are some examples along with my initial confusion and subsequent understanding:

### Example 1: `useEffect` Dependencies
```javascript
useEffect(() => {
  // some code here
}, [count]); // Why does this run only when 'count' changes, but not otherwise?


Confusion: I was confused as to why useEffect only runs when the count variable changes, and not on every render.
Understanding: The array [count] passed as the second argument to useEffect is a list of dependencies. This tells useEffect to re-run only when count changes. Without this array, useEffect would run on every render.


### Example 2:

<button onClick={() => handleClick()}>Click Me</button>

Confusion: I didn't understand why the arrow function was necessary here instead of just passing handleClick directly.
Understanding: The arrow function () => handleClick() is used to create a new function on every render. This is important if the function requires arguments or if you want to delay the function call until the button is clicked. If you simply use handleClick, it would be called immediately upon rendering.

### Example 3:

const items = ['Item1', 'Item2', 'Item3'];
items.map((item) => {
  console.log(item);
});
Confusion: I was confused about what the map() method actually does compared to forEach().
Understanding: The map() method is used to iterate over an array and returns a new array with the results of calling a provided function on every element. In contrast, forEach() simply iterates without returning anything, which makes map() more useful when transforming data.

### Example 4: 'setState' with Previous State
const [count, setCount] = useState(0);
const increment = () => {
  setCount(prevCount => prevCount + 1);
};
Confusion: Initially, I did not understand the prevCount argument in the setCount function.
Understanding: When using setState, it’s important to access the previous state if the new state depends on it. This ensures that state updates correctly, especially when updates are asynchronous.

### Example 5: Conditional Rendering with Ternary Operator
return (
  <div>
    {isLoggedIn ? <Dashboard /> : <LoginPage />}
  </div>
);
Confusion: I was unsure how the ternary operator worked within JSX to conditionally render components.
Understanding: The ternary operator allows for concise conditional rendering in JSX. If isLoggedIn is true, it renders the Dashboard component; otherwise, it renders the LoginPage.