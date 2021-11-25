<?php

$con = mysqli_connect("localhost","root","3519","CHA");
$table = "hunt";

//profile data
if(isset($_POST['username']))
{
	$un = $_POST['username'];
	$sql = "select * from ".$table." where username='".$un."'";
	//$sql = "select * from hunt";
	$res = mysqli_query($con,$sql);
	$row = mysqli_fetch_assoc($res);
	if(mysqli_num_rows($res)!=0)
	{
		echo $row['username'].":".$row['email'].":".$row['department']." ";
	}
}

//delete account
if(isset($_POST['delete']))
{
	$un_1 = $_POST['delete'];
	$sql_1= "delete from ".$table." where username='".$un_1."'";
	if(mysqli_query($con,$sql_1))
	{
		echo "success";
	}
}
?>