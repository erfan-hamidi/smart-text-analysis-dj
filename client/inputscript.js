function sendMessage() {
    const userInput = document.getElementById('user-input');
    const chatHistory = document.getElementById('chat-history');
    var outputtype = document.querySelector( 'input[name="toggle"]:checked');
    // Get the user's input text
    const userMessage = userInput.value.trim();
    console.log(outputtype.value,userMessage);
    const apiUrl = 'http://127.0.0.1:8000/STA/';

        
    if (userMessage !== '') {
        //  access token
        const accessToken = localStorage.getItem("access");
        console.log(accessToken);
        //async function fetchProtectedResource() {
            const headers = {
                'Authorization': `Bearer ${accessToken}`,
                'Content-Type': 'application/json',
            };
            const inputdata = {
                'output-type' : outputtype.value,
                'input' : userMessage,
            }
           
                fetch(apiUrl, {
                    method: 'POST',
                    headers: headers,
                    body: JSON.stringify(inputdata),
                })
                .then((response) => {
                    console.log(response.status);
                    if (response.status == 401) {
                        alert("You must login!")
                    }
                    if (!response.ok) {
                      alert("ERROR")
                      throw new Error("Network response was not ok");
                    }
                    
                    return response.json();
                  })
                .then((data) => {
                    console.log(data.message);
                    document.getElementById('chat-history').textContent = data.message;
                })
                .catch((error) => {
                    console.error("Error:", error);
                    // Add error handling logic, like showing an error message to the user
                  });
                
            
        }

    }
//}
    //fetchProtectedResource();
