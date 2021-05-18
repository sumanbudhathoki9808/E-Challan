const overlay = document.querySelector('.logout-page-overlay');
const logout = document.querySelector('.mobile-log-out-btn');
const closeLayout = document.querySelector('.close-btn');
const no = document.querySelector('.no-logout');

logout.addEventListener('click', openLogout);
closeLayout.addEventListener('click', closeLogout);
no.addEventListener('click', closeLogout);

function openLogout(){
    overlay.style.display = "block";
}

function closeLogout(){
    overlay.style.display = "none";
}