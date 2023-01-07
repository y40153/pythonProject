#!/bin/sh
ps -ef |grep ycw | grep -v grep | awk '{print $2}' | xargs kill -9
