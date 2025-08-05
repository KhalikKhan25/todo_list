# To-Do List Application

A simple console-based To-Do List manager built in Python that allows you to manage your daily tasks efficiently with persistent storage.

## Features

- ✅ **Add Tasks**: Add new tasks to your to-do list
- 👀 **View Tasks**: Display all current tasks with numbering
- ❌ **Remove Tasks**: Remove tasks by number or by searching name
- 📍 **Insert Tasks**: Insert tasks at specific positions
- 🗑️ **Clear All**: Remove all tasks at once
- 💾 **Persistent Storage**: Tasks are automatically saved to a text file
- 🔄 **Auto-load**: Previously saved tasks are loaded when you start the app

## Installation & Usage

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd todo-list-app
   ```

2. **Run the application**:
   ```bash
   python todo.py
   ```

3. **Follow the menu prompts** to manage your tasks!

## How It Works

### File Structure
- `todo.py` - Main application file
- `tasks.txt` - Automatically created file to store your tasks
- `README.md` - This documentation

### Core Functionality

The application uses several key Python concepts:

#### File Handling
- Uses `open()` with context managers (`with` statement)
- Automatically creates `tasks.txt` if it doesn't exist
- Reads tasks line by line using file iteration
- Saves tasks persistently between sessions

#### List Operations
- `append()` - Add tasks to the end of the list
- `insert()` - Add tasks at specific positions
- `pop()` - Remove tasks by index
- `clear()` - Remove all tasks

#### String Manipulation
- `.strip()` - Remove whitespace and newlines from input
- String searching for task removal by name

## Menu Options

1. **View all tasks** - Shows numbered list of all current tasks
2. **Add a new task** - Prompts for task input and adds to list
3. **Remove task by number** - Select task number to remove
4. **Remove task by name** - Search and remove tasks by name/keyword
5. **Insert task at position** - Add task at specific position in list
6. **Clear all tasks** - Remove all tasks (with confirmation)
7. **Exit** - Close the application

## Technical Implementation

### Key Python Concepts Used

- **Lists**: Dynamic storage of tasks
- **File I/O**: Reading from and writing to text files
- **Exception Handling**: Graceful error handling for file operations
- **Context Managers**: Safe file handling with `with` statements
- **String Methods**: Text processing and validation
- **Classes**: Object-oriented design for better code organization

### File Modes Used
- `'r'` - Read mode for loading existing tasks
- `'w'` - Write mode for saving tasks

## Example Usage

```
Welcome to To-Do List Manager!
Loaded 3 tasks from tasks.txt

========================================
       TO-DO LIST MANAGER
========================================
1. View all tasks
2. Add a new task
3. Remove task by number
4. Remove task by name
5. Insert task at position
6. Clear all tasks
7. Exit
========================================

Enter your choice (1-7): 1

--- Your To-Do List ---
1. Buy groceries
2. Complete Python assignment
3. Call dentist

Total tasks: 3
```

## Error Handling

The application handles various error scenarios:
- File not found (creates new file)
- Invalid user input (prompts for correct input)
- Empty tasks (prevents adding empty tasks)
- Invalid task numbers (validates range)

## Requirements

- Python 3.x
- No external libraries required (uses only built-in modules)

## Contributing

Feel free to fork this project and submit pull requests for improvements!

## Author
Khalik Khan
Created as part of Python Developer Internship Task 2

---

**Key Learning Outcomes:**
- File handling in Python
- List manipulation and methods
- String processing techniques
- Exception handling
- Object-oriented programming basics
- User input validation
