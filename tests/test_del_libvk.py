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


import platform
import glob
import os

if __name__ == "__main__":
    if platform.system() == 'Linux':
        libs = glob.glob(r'/usr/lib/**/libvulkan*')
        libs64 = glob.glob(r'/usr/lib64/**/libvulkan*')

    if platform.system() == 'Windows':
        libs = glob.glob(r'c:\Windows\System32\**\libvulkan*')
        libs64 = glob.glob(r'c:\Windows\SysWOW64\**\libvulkan*')
        

    if platform.system() == 'Darwin':
        libs = glob.glob(r'/usr/local/lib/**/libvulkan*')
        libs64 = glob.glob(r'/usr/local/lib64/**/libvulkan*')

    print(libs)
    print(libs64)

    if libs != [] and libs64 != []:
        for found_lib in libs:
            print("found_lib:", found_lib)
            os.remove(found_lib)
        for found_lib in libs64:
            os.remove(found_lib)
        print("trying to remove the libs.")

    
        if platform.system() == 'Linux':
            libs = glob.glob(r'/usr/lib/**/libvulkan*')
            libs64 = glob.glob(r'/usr/lib64/**/libvulkan*')

        if platform.system() == 'Windows':
            libs = glob.glob(r'c:\Windows\System32\**\libvulkan*')
            libs64 = glob.glob(r'c:\Windows\SysWOW64\**\libvulkan*')
            

        if platform.system() == 'Darwin':
            libs = glob.glob(r'/usr/local/lib/**/libvulkan*')
            libs64 = glob.glob(r'/usr/local/lib64/**/libvulkan*')

        print("after removing:")
        print(libs)
        print(libs64)
