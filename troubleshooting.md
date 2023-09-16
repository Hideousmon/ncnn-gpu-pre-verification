### 1. 部分平台架构无法顺利编译带Vulkan版本，问题记录(20230917)

#### a. arm64 universal2-MacOS问题修复 

发现一个cibuildwheel的Bug，之前纯cpu版本的macos arm64 及 universal2 的实际xcode编译目标平台依旧是x86_64，导致加上arm64 vulkan之后一直在报错。现在按照与macos-arm64-gpu.yml一致的流程编译ncnn后即可正常工作。
#### b. arm64-Windows问题隐患




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