# Torch2Caffe2

Python and shell script to convert Torch models into Caffe2 protobuf files.
The conversion uses ONNX-Caffe2 backend and has three steps like:
Torch (.t7) -> PyTorch (.pth) -> ONNX (.onnx.pb) -> Caffe2 (.pb)
You need to specify the input dimension of the model.

## Source Download

    git clone --recursive git@github.com:ca1773130n/Torch2Caffe2.git

## Requirements

* Python 3.5
* PyTorch
* ONNX, ONNX-Caffe2
* Caffe2 (optional)

NOTE:
* If you don't have those in your environment yet, follow the steps below:
* https://github.com/caffe2/caffe2/issues/1204

## Usage

    torch_to_caffe2.sh <model_filename> <input_dimension>

* The model file must be in the same directory of the shell script
* The input dimension needs to be surrounded by quotes. It should look like this: "(1,3,512,512)"

## Acknowledgement

This work is based on a GitHub project below.
 * https://github.com/clcarwin/convert_torch_to_pytorch

Tested environment
 * Ubuntu 16.04
 * Anaconda Python 3.6
 * A Torch VGG-19 model file

Known Issues
 * PyTorch to ONNX conversion is imperfect (e.g. ONNX doesn't support ceil_mode in MaxPooling)

