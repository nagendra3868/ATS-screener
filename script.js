// =============================
// Smart ATS
// =============================

const resumeInput = document.getElementById("resumeFile");
const chooseBtn = document.getElementById("chooseBtn");
const fileName = document.getElementById("fileName");

const analyzeBtn = document.getElementById("analyzeBtn");
const roleSelect = document.getElementById("roleSelect");

const scoreValue = document.getElementById("scoreValue");
const rating = document.getElementById("rating");

const matchedList = document.getElementById("matchedList");
const missingList = document.getElementById("missingList");


// ------------------------------
// Choose Resume
// ------------------------------

chooseBtn.addEventListener("click", () => {

    resumeInput.click();

});

resumeInput.addEventListener("change", () => {

    if (resumeInput.files.length === 0) {

        fileName.textContent = "No file selected";

        return;

    }

    const file = resumeInput.files[0];

    fileName.innerHTML = `
        <strong>${file.name}</strong><br>
        ${(file.size / 1024).toFixed(2)} KB
    `;

});


// ------------------------------
// Analyze Resume
// ------------------------------

analyzeBtn.addEventListener("click", async () => {

    if (resumeInput.files.length === 0) {

        alert("Please upload a resume.");

        return;

    }

    if (!roleSelect.value) {

        alert("Please select a role.");

        return;

    }

    const formData = new FormData();

    formData.append("resume", resumeInput.files[0]);
    formData.append("role", roleSelect.value);

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/analyze",
            {
                method: "POST",
                body: formData
            }
        );

        const data = await response.json();

        console.log(data);

        updateScore(data.score);

        rating.textContent = data.rating;

        showKeywords(
            data.matched_keywords,
            matchedList
        );

        showKeywords(
            data.missing_keywords,
            missingList
        );

    }

    catch (error) {

        console.error(error);

        alert("Unable to connect to Flask Backend.");

    }

});


// ------------------------------
// Score Animation
// ------------------------------

function updateScore(score) {

    scoreValue.textContent = score + "%";

}


// ------------------------------
// Keywords
// ------------------------------

function showKeywords(list, element) {

    element.innerHTML = "";

    list.forEach(skill => {

        const li = document.createElement("li");

        li.textContent = skill;

        element.appendChild(li);

    });

}
// Dark Mode Toggle
const themeToggle = document.getElementById("themeToggle");

if (localStorage.getItem("theme") === "dark") {
    document.body.classList.add("dark-mode");
    themeToggle.innerHTML = '<i class="fa-solid fa-sun"></i>';
}

themeToggle.addEventListener("click", () => {

    document.body.classList.toggle("dark-mode");

    if (document.body.classList.contains("dark-mode")) {
        localStorage.setItem("theme", "dark");
        themeToggle.innerHTML = '<i class="fa-solid fa-sun"></i>';
    } else {
        localStorage.setItem("theme", "light");
        themeToggle.innerHTML = '<i class="fa-solid fa-moon"></i>';
    }

});