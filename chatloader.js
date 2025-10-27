// chatloader.js
(function () {
  const scriptUrl = "https://media.imi.chat/widget/js/imichatinit.js";

  // Create a script tag to load the chat widget directly
  const script = document.createElement("script");
  script.src = scriptUrl;
  script.async = true;

  script.onload = function () {
    console.log("Chat widget loaded successfully.");
  };

  script.onerror = function () {
    console.error("Failed to load chat widget. Check CORS or domain restrictions.");
  };

  document.body.appendChild(script);
})();
