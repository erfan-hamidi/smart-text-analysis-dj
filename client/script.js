const loginForm = document.getElementById("loginForm");
console.log(loginForm)
// Function to handle the login form submission
loginForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const formData = new FormData(loginForm);
  const email = formData.get("email");
  const password = formData.get("password");

  const loginData = {
    email: email,
    password: password,
  };
  console.log(loginData)
  // Replace 'your-api-login-endpoint' with the actual login API endpoint in your Django backend
  fetch("http://127.0.0.1:8000/STA/login/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(loginData),
    
  })
    .then((response) => {
      if (!response.ok) {
        alert("The email address or password you entered is invalid")
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      // Handle the response from the API
      console.log(data.refresh);
      // For simplicity, just log the token received from the API
      alert("Login successful!");
      localStorage.setItem("refresh", data.refresh);
      localStorage.setItem("access", data.access);
      const homeUrl = 'input.html'; // Replace with your home URL
      window.location.href = homeUrl;
    })
    .catch((error) => {
      console.error("Error:", error);
      // Add error handling logic, like showing an error message to the user
    });
});


const signupForm = document.getElementById("signupForm");
console.log(signupForm)
// Function to handle the login form submission
signupForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const formData = new FormData(signupForm);
  const email = formData.get("email");
  const password = formData.get("pswd");
  const username = formData.get("txt")

  const signupData = {
    email: email,
    username : username,
    password: password,
  };
  console.log(signupData)
  // Replace 'your-api-login-endpoint' with the actual login API endpoint in your Django backend
  fetch("http://127.0.0.1:8000/STA/signup/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(signupData),
    
  })
    .then((response) => {
      if (!response.ok) {
        alert("You can not Signup!")
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      // Handle the response from the API
      console.log(data.refresh);
      // For simplicity, just log the token received from the API
      alert("Signup successful!");
      localStorage.setItem("refresh", data.refresh);
      localStorage.setItem("access", data.access);
      const homeUrl = 'input.html'; // Replace with your home URL
      window.location.href = homeUrl;
    })
    .catch((error) => {
      console.error("Error:", error);
      // Add error handling logic, like showing an error message to the user
    });
});