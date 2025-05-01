document.addEventListener("DOMContentLoaded", () => {
  const dropdownToggles = document.querySelectorAll(".dropdown-toggle");

  dropdownToggles.forEach((toggle) => {
    toggle.addEventListener("click", (event) => {
      event.preventDefault();

      // Close other open dropdowns
      document.querySelectorAll(".nav-item.dropdown").forEach((item) => {
        if (item !== toggle.parentElement) {
          item.classList.remove("show");
        }
      });

      // Toggle the current dropdown
      const parent = toggle.parentElement;
      parent.classList.toggle("show");

      // Rotate the arrow
      const arrow = toggle.querySelector(".arrow");
      if (arrow) {
        arrow.classList.toggle("rotate");
      }
    });
  });

  // Close dropdowns when clicking outside
  document.addEventListener("click", (event) => {
    if (!event.target.closest(".nav-item.dropdown")) {
      document.querySelectorAll(".nav-item.dropdown").forEach((item) => {
        item.classList.remove("show");
        const arrow = item.querySelector(".arrow");
        if (arrow) {
          arrow.classList.remove("rotate");
        }
      });
    }
  });
});

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
