<?php
//ini_set('display_errors', '1');
//ini_set('display_startup_errors', '1');
//error_reporting(E_ALL);

header('Access-Control-Allow-Origin: *');


#$output = shell_exec($command);

$args=$_POST["activeTabId"];

exec("/Users/alexpetmecky/Desktop/Recipes/venv/bin/python ./main.py 2>&1 $args", $output);
#echo "OUTPUT:";
#print_r($output);
#echo "DONE";
echo "http://localhost:8888/recipe_callback/output_dir/".$output[0].".pdf";