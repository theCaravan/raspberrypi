#!/bin/bash
scp -i ~/.stuff/AWSKeyX.pem /home/pi/raspberrypi/temperature_proj/temp_output ec2-user@ec2-35-166-168-102.us-west-2.compute.amazonaws.com:/var/www/html/raspberrypi_outputs/blueberry.txt
