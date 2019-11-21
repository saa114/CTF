<?php
//include "config.php";
$con = mysqli_connect("localhost", "sqli", "7ohfiIYo2Ex", "exploits");
// verify connected
if (mysqli_connect_errno())
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }
$username = $_POST["username"];
$password = $_POST["password"];
$debug = $_POST["debug"];
$query = "SELECT * FROM users WHERE username='$username' AND password='$password'";
$result = mysqli_query($con, $query);

if (intval($debug)) {
  echo "<pre>";
  echo "username: ", htmlspecialchars($username), "\n";
  echo "password: ", htmlspecialchars($password), "\n";
  echo "SQL query: ", htmlspecialchars($query), "\n";
  if (mysqli_errno($con) !== 0) {
    echo "SQL error: ", htmlspecialchars(mysqli_error($con)), "\n";
  }
  echo "</pre>";
}

if (mysqli_num_rows($result) !== 1) {
  echo "<h1>Login failed.</h1>";
} else if ($username !== "admin") {
    echo "<h1>Logged in!</h1>";
    echo "<p>Cannot give flag to non-admin users</p>";
} else {
  echo "<h1>Logged in!</h1>";
  echo "<p>Your flag is: FLAG{inj3cti0n_1s_bad_a55}</p>";
}

?>
