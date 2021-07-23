console.log("check it out: https://linktr.ee/sksaddam");

// dynamically display socail media handle's ids with Typed effect
function displayTwitterId() {
  var twitterId = new Typed("#twitterTyped", {
    strings: ["@sksaddyy"],
    typeSpeed: 21,
    onBegin: function (self) {
      document.getElementById("twitter").addEventListener("mouseleave", () => {
        self.destroy();
      });
    },
  });
}
function displayLinkedInId() {
  var twitterId = new Typed("#linkedinTyped", {
    strings: ["@sksaddy99"],
    typeSpeed: 21,
    onBegin: function (self) {
      document.getElementById("linkedin").addEventListener("mouseleave", () => {
        self.destroy();
      });
    },
  });
}
function displayInstaId() {
  var twitterId = new Typed("#instaTyped", {
    strings: ["@sksaddam.99"],
    typeSpeed: 21,
    onBegin: function (self) {
      document
        .getElementById("instagram")
        .addEventListener("mouseleave", () => {
          self.destroy();
        });
    },
  });
}

// Typed effect
window.onload = function () {
  var typed = new Typed("#typed", {
    strings: ["Full-Stack Web Developer,", "A Learner"],
    typeSpeed: 77,
    backSpeed: 27,
    smartBackSpace: true,
    backDelay: 1234,
    startDelay: 1111,
    loop: true,
  });
};

// change innerText of contact option on mouseover and mouseout
const emailMe = document.getElementById("emailMe");
emailMe.addEventListener("mouseover", () => {
  emailMe.innerText = "Email me";
  // emailMe.classList.add('text-center', 'lh-1');
  emailMe.classList.add("lh-1");
});
emailMe.addEventListener("mouseout", () => {
  // emailMe.classList.remove('text-center');
  emailMe.innerText = "Contact";
});

// change background and add transition to the navbar on scrolling
window.addEventListener("scroll", () => {
  let header = document.querySelector("header");
  header.classList.toggle("sticky", window.scrollY > 15);
});

// Responsive NAVBAR from codepen
// ----- TOGGLE Navbar STARTS here -----
// define all UI variable
const navToggler = document.querySelector(".nav-toggler");
const navMenu = document.querySelector(".site-navbar ul");
const navLinks = document.querySelectorAll(".site-navbar a");

// load all event listners
allEventListners();

// functions of all event listners
function allEventListners() {
  // toggler icon click event
  navToggler.addEventListener("click", togglerClick);
  // nav links click event
  navLinks.forEach((elem) => elem.addEventListener("click", navLinkClick));
}

// togglerClick function
function togglerClick() {
  navToggler.classList.toggle("toggler-open");
  navMenu.classList.toggle("open");
}

// navLinkClick function
function navLinkClick() {
  if (navMenu.classList.contains("open")) {
    navToggler.click();
  }
}
// ----- TOGGLE Navbar ENDS here -----

// Microsoft Clarity

