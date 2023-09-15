### 1. 部分平台架构无法顺利编译带Vulkan版本，问题记录(20230915)

#### a. ARM64架构-Windows

> 【使用Vulkan-Loader】报错位置：repair built wheel过程
>
> 报错：FileNotFoundError: Unable to find library: msvcp140.dll

CIBW_BEFORE_ALL:

```
git clone https://github.com/KhronosGroup/Vulkan-Loader.git &&
cd Vulkan-Loader && mkdir build && cd build &&
python3 ../scripts/update_deps.py --dir ../external --config debug &&
cmake -C ../external/helper.cmake -G "Visual Studio 17 2022" -A ARM64 -DCMAKE_BUILD_TYPE=Debug -DUSE_MASM=OFF ..  && cmake --build . &&
mklink /d "D:/a/ncnn-gpu-pre-verification/ncnn-gpu-pre-verification/Vulkan-Loader/external/Vulkan-Headers/build/install/lib" "D:/a/ncnn-gpu-pre-verification/ncnn-gpu-pre-verification/Vulkan-Loader/build/loader/Debug"
```

问题思考：

根据cibuildwheel的工作方式描述[cibuildwheel/docs/data/how-it-works.png at main · pypa/cibuildwheel (github.com)](https://github.com/pypa/cibuildwheel/blob/main/docs/data/how-it-works.png) ，Linux系统会创建容器，并在容器中进行编译；而Windows与MacOS则只在x86_64架构上进行交叉编译。

Visual C++ Redistributables 在Github Actions的runner中应该是齐全的([runner-images/images/win/Windows2019-Readme](https://github.com/actions/runner-images/blob/main/images/win/Windows2019-Readme.md))，且应该不有路径缺失的问题，可能还是交叉编译或修复工具有些问题。

#### b. ARM64架构-MacOS

> 【使用VULKAN_SDK】报错位置：repair built wheel过程
>
> 报错：Required arch arm64 missing from ncnn/ncnn.cpython-38-darwin.so
>
> [ncnn-vulkan对此架构没有进行repair的过程，故其实生成的wheel可能存在问题]
>
> 【使用Vulkan-Loader】报错位置：编译wheel过程
>
> 报错：ld: can't map file, errno=22 file '/Users/runner/work/ncnn-gpu-pre-verification/ncnn-gpu-pre-verification/Vulkan-Loader/build/Vulkan-Headers/lib/vulkan.framework' for architecture x86_64

CIBW_BEFORE_ALL:

```
git clone https://github.com/KhronosGroup/Vulkan-Loader.git &&
cd Vulkan-Loader && mkdir build && cd build &&
../scripts/update_deps.py && cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_SYSTEM_PROCESSOR=arm64 -DCMAKE_OSX_ARCHITECTURES=arm64 -DVULKAN_HEADERS_INSTALL_DIR=$(pwd)/Vulkan-Headers/build/install .. &&
make -j$(nproc) && cd Vulkan-Headers && ln -s ../loader lib 
```

问题思考：

交叉编译或修复工具还存在问题，但修不通。

#### c. Universal2架构-MacOS

> 【使用VULKAN_SDK】报错位置：repair built wheel过程
>
> 报错：Required arch arm64 missing from ncnn/ncnn.cpython-38-darwin.so
>
> [ncnn-vulkan对此架构没有进行repair的过程，故其实生成的wheel可能存在问题]
>
> 【使用Vulkan-Loader】报错位置：编译wheel过程
>
> 报错：ld: can't map file, errno=22 file '/Users/runner/work/ncnn-gpu-pre-verification/ncnn-gpu-pre-verification/Vulkan-Loader/build/Vulkan-Headers/lib/vulkan.framework' for architecture x86_64

问题思考：

同ARM64架构-MacOS。

#### d. 对上述架构暂时保持cpu版本

或者取消掉repair过程，可以完成编译，但是如果缺库导致没法正常工作好像不太好。

### 2. Forked ncnn 编译全部wheels最新验证(20230914) √

可见[release test · Hideousmon/ncnn@43df385 (github.com)](https://github.com/Hideousmon/ncnn/actions/runs/6182483110)。

### 3. libvulkan库无法找到时是否可用的验证(20230914) √

> libvulkan库无法找到时依然可用的依据：
>
> 在cibuildwheel执行过程中，默认会执行repair built wheel的过程，对于linux使用auditwheel工具进行，对于macOS使用delacate-wheel工具进行，具体原理为检测被用到的共享库并复制到wheel包中，从而避免用于机器上缺失共享库而无法使用。

验证过程：

在ubuntu、windows、macos系统上确保删除或无法找到libvulkan共享库，然后对推理过程进行测试。

验证使用[test_del_libvk.py](https://github.com/Hideousmon/ncnn-gpu-pre-verification/blob/main/tests/test_del_libvk.py)删除并测试是否成功删除libvulkan，之后使用[test_net_withoutvk.py](https://github.com/Hideousmon/ncnn-gpu-pre-verification/blob/main/tests/test_net_withoutvk.py)进行推理测试。

验证结果：

在成功删除了'/usr/lib/x86_64-linux-gnu/libvulkan.so.1'及 '/usr/lib/x86_64-linux-gnu/libvulkan.so.1.2.131'的ubuntu系统上依旧可以正常使用。在初始不携带libvulkan的windows、macos系统上也可以正常使用，最新的结果(20230914)可见[update wheels · Hideousmon/ncnn-gpu-pre-verification@b5dbf58 (github.com)](https://github.com/Hideousmon/ncnn-gpu-pre-verification/actions/runs/6184598973/job/16788555563)



### 4. Windows系统cibuildwheel无默认repair wheel过程问题修复(20230910)  √

> 问题描述：
>
> 在验证缺失libvulkan是否可用的过程中发现，在github actions的windows runner上安装编译的ncnn wheel后无法正常import并报错ImportError: DLL load failed while importing ncnn: The specified module could not be found. 
>
> 按常理，执行repair built wheel过程后需要的dll应已经被复制到wheel当中，不应该出现此报错。故查看cibuildwheel文档，发现默认的repair built wheel过程只在linux及macos上有定义，于是尝试使用windows上类似的工具[adang1345/delvewheel: Self-contained Python wheels for Windows (github.com)](https://github.com/adang1345/delvewheel)，将问题解决。
>
> [在测试过程中发现，ncnn-vulkan的wheel由于没有repair wheel过程，故也存在上述问题]

使用delvewheel修复wheel之前的 ncnn-1.0.20230906-cp38-cp38-win_amd64.whl 文件大小为 3117KB，修复后大小为3632KB，使用修复后的包可以在github actions的windows runner上正常运行。