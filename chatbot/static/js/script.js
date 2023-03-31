const conversation = document.querySelector('.conversation');
const input = document.querySelector('.input input');
const sendButton = document.querySelector('.input button');

sendButton.addEventListener('click', () => {
  const message = input.value;
  if (message.trim() === '') {
    return;
  }
  input.value = '';
  addMessage('You', message);
  sendMessage(message);
});

function addMessage(sender, message) {
  const p = document.createElement('p');
  p.innerHTML = `<strong>${sender}:</strong> ${message}`;
  conversation.appendChild(p);
  conversation.scrollTop = conversation.scrollHeight;
}

function sendMessage(message) {
  fetch('/chatbot', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      message: message
    })
  })
  .then(response => response.json())
  .then(data => {
    const message = data.message;
    addMessage('Bot', message);
  });
}

input.addEventListener('keydown', event => {
  if (event.key === 'Enter') {
    sendButton.click();
  }
});
