var input, input2, filter, members, card, h4, i, txtValue, txtValue1;

function Search(filter) {
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    members = document.getElementById("membersContent")
    card = members.getElementsByClassName("card");

    for (i = 0; i < card.length; i++) {
        h4 = card[i].getElementsByTagName('h4')[0];
        txtValue = h4.innerHTML;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          card[i].style.display = "block";
        } else {
          card[i].style.display = "none";
        }
      }
}

filterSelection('All');

function filterSelection(c) {

    members = document.getElementById("membersContent")
    card = members.getElementsByClassName("card");

    for (i = 0; i < card.length; i++) {
        p = card[i].getElementsByTagName('p')[0];
        txtValue1 = p.innerHTML;
        if (c == 'All') {
            card[i].style.display = "block";
        }
        else {
            if (txtValue1.indexOf(c) > -1) {
                card[i].style.display = "block";
              } else {
                card[i].style.display = "none";
              }
        } 
      }
}

function saveMessage() {
    const title = document.getElementById("title");
    const content = document.getElementById("content");

    console.log(title.value)
    console.log(content.value);
}

