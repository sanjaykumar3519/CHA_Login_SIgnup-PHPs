<?php

$conn = mysqli_connect("localhost","root","Password#","CHA");

$table = "hunt";

if(isset($_POST['username']) && isset($_POST['email']) && isset($_POST['department']) && isset($_POST['password'])) {

    $sql = "insert into ".$table."(username,email,department,password) values('".$_POST['username']."','".$_POST['email']."','".$_POST['department']."','".$_POST['password']."')";

    $check = "  select * from ".$table. " where username = '" .$_POST['username'].  "'";
    $result = mysqli_query($conn,$check);
    if (mysqli_num_rows($result) != 0) {
        echo "username already exist";
    } else {
        $res = mysqli_query($conn, $sql);
        if ($res) {
            echo "Signup Success";
        } else {
            echo "Signup failed";
        }
    }
}

?>
