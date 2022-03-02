function validatePassword() {
    const new_email = document.getElementById("email")
    const password = document.getElementById("password");
    const confirm_password = document.getElementById("confirm_password");

    console.log(new_email.value);
    console.log(password.value);
    console.log(confirm_password.value);

    if (password.value == confirm_password.value) {
        console.log("password accepted");
    } else {
        console.log("passwords do not match");
    }
    
}