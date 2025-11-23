import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

DATA_FOLDER = "data"

class StudentPerformanceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Performance Analyzer (Multiple CSVs + Tabbed Plots)")
        self.geometry("1000x700")
        self.data = None
        self._build_ui()
        self.refresh_csv_list()

    def _build_ui(self):
        # Top bar for CSV selection
        top = ttk.Frame(self)
        top.pack(fill="x", padx=10, pady=10)

        self.csv_var = tk.StringVar()
        self.csv_dropdown = ttk.Combobox(top, textvariable=self.csv_var, state="readonly")
        self.csv_dropdown.pack(side="left", padx=5)

        ttk.Button(top, text="Load Selected CSV", command=self.load_selected_csv).pack(side="left", padx=5)

        # Table to show data
        self.tree = ttk.Treeview(self, show="headings")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        # Output labels
        self.lbl_score = ttk.Label(self, text="Expected Final Score: -")
        self.lbl_score.pack(anchor="w", pady=5)
        self.lbl_passfail = ttk.Label(self, text="Pass/Fail Prediction: -")
        self.lbl_passfail.pack(anchor="w", pady=5)

        self.alert_box = tk.Text(self, height=6)
        self.alert_box.pack(fill="both", expand=True, pady=10)

        # Notebook for charts
        self.chart_notebook = ttk.Notebook(self)
        self.chart_notebook.pack(fill="both", expand=True, pady=10)

    def refresh_csv_list(self):
        """Refresh dropdown with all CSV files in data folder"""
        files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")]
        self.csv_dropdown["values"] = files
        if files:
            self.csv_var.set(files[0])  # default selection

    def load_selected_csv(self):
        filename = self.csv_var.get()
        if filename:
            path = os.path.join(DATA_FOLDER, filename)
            try:
                self.data = pd.read_csv(path)
                self._populate_tree()
                self.analyze_and_plot()
                messagebox.showinfo("Loaded", f"{filename} loaded successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Could not load {filename}\n{e}")

    def _populate_tree(self):
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = list(self.data.columns)
        for col in self.data.columns:
            self.tree.heading(col, text=col)
        for _, row in self.data.iterrows():
            self.tree.insert("", "end", values=list(row.values))

    def analyze_and_plot(self):
        if self.data is None: return

        # Calculate final score as average of subjects
        self.data["final_score"] = self.data[["math","science","english"]].mean(axis=1)
        avg_score = self.data["final_score"].mean()
        pass_rate = (self.data["final_score"] >= 50).mean() * 100

        self.lbl_score.config(text=f"Class Average Score: {avg_score:.1f}")
        self.lbl_passfail.config(text=f"Pass Rate: {pass_rate:.1f}%")

        # Alerts (simple class-level checks)
        alerts = []
        if self.data["attendance_pct"].mean() < 75:
            alerts.append("Overall attendance is low.")
        if self.data["study_hours_week"].mean() < 6:
            alerts.append("Average study hours are low.")
        if avg_score < 60:
            alerts.append("Class average is weak. Needs improvement.")

        self.alert_box.delete("1.0", "end")
        self.alert_box.insert("end", "\n".join(alerts) if alerts else "No alerts. Class is doing well!")

        # Draw plots in tabs
        self.draw_plots()

    def draw_plots(self):
        # Clear old tabs
        for tab in self.chart_notebook.winfo_children():
            tab.destroy()

        # Subjects Tab
        frame1 = ttk.Frame(self.chart_notebook)
        self.chart_notebook.add(frame1, text="Subjects")
        fig1, ax1 = plt.subplots(figsize=(5,4))
        subject_means = self.data[["math","science","english"]].mean()
        ax1.bar(subject_means.index, subject_means.values, color="skyblue")
        ax1.set_title("Subject Averages")
        ax1.set_ylim(0,100)
        canvas1 = FigureCanvasTkAgg(fig1, master=frame1)
        canvas1.draw()
        canvas1.get_tk_widget().pack(fill="both", expand=True)

        # Attendance Tab
        frame2 = ttk.Frame(self.chart_notebook)
        self.chart_notebook.add(frame2, text="Attendance")
        fig2, ax2 = plt.subplots(figsize=(5,4))
        ax2.scatter(self.data["attendance_pct"], self.data["final_score"], color="green")
        ax2.set_title("Attendance vs Final Score")
        ax2.set_xlabel("Attendance %")
        ax2.set_ylabel("Final Score")
        canvas2 = FigureCanvasTkAgg(fig2, master=frame2)
        canvas2.draw()
        canvas2.get_tk_widget().pack(fill="both", expand=True)

        # Study Hours Tab
        frame3 = ttk.Frame(self.chart_notebook)
        self.chart_notebook.add(frame3, text="Study Hours")
        fig3, ax3 = plt.subplots(figsize=(5,4))
        ax3.scatter(self.data["study_hours_week"], self.data["final_score"], color="purple")
        ax3.set_title("Study Hours vs Final Score")
        ax3.set_xlabel("Hours/week")
        ax3.set_ylabel("Final Score")
        canvas3 = FigureCanvasTkAgg(fig3, master=frame3)
        canvas3.draw()
        canvas3.get_tk_widget().pack(fill="both", expand=True)

        # Tests Tab
        frame4 = ttk.Frame(self.chart_notebook)
        self.chart_notebook.add(frame4, text="Tests")
        fig4, ax4 = plt.subplots(figsize=(5,4))
        ax4.scatter(self.data["class_tests_avg"], self.data["final_score"], color="orange")
        ax4.set_title("Class Tests Avg vs Final Score")
        ax4.set_xlabel("Tests Avg")
        ax4.set_ylabel("Final Score")
        canvas4 = FigureCanvasTkAgg(fig4, master=frame4)
        canvas4.draw()
        canvas4.get_tk_widget().pack(fill="both", expand=True)

if __name__ == "__main__":
    app = StudentPerformanceApp()
    app.mainloop()