function validateSignIn() {
    const username = document.getElementById("username");
    const password = document.getElementById("password");
    const remember = document.getElementById("remember");


    console.log(username.value);
    console.log(password.value);
    console.log(remember.value);
}

async function transition() {
    const input = document.getElementById("input");
    input.classList.add('animate__animated', 'animate__fadeOut');
    setTimeout(() => {
        input.classList.remove('animate__animated', 'animate__fadeOut');
     }, 540);
    
}