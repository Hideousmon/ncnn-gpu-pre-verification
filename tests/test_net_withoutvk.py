# Tencent is pleased to support the open source community by making ncnn available.
#
# Copyright (C) 2021 THL A29 Limited, a Tencent company. All rights reserved.
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

import numpy as np
import platform
import pytest
import glob

import ncnn


def test_net():
    dr = ncnn.DataReaderFromEmpty()

    with ncnn.Net() as net:
        ret = net.load_param("tests/test.param")
        net.load_model(dr)
        assert ret == 0 and len(net.blobs()) == 3 and len(net.layers()) == 3

        input_names = net.input_names()
        output_names = net.output_names()
        assert len(input_names) > 0 and len(output_names) > 0

        in_mat = ncnn.Mat((227, 227, 3))

        with net.create_extractor() as ex:
            ex.input("data", in_mat)
            ret, out_mat = ex.extract("output")

        assert ret == 0 and out_mat.dims == 1 and out_mat.w == 1

        net.clear()
        assert len(net.blobs()) == 0 and len(net.layers()) == 0


def test_net_without_vulkan():
    if platform.system() == 'Linux':
        lib = glob.glob(r'/usr/lib/**/libvulkan*')
        lib64 = glob.glob(r'/usr/lib64/**/libvulkan*')

    if platform.system() == 'Windows':
        lib = glob.glob(r'c:\Windows\System32\**\libvulkan*')
        lib64 = glob.glob(r'c:\Windows\SysWOW64\**\libvulkan*')
        

    if platform.system() == 'Darwin':
        lib = glob.glob(r'/usr/local/lib/**/libvulkan*')
        lib64 = glob.glob(r'/usr/local/lib64/**/libvulkan*')

        
    # dr = ncnn.DataReaderFromEmpty()

    # with ncnn.Net() as net:
    #     ret = net.load_param("tests/test.param")
    #     net.load_model(dr)
    #     assert ret == 0 and len(net.blobs()) == 3 and len(net.layers()) == 3

    #     input_names = net.input_names()
    #     output_names = net.output_names()
    #     assert len(input_names) > 0 and len(output_names) > 0

    #     in_mat = ncnn.Mat((227, 227, 3))

    #     with net.create_extractor() as ex:
    #         ex.input("data", in_mat)
    #         ret, out_mat = ex.extract("output")

    #     assert ret == 0 and out_mat.dims == 1 and out_mat.w == 1

    #     net.clear()
    #     assert len(net.blobs()) == 0 and len(net.layers()) == 0