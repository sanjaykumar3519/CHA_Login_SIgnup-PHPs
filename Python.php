<?php


$rooms = array(
#room1.avi
array("101","http://192.168.244.193:8080/video"),
array("102","room2.avi"),
array("103","room3.avi"),
array("201","201.avi"),
array("202","room5.avi"),
array("203","room6.avi"),
array("301","room7.avi"),
array("302","room8.avi"),
array("303","room9.avi"),
array("401","room10.avi"),
array("402","room11.avi"),
array("403","room12.avi")

);

if(isset($_POST['room']))
{
    for($r=0;$r<sizeof($rooms);$r++)
    {
        for($c=0;$c<1;$c++)
        {
            if($_POST['room']==$rooms[$r][$c])
            {
                $command = escapeshellcmd('Detect.py '.$rooms[$r][$c+1]);
                $output = shell_exec($command);
                echo $output;
                break;
            }
        }
    }
}
?>