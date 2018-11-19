#!/bin/bash
found=`pip list|grep opencv-python`
if [ -z "$found" ]; then
  echo "install opencv-python by pip"
  pip install opencv-python
else
  echo "opencv-python is installed"
fi
