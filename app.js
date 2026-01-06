// Highlight the active nav link and reveal sections on scroll.
const navLinks = document.querySelectorAll(".nav-item");
let currentPath = window.location.pathname.split("/").pop();
if (!currentPath) {
  currentPath = "index.html";
}

navLinks.forEach((link) => {
  const target = link.getAttribute("href");
  if (target === currentPath) {
    link.classList.add("selected");
  }
});

const revealElements = document.querySelectorAll(".reveal");

if (revealElements.length > 0 && "IntersectionObserver" in window) {
  const observer = new IntersectionObserver(
    (entries, activeObserver) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("in-view");
          activeObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.2 }
  );

  revealElements.forEach((el) => observer.observe(el));
} else {
  revealElements.forEach((el) => el.classList.add("in-view"));
}
