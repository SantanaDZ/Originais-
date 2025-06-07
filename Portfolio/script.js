const botaoModo = document.getElementById("modo-toggle");
botaoModo.addEventListener("click", () => {
    document.body.classList.toggle("dark-mode");
    botaoModo.textContent = document.body.classList.contains("dark-mode") ? "☀️" : "🌙";
});
