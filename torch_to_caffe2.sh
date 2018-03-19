torch_file=$1
input_dim=$2
input_dim="${input_dim%\"}"
input_dim="${input_dim#\"}"

torch2pytorch_dir=convert_torch_to_pytorch
mv $torch_file $torch2pytorch_dir
cd $torch2pytorch_dir
python ./convert_torch.py -m $torch_file

extension="${torch_file##*.}"
filename="${torch_file%.*}"
pytorch_file=$filename.pth
model_structure_pyfile=$filename.py
mv $pytorch_file ..
mv $model_structure_pyfile ..
cd ..

convert_pyfile=$filename.convert.py
python ./pytorch2caffe2.py -src $pytorch_file -out $convert_pyfile -dim $input_dim
python $convert_pyfile -src $pytorch_file

onnx_file=$filename.onnx.pb
python ./onnx2caffe2.py -src $onnx_file

rm $pytorch_file
rm $onnx_file
rm $model_structure_pyfile
rm $convert_pyfile
