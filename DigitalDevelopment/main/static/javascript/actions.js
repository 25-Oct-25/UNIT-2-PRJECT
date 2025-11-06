
const navLinks =document.getElementById('navLinks');
const links = navLinks.querySelectorAll('a');

function closeNav()
{
    navLinks.classList.remove('active');
    menuToggle,innerHTML = '&#9776;';
    menuToggle.setAttribute('aria-label', 'Open navigation menu');
}

links.forEach(link => {
    link.addEventListener('click',function()
{
    closeNav();
});
});

//----------------------------------------------//
const menuToggle = document.getElementById('menuToggle');
//Open icon
const iconOpen = '&#9776;';
//Close icon
const iconClose = '&#10005;';

function updateToggleIcon()
{
    if (navLinks.classList.contains('active'))
    {
        menuToggle.innerHTML = iconClose;
        menuToggle.setAttribute('aria-label','Close navigation menu');
    }
    else
    {
        menuToggle.innerHTML = iconOpen;
        menuToggle.setAttribute('aria-label','Open navigation menu');
    }
}

//----------------------------------------------------//
menuToggle.addEventListener('click', function()
{
    navLinks.classList.toggle('active');
    updateToggleIcon();
});

links.forEach(link=> {
    link.addEventListener('click', function()
{
    navLinks.classList.remove('active');
    updateToggleIcon();
});
});
