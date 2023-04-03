async function submitData() {
    event.preventDefault() // Evita que a página seja recarregada

    // Envia os dados do formulário para o servidor em JSON
    const response = await fetch('http://127.0.0.1:5000/api/position', {
        method: 'POST',
        body: JSON.stringify({
            x: document.getElementById('x').value,
            y: document.getElementById('y').value,
            z: document.getElementById('z').value,
            r: document.getElementById('r').value,
            j1: document.getElementById('j1').value,
            j2: document.getElementById('j2').value,
            j3: document.getElementById('j3').value,
            j4: document.getElementById('j4').value
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    });
    const responseJson = await response.json();
    console.log(responseJson); // Exibe o resultado no console

    // Limpa os campos do formulário
    document.getElementById('x').value = ''
    document.getElementById('y').value = ''
    document.getElementById('z').value = ''
    document.getElementById('r').value = ''
    document.getElementById('j1').value = ''
    document.getElementById('j2').value = ''
    document.getElementById('j3').value = ''
    document.getElementById('j4').value = ''
}
function fetchDataAndAddToTable() {
    // Get the table element
    const table = document.getElementById("table");

    // Fetch the JSON data
    fetch("http://127.0.0.1:5000/api/position")
        .then(response => response.json())
        .then(data => {
            console.log(data)
            clearTable()
            // Loop through the data and add new rows to the table
            data.positions.forEach(item => {
                // Create a new row
                const row = table.insertRow();

                // Add the data to the row
                row.insertCell().textContent = item.x;
                row.insertCell().textContent = item.y;
                row.insertCell().textContent = item.r;
                row.insertCell().textContent = item.z;
                row.insertCell().textContent = item.j1;
                row.insertCell().textContent = item.j2;
                row.insertCell().textContent = item.j3;
                row.insertCell().textContent = item.j4;
            });
        });
}
function clearTable() {
    // Get the table element
    const table = document.getElementById("table");
    // Keep the first row (which should contain the th elements)
    const thRow = table.rows[0];
    table.innerHTML = '';
    table.appendChild(thRow);

    // Remove all other rows
    while (table.rows.length > 1) {
        table.deleteRow(1);
    }
}

// Call the function every second
setInterval(fetchDataAndAddToTable, 1000);