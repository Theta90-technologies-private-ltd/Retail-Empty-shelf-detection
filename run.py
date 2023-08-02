import os
os.system("detectnet --model=ssd-mobilenet.onnx --labels=labels.txt --input-blob=input_0 --output-cvg=scores --output-bbox=boxes /dev/video0")
