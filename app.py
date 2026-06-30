<?php
$host = "YOUR_RDS_ENDPOINT";
$user = "YOUR_DB_USERNAME";
$password = "YOUR_DB_PASSWORD";
$db = "company";

$conn = new mysqli($host, $user, $password, $db);

if ($conn->connect_error) {
    die("Connection Failed: " . $conn->connect_error);
}
?>