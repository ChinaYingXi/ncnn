# Tencent is pleased to support the open source community by making ncnn available.
#
# Copyright (C) 2024 THL A29 Limited, a Tencent company. All rights reserved.
#
# Licensed under the BSD 3-Clause License (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# https://opensource.org/licenses/BSD-3-Clause
#
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

import torch
import torchvision
import torchvision.models as models
from packaging import version

def test():
    if version.parse(torchvision.__version__) < version.parse('0.12'):
        return True

    if version.parse(torch.__version__) >= version.parse('2.0') and version.parse(torch.__version__) < version.parse('2.1'):
        return True

    net = models.vit_b_32()
    net.eval()

    torch.manual_seed(0)
    x = torch.rand(1, 3, 224, 224)

    a = net(x)

    # export onnx
    torch.onnx.export(net, (x,), "test_vit_b_32.onnx")

    # onnx to pnnx
    import os
    os.system("../../src/pnnx test_vit_b_32.onnx inputshape=[1,3,224,224]")

    # pnnx inference
    import test_vit_b_32_pnnx
    b = test_vit_b_32_pnnx.test_inference()

    if not torch.allclose(a, b, 1e-4, 1e-4):
        return False

    if version.parse(torch.__version__) < version.parse('2.8'):
        return True

    # export dynamo onnx
    torch.onnx.dynamo_export(net, x).save("test_vit_b_32_dynamo.onnx")

    # onnx to pnnx
    os.system("../../src/pnnx test_vit_b_32_dynamo.onnx inputshape=[1,3,224,224]")

    # pnnx inference
    import test_vit_b_32_dynamo_pnnx
    b = test_vit_b_32_dynamo_pnnx.test_inference()

    return torch.allclose(a, b, 1e-4, 1e-4)

if __name__ == "__main__":
    if test():
        exit(0)
    else:
        exit(1)
