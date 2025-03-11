document.addEventListener('DOMContentLoaded', function() {
    fetch('scraped_data.csv')
        .then(response => response.text())
        .then(data => {
            const rows = data.split('\n').slice(1);
            const gallery = document.getElementById('gallery');
            rows.forEach(row => {
                const cols = row.split(';');
                if (cols.length < 4) return;
                const title = cols[0].replace(/"/g, '');
                const description = cols[1].replace(/"/g, '');
                const link = cols[2].replace(/"/g, '');
                const imagePath = `./images/${cols[3].replace(/"/g, '').split('/').pop()}`;

                const item = document.createElement('div');
                item.className = 'gallery-item';
                item.innerHTML = `
                    <a href="${link}" target="_blank">
                        <img src="${imagePath}" alt="${title}">
                    </a>
                    <h3>${title}</h3>
                    <p>${description}</p>
                `;
                gallery.appendChild(item);
            });
        });
});
