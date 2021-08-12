const btnMobile = document.getElementById('btn-mobile');

function toggleMenu(){
    const nav = document.getElementById('nav-list');
    nav.classList.toggle('active')
}

btnMobile.addEventListener('click', toggleMenu);