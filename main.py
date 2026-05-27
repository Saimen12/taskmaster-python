import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title('TaskMaster - Organizador de Estudos')
        self.root.geometry('700x500')
        self.root.config(bg='#111827')

        self.tasks = []

        title = tk.Label(
            root,
            text='TaskMaster',
            font=('Arial', 26, 'bold'),
            bg='#111827',
            fg='white'
        )
        title.pack(pady=15)

        subtitle = tk.Label(
            root,
            text='Organize seus estudos e projetos de tecnologia',
            font=('Arial', 12),
            bg='#111827',
            fg='#9CA3AF'
        )
        subtitle.pack()

        self.task_entry = tk.Entry(
            root,
            font=('Arial', 14),
            width=40,
            bg='#1F2937',
            fg='white',
            insertbackground='white',
            relief='flat'
        )
        self.task_entry.pack(pady=20, ipady=8)

        add_button = tk.Button(
            root,
            text='Adicionar Tarefa',
            command=self.add_task,
            bg='#2563EB',
            fg='white',
            font=('Arial', 12, 'bold'),
            relief='flat',
            padx=20,
            pady=10,
            cursor='hand2'
        )
        add_button.pack()

        self.task_listbox = tk.Listbox(
            root,
            width=60,
            height=12,
            font=('Arial', 12),
            bg='#1F2937',
            fg='white',
            selectbackground='#2563EB',
            relief='flat'
        )
        self.task_listbox.pack(pady=25)

        button_frame = tk.Frame(root, bg='#111827')
        button_frame.pack()

        complete_button = tk.Button(
            button_frame,
            text='Concluir',
            command=self.complete_task,
            bg='#10B981',
            fg='white',
            font=('Arial', 11, 'bold'),
            relief='flat',
            padx=18,
            pady=8,
            cursor='hand2'
        )
        complete_button.grid(row=0, column=0, padx=10)

        delete_button = tk.Button(
            button_frame,
            text='Excluir',
            command=self.delete_task,
            bg='#EF4444',
            fg='white',
            font=('Arial', 11, 'bold'),
            relief='flat',
            padx=18,
            pady=8,
            cursor='hand2'
        )
        delete_button.grid(row=0, column=1, padx=10)

        self.status_label = tk.Label(
            root,
            text='0 tarefas adicionadas',
            font=('Arial', 11),
            bg='#111827',
            fg='#9CA3AF'
        )
        self.status_label.pack(pady=15)

    def update_status(self):
        total = len(self.tasks)
        self.status_label.config(text=f'{total} tarefas adicionadas')

    def add_task(self):
        task = self.task_entry.get().strip()

        if task == '':
            messagebox.showwarning('Aviso', 'Digite uma tarefa!')
            return

        current_time = datetime.now().strftime('%d/%m %H:%M')
        formatted_task = f'📚 {task}  |  {current_time}'

        self.tasks.append(formatted_task)
        self.task_listbox.insert(tk.END, formatted_task)
        self.task_entry.delete(0, tk.END)

        self.update_status()

    def complete_task(self):
        try:
            selected = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected)

            self.task_listbox.delete(selected)
            self.task_listbox.insert(selected, f'✅ {task}')

        except:
            messagebox.showwarning('Aviso', 'Selecione uma tarefa!')

    def delete_task(self):
        try:
            selected = self.task_listbox.curselection()[0]

            self.task_listbox.delete(selected)
            del self.tasks[selected]

            self.update_status()

        except:
            messagebox.showwarning('Aviso', 'Selecione uma tarefa!')


if __name__ == '__main__':
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
   