import argparse
import io

parser = argparse.ArgumentParser()
parser.add_argument('-src', '--source', dest='pth_weight_file', type=str, default=None, help='PyTorch weight file (.pth)')
parser.add_argument('-out', '--output', dest='out_python_filename', type=str, default=None, help='Output python file generated for conversion (.py)')
parser.add_argument('-dim', '--input_dim', dest='input_dim', type=str, default=None, help='Input dimension for the model. e.g. (1,3,512,512)')
args = parser.parse_args()

model_name = args.pth_weight_file.replace('.pth','')
header = '''
import torch
import torch.onnx
from torch import nn
from torch.autograd import Variable
import MODEL_NAME
MODEL_NAME.MODEL_NAME.load_state_dict(torch.load("MODEL_FILE"))
MODEL_NAME.MODEL_NAME.train(False)
x = Variable(torch.randn(MODEL_INPUT_DIM_VECTOR), requires_grad=True)
torch_out = torch.onnx._export(MODEL_NAME.MODEL_NAME, x, "MODEL_NAME.onnx.pb", verbose=True, export_params=True)
'''

header = header.replace('MODEL_NAME', model_name)
header = header.replace('MODEL_FILE', args.pth_weight_file)
header = header.replace('MODEL_INPUT_DIM_VECTOR', args.input_dim)

with open(args.out_python_filename, "w") as f:
    f.write(header)

