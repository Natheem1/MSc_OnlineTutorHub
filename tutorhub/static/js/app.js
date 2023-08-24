// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  hljs.highlightAll();
});

let alertWrapper = document.querySelector('.alert')
let alertClose = document.querySelector('.alert__close')

if (alertWrapper) {
  alertClose.addEventListener('click', () =>
    alertWrapper.style.display = 'none'
  )

  setTimeout(() => {
    alertWrapper.style.display = 'none';
  }, 4000);
}

// Chat Message Box Minimizing 

  const chatWidget = document.querySelector('.chat-widget');
  const minimizeButton = chatWidget.querySelector('.minimize-button');

  // Toggle the "minimized" class when the minimize button is clicked
  minimizeButton.addEventListener('click', () => {
      chatWidget.classList.toggle('minimized');
  });
