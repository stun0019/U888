const API_BASE = "https://www.thesportsdb.com/api/v1/json/3";
let matches = [];

document.addEventListener("DOMContentLoaded", () => {
    init();
});

async function init() {
    setTodayDate();
    await loadMatches();
    bindEvents();
}

function setTodayDate() {
    const today = new Date();
    const taipei = new Date(today.toLocaleString("en-US", { timeZone: "Asia/Taipei" }));
    document.getElementById("dateFilter").value = taipei.toISOString().split("T")[0];
}

async function loadMatches() {
    try {
        const res = await fetch(`${API_BASE}/eventsnextleague.php?id=4328`);
        const data = await res.json();

        matches = (data.events || []).map(e => ({
            sport: "soccer",
            league: e.strLeague,
            home: e.strHomeTeam,
            away: e.strAwayTeam,
            time: convertTime(e.dateEvent, e.strTime),
            status: "upcoming",
            homeScore: null,
            awayScore: null
        }));

        document.getElementById("loading").style.display = "none";
        document.getElementById("matchTable").style.display = "table";

        render();

    } catch (err) {
        document.getElementById("loading").innerText = "API load failed";
    }
}

function convertTime(date, time) {
    return new Date(`${date}T${time || "00:00:00"}Z`);
}

function bindEvents() {
    document.getElementById("sportFilter").addEventListener("change", render);
    document.getElementById("statusFilter").addEventListener("change", render);
    document.getElementById("dateFilter").addEventListener("change", render);
}

function render() {
    const sport = document.getElementById("sportFilter").value;
    const status = document.getElementById("statusFilter").value;
    const date = document.getElementById("dateFilter").value;

    const body = document.getElementById("matchBody");
    body.innerHTML = "";

    let filtered = matches.filter(m => {

        if (sport !== "all" && m.sport !== sport) return false;

        if (status !== "all" && m.status !== status) return false;

        const matchDate = m.time.toISOString().split("T")[0];
        if (matchDate !== date) return false;

        return true;
    });

    filtered.forEach(m => {

        const tr = document.createElement("tr");

        tr.innerHTML = `
            <td>${m.league}</td>
            <td>${m.home} vs ${m.away}</td>
            <td>${m.time.toLocaleString("zh-TW", { timeZone: "Asia/Taipei" })}</td>
            <td><span class="status-upcoming">${m.status}</span></td>
        `;

        body.appendChild(tr);
    });

    if (filtered.length === 0) {
        body.innerHTML = `<tr><td colspan="4">No data</td></tr>`;
    }
}
