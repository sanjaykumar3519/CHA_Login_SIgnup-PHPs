<?php

$conn = mysqli_connect("localhost","root","Password#","cha");
$table = "hunt";
$un = $_POST['username'];
$pass = $_POST['password'];
$sql = "select * from " .$table. " where username = '" .$un. "'";
$result = mysqli_query($conn,$sql);
$row = mysqli_fetch_assoc($result);
if(mysqli_num_rows($result)!=0)
{
    $db_un = $row['username'];
    $db_pass = $row['password'];
    if($db_un==$un && $db_pass==$pass)
    {
        echo "Login Success";
    }
    else
    {
        echo "username/password mismatch";
    }
}
else{
    echo "user not exist";
}

?>