document.getElementById('load-items').addEventListener('click', function() {
  fetch('{% url "get-items" %}')
    .then(response => response.json())
    .then(data => {
      const container = document.getElementById('items-container');
      container.innerHTML = '';
      data.forEach(item => {
        const itemElement = document.createElement('div');
        itemElement.textContent = item.name;
        container.appendChild(itemElement);
      });
    })
    .catch(error => console.error(error));
});
