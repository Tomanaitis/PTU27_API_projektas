// JAVASCRIPT KODAS DINAMIŠKAI GENERUOTI LENTELĘ SU DUOMENIMIS
document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/automobiliai')
        .then(response => response.json())
        .then(data => {
            const tbody = document.getElementById('automobiliai-body');
            tbody.innerHTML = '';

            data.forEach(auto => {
                const tr = document.createElement('tr');

                tr.innerHTML = `
                    <td>${auto.id}</td>
                    <td>${auto.gamintojas}</td>
                    <td>${auto.modelis}</td>
                    <td>${auto.spalva}</td>
                    <td>${auto.kaina}</td>
                `;

                tbody.appendChild(tr);
            });
        })
        .catch(error => console.error('Error fetching data:', error));
});

