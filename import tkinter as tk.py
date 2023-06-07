import tkinter as tk

class LoadMonitor:
    def __init__(self, num_cores):
        self.num_cores = num_cores
        self.core_loads = [0] * num_cores

        self.root = tk.Tk()
        self.root.title("Load Monitor")

        self.load_labels = []
        self.load_entries = []

        for i in range(num_cores):
            label = tk.Label(self.root, text=f"Core {i+1} Load:")
            label.grid(row=i, column=0, padx=10, pady=5)
            self.load_labels.append(label)

            entry = tk.Entry(self.root, width=10)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.load_entries.append(entry)

        increase_button = tk.Button(self.root, text="Increase Load", command=self.increase_loads)
        increase_button.grid(row=num_cores, column=0, padx=10, pady=5)

        reset_button = tk.Button(self.root, text="Reset Loads", command=self.reset_loads)
        reset_button.grid(row=num_cores, column=1, padx=10, pady=5)

    def increase_loads(self):
        for i in range(self.num_cores):
            try:
                increase_percentage = int(self.load_entries[i].get())
                self.core_loads[i] += increase_percentage
                self.load_entries[i].delete(0, tk.END)
                self.load_entries[i].insert(0, str(self.core_loads[i]))
            except ValueError:
                pass

    def reset_loads(self):
        for i in range(self.num_cores):
            self.core_loads[i] = 0
            self.load_entries[i].delete(0, tk.END)
            self.load_entries[i].insert(0, "0")

    def run(self):
        self.root.mainloop()
        

num_cores = 4  # تعداد هسته‌های پردازشی را در اینجا تغییر دهید
monitor = LoadMonitor(num_cores)
monitor.run()