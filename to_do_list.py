import tkinter as tk
from tkinter import messagebox
import os

# Função para adicionar uma nova tarefa com descrição
def add_task():
    task = task_entry.get()
    description = description_entry.get()
    if task != "":
        if description != "":
            task = f"{task} - {description}"
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        description_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Você deve digitar uma tarefa.")

# Função para remover a tarefa selecionada
def delete_task():
    try:
        task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(task_index)
    except:
        messagebox.showwarning("Aviso", "Você deve selecionar uma tarefa para remover.")

# Função para carregar tarefas de um arquivo
def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                tasks_listbox.insert(tk.END, task.strip())

# Função para salvar tarefas em um arquivo
def save_tasks():
    tasks = tasks_listbox.get(0, tasks_listbox.size())
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Função para marcar uma tarefa como concluída
def mark_task_completed():
    try:
        task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(task_index)
        if not task.endswith(" ✔"):
            task += " ✔"
            tasks_listbox.delete(task_index)
            tasks_listbox.insert(task_index, task)
    except:
        messagebox.showwarning("Aviso", "Você deve selecionar uma tarefa para marcar como concluída.")

# Função para desmarcar uma tarefa como não concluída
def unmark_task_completed():
    try:
        task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(task_index)
        if task.endswith(" ✔"):
            task = task[:-2]
            tasks_listbox.delete(task_index)
            tasks_listbox.insert(task_index, task)
    except:
        messagebox.showwarning("Aviso", "Você deve selecionar uma tarefa para desmarcar como concluída.")

# Criar a janela principal
window = tk.Tk()
window.title("Lista de Tarefas")

# Configurar a geometria da janela
window.geometry("700x600")
window.configure(bg="#f0f0f0")  # Cor de fundo da janela

# Criar um título
title_label = tk.Label(window, text="Gerenciador de Tarefas", font=("Poppins", 30, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Criar frame para a entrada de nova tarefa
frame_entry = tk.Frame(window, bg="#f0f0f0")
frame_entry.pack(pady=10)

# Criar uma caixa de entrada para adicionar novas tarefas
task_entry = tk.Entry(frame_entry, width=30, font=("Poppins", 12))
task_entry.pack(side=tk.LEFT, padx=10)

# Criar uma caixa de entrada para adicionar a descrição da tarefa
description_entry = tk.Entry(frame_entry, width=30, font=("Poppins", 12))
description_entry.pack(side=tk.LEFT, padx=10)

# Botão para adicionar a nova tarefa
add_task_button = tk.Button(frame_entry, text="Adicionar Tarefa", command=add_task, bg="#5a78ff", fg="white", font=("Poppins", 12))
add_task_button.pack(side=tk.LEFT)

# Criar frame para a lista de tarefas
frame_tasks = tk.Frame(window, bg="#f0f0f0")
frame_tasks.pack(pady=10)

# Barra de rolagem para a lista de tarefas
scrollbar = tk.Scrollbar(frame_tasks, bg="#f0f0f0")
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Lista de tarefas
tasks_listbox = tk.Listbox(frame_tasks, height=10, width=80, yscrollcommand=scrollbar.set, selectmode=tk.SINGLE, font=("Poppins", 12))
tasks_listbox.pack()

# Configurar a barra de rolagem
scrollbar.config(command=tasks_listbox.yview)

# Criar frame para os botões de ação
frame_buttons = tk.Frame(window, bg="#f0f0f0")
frame_buttons.pack(pady=10)

# Botão para remover a tarefa selecionada
delete_task_button = tk.Button(frame_buttons, text="Remover Tarefa", command=delete_task, bg="#f44336", fg="white", font=("Poppins", 12))
delete_task_button.pack(side=tk.LEFT, padx=5)

# Botão para marcar a tarefa como concluída
mark_task_completed_button = tk.Button(frame_buttons, text="Concluir Tarefa", command=mark_task_completed, bg="#2196F3", fg="white", font=("Poppins", 12))
mark_task_completed_button.pack(side=tk.LEFT, padx=5)

# Botão para desmarcar a tarefa como concluída
unmark_task_completed_button = tk.Button(frame_buttons, text="Desmarcar Tarefa", command=unmark_task_completed, bg="#FFC107", fg="black", font=("Poppins", 12))
unmark_task_completed_button.pack(side=tk.LEFT, padx=5)

# Carregar as tarefas quando o programa é iniciado
load_tasks()

# Salvar as tarefas quando o programa é fechado
window.protocol("WM_DELETE_WINDOW", lambda: [save_tasks(), window.destroy()])

# Iniciar o loop principal
window.mainloop()
