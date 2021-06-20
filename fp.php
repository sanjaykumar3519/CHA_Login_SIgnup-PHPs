<?php

$con = mysqli_connect("localhost","root","Password#","cha");
$table = "hunt";

//forgot password
if(isset($_POST['check_user'])) {
    $sql = "select * from " . $table . " where username='" . $_POST['check_user'] . "'";
    $result = mysqli_query($con, $sql);
    if (mysqli_num_rows($result) != 0) {
        echo "true";
    } else {
        echo "username not exist";
    }
}
//reset password
if(isset($_POST['username']) && isset($_POST['password'])) {
    $sql = "update " . $table . " set password = '" .$_POST['password']. "' where username = '" .$_POST['username']. "'";
    if (mysqli_query($con, $sql)) {
        echo "success";
    }else{
        echo "password reset failed";
    }
}
?>

