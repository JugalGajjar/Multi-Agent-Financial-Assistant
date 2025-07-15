const chatHistory = document.getElementById("chat-history");
const queryForm = document.getElementById("query-form");
const queryInput = document.getElementById("query");
const themeToggle = document.getElementById("theme-toggle");

// === Load theme from localStorage on page load ===
document.addEventListener("DOMContentLoaded", () => {
    const isDark = localStorage.getItem("theme") === "dark";
    document.body.classList.toggle("dark-mode", isDark);
    themeToggle.textContent = isDark ? "☀️ Light Mode" : "🌙 Dark Mode";
});

// === Handle form submit ===
queryForm.addEventListener("submit", async function (e) {
    e.preventDefault();
    const query = queryInput.value.trim();
    if (!query) return;

    // Show user message
    const userMsg = document.createElement("div");
    userMsg.innerHTML = `<strong>You:</strong> ${query}`;
    chatHistory.appendChild(userMsg);

    // Clear input
    queryInput.value = "";

    // Show placeholder agent message
    const agentMsg = document.createElement("div");
    agentMsg.innerHTML = `<em>Processing...</em>`;
    chatHistory.appendChild(agentMsg);

    try {
        const response = await fetch("/query", {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query })
        });

        const data = await response.json();

        // Render Markdown to HTML using marked.js
        const html = marked.parse(data.response);
        agentMsg.innerHTML = `<strong>Agent:</strong><div class="md-output">${html}</div>`;

        // Scroll to bottom
        chatHistory.scrollTop = chatHistory.scrollHeight;
    } catch (err) {
        agentMsg.innerHTML = `<strong>Agent:</strong> <em>Something went wrong. Please try again.</em>`;
    }
});

// === Theme toggle ===
themeToggle.addEventListener("click", () => {
    const isDarkMode = document.body.classList.toggle("dark-mode");
    localStorage.setItem("theme", isDarkMode ? "dark" : "light");
    themeToggle.textContent = isDarkMode ? "☀️ Light Mode" : "🌙 Dark Mode";
});
