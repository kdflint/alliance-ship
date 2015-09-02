<?php 

echo "callinc...";
$command = escapeshellcmd('/home1/northbr6/batch/dev/alliance/backlog_bridge/webhook_test.py');
$output = shell_exec($command);
echo $output;

?>