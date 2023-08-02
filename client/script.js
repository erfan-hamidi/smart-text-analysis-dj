const loginForm = document.getElementById("loginForm");

// Function to handle the login form submission
loginForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  const loginData = {
    email: email,
    password: password,
  };

  // Replace 'your-api-login-endpoint' with the actual login API endpoint in your Django backend
  fetch("http://127.0.0.1:8000/STA/login/", {
    mode: 'cors',
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(loginData),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      // Handle the response from the API
      console.log(data);
      // For simplicity, just log the token received from the API
      alert("Login successful! Token: " + data.token);
      const homeUrl = 'https://example.com/home'; // Replace with your home URL
      window.location.href = homeUrl;
    })
    .catch((error) => {
      console.error("Error:", error);
      // Add error handling logic, like showing an error message to the user
    });
});
