document.addEventListener("DOMContentLoaded", () => {
    const toggleDarkMode = document.getElementById("dark-mode-toggle");
    toggleDarkMode.addEventListener("click", () => {
        document.body.classList.toggle("dark-mode");
    });

    document.querySelectorAll(".fade-in").forEach(element => {
        element.classList.add("show");
    });

    const addTaskForm = document.getElementById("add-task-form");
    if (addTaskForm) {
        addTaskForm.addEventListener("submit", (e) => {
            e.preventDefault();
            const taskList = document.getElementById("task-list");
            const taskInput = document.getElementById("task-input");
            if (taskInput.value.trim() !== "") {
                const newTask = document.createElement("li");
                newTask.className = "fade-in";
                newTask.textContent = taskInput.value;
                taskList.appendChild(newTask);
                taskInput.value = "";
            }
        });
    }
});