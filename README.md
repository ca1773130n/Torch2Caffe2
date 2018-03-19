# Torch2Caffe2

Python and shell script to convert Torch model to Caffe2.
The conversion uses ONNX Caffe2 backend and has three steps like:
Torch (.t7) -> PyTorch (.pth) -> ONNX (.onnx.pb) -> Caffe2 (.pb)

## Requirement

* PyTorch
* ONNX, ONNX-Caffe2
* Caffe2 (Python)
* A Torch model file to convert (.t7)

NOTE:
* If you don't have those in your environment yet, follow the steps below:
* https://github.com/caffe2/caffe2/issues/1204

## Usage

  torch_to_caffe2.sh <model_filename> <input_dimension>

* The model file must be in the same directory of the shell script
* The input dimension should look like this: (1,3,512,512)

## Acknowledgement

This script is based on a GitHub project "convert_torch_to_pytorch"
https://github.com/clcarwin/convert_torch_to_pytorch

