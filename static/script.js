document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("searchForm");
  const resultsDiv = document.getElementById("results");

  if (form) {
    form.addEventListener("submit", async (e) => {
      e.preventDefault();

      const formData = new FormData(form);
      const res = await fetch("/search", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();
      const rows = data.results;

      if (!rows || rows.length === 0) {
        resultsDiv.innerHTML = "<p>No results found. Try SQL injection 😉</p>";
        return;
      }

      const keys = Object.keys(rows[0]);
      let table = "<table><tr>";
      keys.forEach((key) => {
        table += `<th>${key}</th>`;
      });
      table += "</tr>";

      rows.forEach((row) => {
        table += "<tr>";
        keys.forEach((key) => {
          table += `<td>${row[key] ?? ""}</td>`;
        });
        table += "</tr>";
      });

      table += "</table>";
      resultsDiv.innerHTML = table;
    });
  }
});
