# Flask PCW Answers

## What is Flask and why is it considered a microframework?
Flask is a lightweight, minimalistic web framework for Python. It's called a microframework because it doesn’t come with built-in tools like database handling or form validation, allowing developers to add extensions based on their project needs.

## Roles of Parts in a Flask App
- **Templates:** These define the HTML structure for your app. Using Jinja2 templating, you can dynamically generate pages.
- **Static Files:** These are files like CSS, JavaScript, and images that are served directly without processing.
- **requirements.txt:** This file lists the Python dependencies for the project.
- **Virtual Environment (venv):** A Python environment isolated from the system-wide Python installations. It keeps dependencies separate.
- **render_template:** This function renders an HTML template and passes data to it.
- **redirect:** Redirects users to another URL.
- **url_for:** Generates a URL for a specific function. Useful for dynamic routing.
- **session:** Used to store user-specific data between requests.

## Flask Commands Explained
- **$ pip3 install -r requirements.txt:** Installs the dependencies listed in `requirements.txt`.
- **$ export FLASK_APP=app:** Sets the environment variable so Flask knows which file to run.
- **$ python3 -m flask run:** Starts the Flask development server.

## Flask App Running Differences
- **export FLASK_APP=app.py** and **python3 -m flask run** are used to run the app in a development environment with Flask’s built-in CLI.
- **python3 app.py** runs the script directly like any other Python file.

## Versioning in requirements.txt
Specifying versions in `requirements.txt` ensures that the correct library versions are used, preventing conflicts with newer releases. You can check library versions using `pip freeze`.

## @app.route Decorator
This decorator maps a URL to a function in the app. The default method is `GET` if not specified. It's placed right before the function definition to bind the function to a specific route.

## What is a Decorator?
A decorator in Python modifies or extends the behavior of functions. In Flask, decorators like `@app.route` map functions to routes.

## Flask Config Attribute
The config attribute stores settings for the Flask app. You can define `TESTING=True` or `SECRET_KEY='abc'` by adding these in the app’s config object.

## JSON in Flask
JSON (JavaScript Object Notation) is a lightweight data format commonly used for APIs. Flask can return JSON responses via `jsonify()`.

## Default Host and Port
The default host is `127.0.0.1` (localhost) and the port is `5000`. You can change them by running `flask run --host=<host> --port=<port>`.
