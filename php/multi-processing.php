<?php

// Config
$workers = 4;
$processList = [];

// PCNTL process
for ($seq=1; $seq <= $workers; $seq++) { 

    $pid = pcntl_fork();

    // Failed to fork process
    if ($pid == -1) {
        die("Could not fork");
    } 
    // Parent process
    else if ($pid) {

        array_push($processList, $pid);
        echo "Child process (PID: {$pid}) has been forked.\n";
    }
    // Each child process
    else {

        // For monitoring usage of CPU cores
        for ($i=0; $i < 100000000; $i++) { 
            $sum = $sum + $i;
        }
        
        // Stop child process
        die();
        break;
    }
}

// Wait for all child processes
foreach ($processList as $key => $pid) {

    pcntl_waitpid($pid, $status);
    echo "Child process (PID: {$pid}) done.\n";
}

echo "All done\n";