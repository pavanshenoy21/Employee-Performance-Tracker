# Employee Performance Tracker

A desktop application for managing and tracking employee performance reviews. This tool allows organizations to record, update, and analyze employee performance metrics through an intuitive graphical interface.

## Features

- **Add Employee Records**: Record employee performance reviews with metrics for punctuality, teamwork, work quality, and communication
- **Update Records**: Modify existing employee performance data
- **Delete Records**: Remove employee records from the system
- **Search Functionality**: Search employees by ID or name
- **Automatic Average Calculation**: System automatically calculates average performance scores
- **Data Visualization**: Generate charts and visualizations of employee performance data
- **Persistent Storage**: All data is saved to CSV format for easy backup and sharing

## Performance Metrics

Each employee is evaluated on four key criteria:
- **Punctuality**: Timeliness and attendance
- **Teamwork**: Collaboration and cooperation
- **Work Quality**: Output quality and standards
- **Communication**: Effectiveness in communication

Each metric is scored, and an automatic average is calculated for overall performance assessment.

## Project Structure

- `main_gui.py`: Main GUI application built with Tkinter
- `operations.py`: Core operations for data manipulation (add, update, delete, search)
- `file_handler.py`: File I/O operations for CSV data storage
- `employee_reviews.csv`: Database file storing employee records

## Requirements

- Python 3.x
- tkinter (typically included with Python)
- matplotlib
- pandas (for CSV handling)

## Usage

Run the application:
```bash
python main_gui.py
```

### Basic Operations

1. **Add Employee**: Fill in employee details and click "Add"
2. **Search Employee**: Enter employee ID or name to search
3. **Update Performance**: Select an employee and update their metrics
4. **Delete Record**: Remove an employee from the system
5. **View Analytics**: Generate performance visualizations

## Data Storage

Employee data is stored in `employee_reviews.csv` with the following format:
- Employee ID
- Employee Name
- Punctuality Score
- Teamwork Score
- Work Quality Score
- Communication Score
- Average Performance Score