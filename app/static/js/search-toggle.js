document.addEventListener("DOMContentLoaded", function(){
    const searchInput = document.getElementById('searchInput');
    const searchForm = document.getElementById('searchForm');
    const toggleBtn = document.getElementById('searchToggle');
    const overlay = document.getElementById('mobileSearchOverlay');
    const closeOverlay = document.getElementById('closeSearchOverlay');
    const overlayInput = overlay?.querySelector('input[type="search"]');
    const overlayForm = overlay?.querySelector('form');

    // Desktop behavior
    toggleBtn?.addEventListener('click', function() {
        if (window.innerWidth<=768) {
        // Mobile : affiche overlay
        overlay.classList.remove('d-none');
        overlayInput?.focus();
        } else {
        // Destop : comportement classique
        if (searchInput.classList.contains('d-none')) {
            searchInput.classList.remove('d-none');
            searchInput.focus();
        } else if (searchInput.value.trim() !== "") {
            searchForm.submit();
        }
      }
    });
    // Fermer l'overlay
    closeOverlay?.addEventListener("click", function (e) {
        overlay.classList.add('d-none');
        overlayInput.value = "";
    });

    // Prevent empty desktop search submit
    searchForm?.addEventListener('submit', function (e) {
        if (searchInput.value.trim() === "") {
        e.preventDefault();
        }
    });
    // Prevent empty mobile overlay submit
    overlayForm?.addEventListener('submit', function (e) {
        if (overlayInput.value.trim() === "") {
        e.preventDefault();
        }
    });

    // fermer le champ si click ailleurs (desktop uniquement)
    document.addEventListener("click", function (e) {
        if (window.innerWidth>768) {
            const isClickInside = searchForm.contains(e.target);
            if (!isClickInside) {
                searchInput.classList.add("d-none");
                searchInput.value = "";
            }
        }
    });
}); 
