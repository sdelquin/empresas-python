document.addEventListener("DOMContentLoaded", () => {
  const messages = document.querySelector(".messages");
  if (messages) {
    setTimeout(() => {
      messages.style.display = "none";
    }, 3000);
  }
});
