// Seleziona il form HTML
const queryForm = document.getElementById('queryForm');

// Aggiungi un evento di submit al form
queryForm.addEventListener('submit', (event) => {
  event.preventDefault();

  // Ottieni i valori dei campi del form
  const name = queryForm.elements['name'].value;
  const surname = queryForm.elements['surname'].value;

  // Esegui una richiesta AJAX al server Flask per ottenere i risultati della query
  fetch(`/query_name_surname/${name}/${surname}`)
    .then((response) => response.json())
    .then((data) => {
      // Mostra i risultati della query nella pagina
      const queryResults = document.getElementById('queryResults');
      queryResults.innerHTML = '';

      if (data.length === 0) {
        queryResults.innerHTML = '<p>No results found.</p>';
      } else {
        data.forEach((player) => {
          const playerInfo = document.createElement('p');
          playerInfo.textContent = `${player.name} ${player.surname} - Team: ${player.team}, Points: ${player.pts}`;
          queryResults.appendChild(playerInfo);
        });
      }
    })
    .catch((error) => console.error('Error:', error));
});

// Function to show/hide the query input groups based on the selected query
function showHideQueryInputs(selectedQuery) {
  const queryGroups = document.querySelectorAll('.query-group');
  queryGroups.forEach(group => {
      if (group.classList.contains(selectedQuery)) {
          group.style.display = 'block'; // Show the selected group
      } else {
          group.style.display = 'none'; // Hide other groups
      }
  });
}

document.getElementById('queryType').addEventListener('change', function () {
  const selectedQuery = this.value;
  showHideQueryInputs(selectedQuery);
});

// Add the event listener for the initial selected value on page load
showHideQueryInputs(document.getElementById('queryType').value);