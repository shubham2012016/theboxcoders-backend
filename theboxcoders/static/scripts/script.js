gsap.registerPlugin(ScrollTrigger);

// 1. Define the animation as a PAUSED Timeline
const pageTwoAnimation = gsap.timeline({ 
    paused: true,
    // Add a default 'to' state to ensure the elements are visible when the animation ends
    defaults: { opacity: 1, y: 0 } 
});

pageTwoAnimation.from(".page-two span", {
    opacity: 0,
    y: 100,
    duration: 1.2,
    stagger: 0.3,
    ease: "power2.out",
});


// 2. Set the initial state of the elements to the 'from' state
// This ensures the text is hidden before the user scrolls, preventing a 'flash'
gsap.set(".page-two span", { opacity: 0, y: 100 });


// 3. Create the ScrollTrigger to control the timeline
ScrollTrigger.create({
    trigger: ".page-two",
    // Start when the top of the trigger hits 80% down the viewport (coming into view)
    start: "top 80%",
    // End when the trigger's bottom leaves the top of the viewport
    end: "bottom top", 
    
    // Crucial: Use onEnter to RESTART the animation from the beginning
    onEnter: () => {
        // Restart the timeline at time 0 and play it forward
        pageTwoAnimation.restart(); 
    },
    onEnterBack: () => {
        // Restart the timeline at time 0 and play it forward
        pageTwoAnimation.restart();
    },
    
    // Use onLeave/onLeaveBack to hide the text by reversing the animation
    onLeave: () => {
        // Reverse the animation to go back to the hidden (from) state
        pageTwoAnimation.reverse(0); // reverse(0) ensures it starts reversing from the end
    },
    onLeaveBack: () => {
        // Reverse the animation to go back to the hidden (from) state
        pageTwoAnimation.reverse(0);
    },
    
    // markers: true, // Uncomment to see the trigger points
});



// ---------------------------------consultation form -----------------------------------

const DESKTOP_MIN_WIDTH = 1024;
const TABLET_MAX_WIDTH = 1023;
const MOBILE_MAX_WIDTH = 767;

const viewportWidth = window.innerWidth;

document.querySelector(".cunsultation-form-heading button").addEventListener("click", () => {
  document.querySelector(".consultation-form-container").style.display = "none";
});
document.querySelector("#mobile-consultation-booking-form-close-btn").addEventListener("click", () => {
  document.querySelector(".consultation-booking-form-mobile").style.display = "none";
});
document.querySelector("#tablet-consultation-booking-form-close-btn").addEventListener("click", () => {
  document.querySelector(".consultation-booking-form-tablet").style.display = "none";
})


document.querySelector("#consultation-form").addEventListener("click", () => {
  if (viewportWidth >= DESKTOP_MIN_WIDTH) {
    document.querySelector(".consultation-form-container").style.display = "flex";
    initializeDesktopFeatures();

  } else if (viewportWidth <= TABLET_MAX_WIDTH && viewportWidth > MOBILE_MAX_WIDTH) {
    document.querySelector(".consultation-booking-form-tablet").style.display = "flex";
    adjustForTabletTouch();

  } else {
    document.querySelector(".consultation-booking-form-mobile").style.display = "flex";
    optimizeForMobile();
  }
})


document.querySelector("#web-dev-booking-button").addEventListener("click", () => {
  document.querySelector(".web-dev-booking-form").style.display = "flex";
})
document.querySelector("#python-booking-button").addEventListener("click", () => {
  document.querySelector(".python-services-booking-form").style.display = "flex";
})
document.querySelector("#ai-transformation-button").addEventListener("click", () => {
  document.querySelector(".ai-services-booking-form").style.display = "flex";
})
document.querySelector("#instagram-automation-booking-form").addEventListener("click", () => {
  document.querySelector(".instagram-automation-booking-form").style.display = "flex";
})
document.querySelector("#facebook-automation-booking-form").addEventListener("click", () => {
  document.querySelector(".facebook-automation-booking-form").style.display = "flex";
})
document.querySelector("#whatsapp-automation-booking-form").addEventListener("click", () => {
  document.querySelector(".whatssapp-automation-booking-form").style.display = "flex";
})
document.querySelector("#tally-automation-booking-form").addEventListener("click", () => {
  document.querySelector(".tally-automation-booking-form").style.display = "flex";
})
document.querySelectorAll("#close-button").forEach((button) => {
  button.addEventListener("click", () => {
    document.querySelector(".web-dev-booking-form").style.display = "none";
    document.querySelector(".python-services-booking-form").style.display = "none";
    document.querySelector(".ai-services-booking-form").style.display = "none";
    document.querySelector(".instagram-automation-booking-form").style.display = "none";
    document.querySelector(".facebook-automation-booking-form").style.display = "none";
    document.querySelector(".whatssapp-automation-booking-form").style.display = "none";
    document.querySelector(".tally-automation-booking-form").style.display = "none";
  });
});


document.querySelector("#web-dev-booking-button").addEventListener("click", () => {
  document.querySelector(".web-dev-booking-form").style.display = "flex";
})
document.querySelectorAll("#close-button").forEach((button) => {
  button.addEventListener("click", () => {
    document.querySelector(".web-dev-booking-form").style.display = "none";
  });
});