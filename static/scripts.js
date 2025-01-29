// JAVASCRIPT KODAS DINAMIŠKAI GENERUOTI LENTELĘ SU DUOMENIMIS
document.addEventListener('DOMContentLoaded', function() {
    fetch('/api2/projektai')
        .then(response => response.json())
        .then(data => {
            const tbody = document.getElementById('projektai-body');
            tbody.innerHTML = '';

            data.forEach(projektas => {
                const tr = document.createElement('tr');

                tr.innerHTML = `
                    <td>${projektas.id}</td>
                    <td>${projektas.pavadinimas}</td>
                    <td>${projektas.kaina}</td>
                    <td>${projektas.sukurimo_data}</td>
                `;

                tbody.appendChild(tr);
            });
        })
        .catch(error => console.error('Error fetching data:', error));
});

