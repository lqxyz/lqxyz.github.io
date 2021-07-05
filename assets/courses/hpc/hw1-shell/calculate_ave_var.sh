#!/bin/bash
# Qun Liu 2015-3-6
#cat ./df-d18o-340ka-dfo2006.txt | grep [0-9]$ | grep  ^[^[:alpha:]] | awk -F " " '{data[NR]=$4;} END{for(i=1; i<=NR; i++)sum += data[i]; ave=sum/NR; for(i=1; i<=NR; i++)sum_sq += (data[i]-ave)*(data[i]-ave); print "Average is: " ave, "VAR is: " sum_sq/NR }'
awk 'BEGIN {stat=0; sum=0; n=0; sum_sq=0;} {if (stat==0 && NF==4 && $1=="TopDepth") stat=1; else if(stat==1 && NF==4){ data[n]=$4; n++;}} END{for(i=0; i<n; i++) sum+=data[i]; ave=sum/n; for(i=0; i<n; i++) sum_sq+=(data[i]-ave)*(data[i]-ave);  print "Average is: " ave, "\nVariance is: " sum_sq/n}' ./df-d18o-340ka-dfo2006.txt 
