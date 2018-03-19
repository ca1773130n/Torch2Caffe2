import onnx
from onnx_caffe2.backend import Caffe2Backend
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-src', '--source', dest='onnx_weight_file', type=str, default=None, help='ONNX weight file (.onnx.pb)')
args = parser.parse_args()

onnx_proto_file = args.onnx_weight_file
onnx_model = onnx.load(onnx_proto_file)
onnx.checker.check_model(onnx_model)

model_name = onnx_proto_file.replace('.onnx.pb','')
init_net, predict_net = Caffe2Backend.onnx_graph_to_caffe2_net(onnx_model.graph, device="CPU")
with open(model_name + "_init.pb", "wb") as f:
    f.write(init_net.SerializeToString())
with open(model_name + "_init.pbtxt", "w") as f:
    f.write(str(init_net))
with open(model_name + "_predict.pb", "wb") as f:
    f.write(predict_net.SerializeToString())
with open(model_name + "_predict.pbtxt", "w") as f:
    f.write(str(predict_net))

