function sendMessage() {
    const userInput = document.getElementById('user-input');
    const chatHistory = document.getElementById('chat-history');
    var outputtype = document.getElementById("myRadio");
    // Get the user's input text
    const userMessage = userInput.value.trim();
    const apiUrl = 'http://127.0.0.1:8000/STA';

        
    if (userMessage !== '') {
        //  access token
        const accessToken = localStorage.getItem("access");
        async function fetchProtectedResource() {
            const headers = {
                'Authorization': `Bearer ${accessToken}`,
                'Content-Type': 'application/json',
                'output-type' : outputtype,
            };

            try {
                const response = await fetch(apiUrl, {
                    method: 'GET',
                    headers: headers
                });

                if (response.ok) {
                    const data = await response.json();
                    document.getElementById('message').textContent = data.message;
                } else {
                    document.getElementById('message').textContent = 'Error: Unable to access protected resource.';
                }
            } catch (error) {
                document.getElementById('message').textContent = 'Error: Unable to access protected resource.';
            }
        }

        // Clear the input field
        userInput.value = '';

        // Simulate a response from ChatGPT (You can replace this with actual API call and response)
        setTimeout(() => {
            const chatBubble = document.createElement('div');
            chatBubble.className = 'chat-bubble gpt-bubble';
            chatBubble.innerHTML = '<span class="message">ChatGPT response...</span>';
            chatHistory.appendChild(chatBubble);
        }, 500); // Delayed response simulation
    }
}
    fetchProtectedResource();
