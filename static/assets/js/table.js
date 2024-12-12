const examples = {
    1: [
      { source: "Pyramid", target: "Bean", meanDiff: "2.68", tStat: "11.53", pValue: "1.61e-29" },
      { source: "Theatre", target: "Zebra", meanDiff: "2.74", tStat: "14.54", pValue: "3.41e-45" },
    ],
    2: [
      { source: "Asteroid", target: "Viking", meanDiff: "2.48", tStat: "13.85", pValue: "1.60e-40" },
      { source: "Brain", target: "Telephone", meanDiff: "2.89", tStat: "18.76", pValue: "2.70e-72" },
    ],
    3: [
      { source: "Sun", target: "Moon", meanDiff: "1.58", tStat: "9.24", pValue: "2.30e-20" },
      { source: "Ocean", target: "River", meanDiff: "3.02", tStat: "15.67", pValue: "5.67e-50" },
    ],
  };
  
  function showExample(exampleNumber) {
    const tbody = document.querySelector("#dynamicTable tbody");
    tbody.innerHTML = ""; // Clear existing rows
  
    const rows = examples[exampleNumber];
    rows.forEach((row) => {
      const tr = document.createElement("tr");
      tr.innerHTML = `
        <td style="border: 1px solid #ddd; padding: 8px;">${row.source}</td>
        <td style="border: 1px solid #ddd; padding: 8px;">${row.target}</td>
        <td style="border: 1px solid #ddd; padding: 8px;">${row.meanDiff}</td>
        <td style="border: 1px solid #ddd; padding: 8px;">${row.tStat}</td>
        <td style="border: 1px solid #ddd; padding: 8px;">${row.pValue}</td>
      `;
      tbody.appendChild(tr);
    });
  }
  
  // Show the first example by default
  document.addEventListener("DOMContentLoaded", () => {
    showExample(1);
  });
  