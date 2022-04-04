function reset() {
    const email = document.getElementById("email");

    console.log(email.value);
}

window.addEventListener('popstate', function() {
    console.log("o yeaaa");
});