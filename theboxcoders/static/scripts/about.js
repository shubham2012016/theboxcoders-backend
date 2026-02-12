// ---------------------------------consultation form -----------------------------------

document.querySelector(".cunsultation-form-heading button").addEventListener("click", (e) => {
  e.preventDefault();
  document.querySelector(".consultation-form-container").style.display = "none";
});

document.querySelector("#consultation-form").addEventListener("click", () => {
  document.querySelector(".consultation-form-container").style.display = "flex";
})