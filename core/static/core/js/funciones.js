function toggleSubMenu(submenuId) {
    var allSubmenus = document.querySelectorAll('.submenu');
    allSubmenus.forEach(function(submenu) {
        if (submenu.id !== submenuId) {
            submenu.classList.remove('active');
        }
    });

    var currentSubmenu = document.getElementById(submenuId);
    currentSubmenu.classList.toggle('active');
}




