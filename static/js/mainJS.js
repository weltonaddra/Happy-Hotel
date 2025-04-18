
  document.addEventListener("DOMContentLoaded", () => {
    fetch("/api/reservations")
      .then(response => response.json())
      .then(data => {
        const container = document.getElementById("reservation-list");
        
        data.forEach(res => {
          const item = document.createElement("div");
          item.classList.add("reservation-card");
          item.innerHTML = `
            <h4>${res.guest_name}</h4>
            <p>Room: ${res.room}</p>
            <p>Check-in: ${res.checkin}</p>
            <p>Check-out: ${res.checkout}</p>
          `;
          container.appendChild(item);
        });
      })
      .catch(error => console.error("Error loading reservations:", error));
  });
