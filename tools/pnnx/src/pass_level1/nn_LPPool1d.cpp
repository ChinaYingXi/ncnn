// Tencent is pleased to support the open source community by making ncnn available.
//
// Copyright (C) 2021 THL A29 Limited, a Tencent company. All rights reserved.
//
// Licensed under the BSD 3-Clause License (the "License"); you may not use this file except
// in compliance with the License. You may obtain a copy of the License at
//
// https://opensource.org/licenses/BSD-3-Clause
//
// Unless required by applicable law or agreed to in writing, software distributed
// under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
// CONDITIONS OF ANY KIND, either express or implied. See the License for the
// specific language governing permissions and limitations under the License.

#include "fuse_module_pass.h"

namespace pnnx {

class LPPool1d : public FuseModulePass
{
public:
    const char* match_type_str() const
    {
        return "__torch__.torch.nn.modules.pooling.LPPool1d";
    }

    const char* type_str() const
    {
        return "nn.LPPool1d";
    }

    void write(Operator* op, const TorchGraphProxy& graph) const
    {
        const TorchNodeProxy* pow = graph.find_node_by_kind("aten::pow");
        op->params["norm_type"] = pow->input(1);

        const TorchNodeProxy* avg_pool1d = graph.find_node_by_kind("aten::avg_pool1d");

        const TorchNodeProxy* kernel_size = graph.find_producer_node_by_value(avg_pool1d->namedInput("kernel_size"));
        const TorchNodeProxy* stride = graph.find_producer_node_by_value(avg_pool1d->namedInput("stride"));

        op->params["kernel_size"] = kernel_size->input(0);
        if (stride->input_count() == 0)
        {
            op->params["stride"] = op->params["kernel_size"];
        }
        else
        {
            op->params["stride"] = stride->input(0);
        }
        op->params["ceil_mode"] = avg_pool1d->namedInput("ceil_mode");
    }
};

REGISTER_GLOBAL_PNNX_FUSE_MODULE_PASS(LPPool1d)

} // namespace pnnx
