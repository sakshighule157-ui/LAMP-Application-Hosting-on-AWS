<?php

include 'db.php';

$sql="SELECT * FROM employees";

$result=$conn->query($sql);

echo "<h2>Employee List</h2>";

while($row=$result->fetch_assoc()){

echo $row['id']." ".
$row['name']." ".
$row['department']."<br>";

}

?>
