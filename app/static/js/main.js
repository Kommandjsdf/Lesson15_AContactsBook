document.addEvenListener("DOMContentLoaded", function(){
  const editButton = document.getElementById("editButton");
  let selectedRow = null;
  let selectedContactId = null;
  const row = document.querySelectorAll(".table-element");
  rows forEach(row => {
    row.addEventListener("click", function{
      if (selectedRow){
        selectedRow.classList.remove("table-active");
      }
      selectedRow = this;
      selectedRow.classList.add("table-active");

      selectedContactId = this.dataset.contactId;

      editButton.href = `/edit/${selectedContactId}`

    });
  });
});