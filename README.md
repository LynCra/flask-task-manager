# Flask Task Manager

A simple task management web application built with Flask.

## Features

- Add, edit, and delete tasks
- View all tasks in a list
- Simple and user-friendly interface

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/LynCra/flask-task-manager.git
    cd flask-task-manager
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**
    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

5. **Run the application:**
    ```bash
    flask run
    ```

## Usage

1. Open your web browser and go to `http://127.0.0.1:5000/`
2. Use the interface to add, edit, or delete tasks.

## Contributing

Contributions are welcome! Please submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
