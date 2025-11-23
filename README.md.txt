A lightweight tool for students and teachers to track academic performance. Load multiple CSVs, view scores, attendance, study hours, and get instant insights with tabbed charts and alerts. Built with Tkinter, Pandas, and Matplotlib, this app provides a clean interface to explore student data, generate performance analytics, and visualize correlations between study habits and results. The app highlights important insights such as low attendance or study hours, and provides tabbed visualizations that reveal trends across subjects, study habits, and test scores. Simple to set up and lightweight to run, this tool is aimed at students, teachers, and classrooms that want a quick, reproducible way to track performance and identify areas for improvement.

Tech Stack Used Python 3.x → Core programming language Tkinter → GUI framework for building the desktop interface Pandas → Data handling and analysis (loading CSVs, calculating averages, pass rates) NumPy → Numerical operations and efficient data structures Matplotlib → Data visualization (bar charts, line plots, tabbed graphs) OS (Python standard library) → File handling and directory management

Features Load any number of CSV files from the data/ folder
View student data in a sortable table
Analyze class average and pass rate
Get alerts for low attendance or study hours
See visual plots for: Subject averages Attendance vs Final Score Study Hours vs Final Score Class Tests vs Final Score

Project file structure Student-Performance-Analyzer/ │ ├── main.py # Main application code (Tkinter GUI + analysis + plots) ├── requirements.txt # Dependencies (pandas, numpy, matplotlib) ├── README.md # Project documentation │ ├── recording/ # Optional folder for demo recordings or usage videos ├── screenshot/ # Screenshots to showcase the app in README/GitHub │ ├── data/ # Folder containing CSV files for analysis │ ├── classA.csv │ ├── classB.csv │ ├── classC.csv │ └── classD.csv │ └── venv/ (optional) # Virtual environment

How to Run the Application:- Follow these simple steps to run the CSV Scatter Plot Generator on your system:

Install Python Make sure Python (version 3.8 or above) is installed on your computer. You can download it from the official Python website. 2.Install Required Libraries Open Command Prompt / Terminal and run the below command: pip install pandas numpy matplotlib

Download or Copy the Project Files Save the provided Python script (scatter_plot_app.py) in a folder of your choice.

Run the Application Open Command Prompt / Terminal in the folder where the script is stored. Run the command: python scatter_plot_app.py

Upload Your CSV File A file explorer window will open. Select a valid .csv file that contains at least two numeric columns.

View Scatter Plot The application will automatically display a scatter plot graph based on selected columns from your CSV.

Close the Plot Close the plotted window after reviewing the result. You can rerun the program again to try another CSV file.

Future Improvements

Multi‑file handling Allow loading and comparing multiple CSVs side‑by‑side instead of one at a time.
Enhanced UI/UX Add themes, better navigation, and exportable charts (PNG/PDF) for reports.
Advanced analytics Include predictive modeling (e.g., regression to forecast scores based on study hours/attendance).
Interactive plots Use libraries like Plotly or Seaborn for zoomable, hover‑enabled charts.
Export options Save analysis results and plots directly to Excel or PDF for easy sharing.
Database integration Connect to SQLite/MySQL for storing student records instead of relying only on CSVs.
Role‑based features Separate dashboards for teachers (class overview) and students (individual progress).