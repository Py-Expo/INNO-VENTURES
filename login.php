<?php
// Connect to MySQL
$mysqli = new mysqli("id", "username", "password");

// Check connection
if ($mysqli->connect_error) {
    die("Connection failed: " . $mysqli->connect_error);
}

// Retrieve username and password from the form
$username = $_POST['uname'];
$password = $_POST['psw'];

// SQL query to check if the username and password match
$sql = "SELECT * FROM users WHERE username='$username' AND password='$password'";
$result = $mysqli->query($sql);

// Check if there's a row returned
if ($result->num_rows == 1) {
    // Successful login
    echo "Login successful";
} else {
    // Invalid username or password
    echo "Invalid username or password";
}

// Close connection
$mysqli->close();
?>
