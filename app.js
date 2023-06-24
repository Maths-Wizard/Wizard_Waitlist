const faqs = document.querySelectorAll('.faq');

faqs.forEach((faq) => {
    faq.addEventListener("click", () => {
        faq.classList.toggle("active");
    });
});

function changeLanguage() {
  const selectedLanguage = document.getElementById("language-select").value;
  const greetingElement = document.getElementById("greeting");

  // Language translations
  const translations = {
    en: "Hello!",
    fr: "Bonjour!",
    // Add more translations for each language
  };

  greetingElement.textContent = translations[selectedLanguage];

}

document.getElementById("language-select").addEventListener("change", changeLanguage);