function validatePassword() {
    const email = document.getElementById("email");
    const password = document.getElementById("password");
    const confirm = document.getElementById("confirm");

    console.log(email.value);

    if (password.value == confirm.value) { 
        console.log("Password accepted");
        window.location.replace("../corsairDirectory/corsair-directory.html");
    } else {
        console.log("Reenter password");
    }
    
}