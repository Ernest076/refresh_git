```javascript
function scrollToSection() {
  document.getElementById('about').scrollIntoView({
    behavior: 'smooth'
  });
}

const hiddenElements = document.querySelectorAll('.hidden');

const observer = new IntersectionObserver((entries) => {

  entries.forEach((entry) => {

    if (entry.isIntersecting) {
      entry.target.classList.add('show');
    }

  });

});

hiddenElements.forEach((el) => observer.observe(el));

window.addEventListener('scroll', () => {

  const nav = document.querySelector('nav');

  if (window.scrollY > 50) {
    nav.style.boxShadow = '0 0 20px rgba(255,215,0,0.25)';
  }

  else {
    nav.style.boxShadow = 'none';
  }

});
```
