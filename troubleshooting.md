[toc]

### 1. libvulkan库无法找到时是否可用的验证 √

> libvulkan库无法找到时依然可用的依据：
>
> 在cibuildwheel执行过程中，默认会执行repair built wheel的过程，对于linux使用auditwheel工具进行，对于macOS使用delacate-wheel工具进行，具体原理为检测被用到的共享库并复制到wheel包中，从而避免用于机器上缺失共享库而无法使用。

验证过程：

在ubuntu、windows、macos系统上确保删除或无法找到libvulkan共享库，然后对推理过程进行测试。

验证使用[test_del_libvk.py](https://github.com/Hideousmon/ncnn-gpu-pre-verification/blob/main/tests/test_del_libvk.py)删除并测试是否成功删除libvulkan，之后使用[test_net_withoutvk.py](https://github.com/Hideousmon/ncnn-gpu-pre-verification/blob/main/tests/test_net_withoutvk.py)进行推理测试。

验证结果：

在成功删除了'/usr/lib/x86_64-linux-gnu/libvulkan.so.1'及 '/usr/lib/x86_64-linux-gnu/libvulkan.so.1.2.131'的ubuntu系统上依旧可以正常使用。在初始不携带libvulkan的windows、macos系统上也可以正常使用，结果可见[Update test-without-libvulkan.yml · Hideousmon/ncnn-gpu-pre-verification@cc24d88 (github.com)](https://github.com/Hideousmon/ncnn-gpu-pre-verification/actions/runs/6135635910/job/16649585147)

### 2. Windows系统cibuildwheel无默认repair wheel过程问题修复 √

> 问题描述：
>
> 在验证缺失libvulkan是否可用的过程中发现，在github actions的windows runner上安装编译的ncnn wheel后无法正常import并报错ImportError: DLL load failed while importing ncnn: The specified module could not be found. 
>
> 按常理，执行repair built wheel过程后需要的dll应已经被复制到wheel当中，不应该出现此报错。故查看cibuildwheel文档，发现默认的repair built wheel过程只在linux及macos上有定义，于是尝试使用windows上类似的工具[adang1345/delvewheel: Self-contained Python wheels for Windows (github.com)](https://github.com/adang1345/delvewheel)，将问题解决。
>
> [在测试过程中发现，ncnn-vulkan的wheel由于没有repair wheel过程，故也存在上述问题]

使用delvewheel修复wheel之前的 ncnn-1.0.20230906-cp38-cp38-win_amd64.whl 文件大小为 3117KB，修复后大小为3632KB，使用修复后的包可以在github actions的windows runner上正常运行。

### 3. 部分平台架构无法顺利编译带Vulkan版本，问题记录

#### a. Musllinux

> 报错位置：repair built wheel过程
>
> 报错：ValueError: Cannot repair wheel, because required library "libpthread.so.0" could not be located 或 ValueError: Cannot repair wheel, because required library "libm.so.6" could not be located

尝试解决过程记录：

在cibuildwheel的容器中先执行apk add libc6-compat，依旧报错：

ValueError: Cannot repair wheel, because required library "libdl.so.2" could not be located

问题思考：

可能是Musl C库缺失的东西有点多？

#### b. i686架构-Ubuntu

> 报错位置：编译连接生成wheel过程
>
> 报错： /opt/rh/devtoolset-10/root/usr/libexec/gcc/i686-redhat-linux/10/ld: /project/ncnn-python-gpu/1.2.189.0/x86_64/lib/libvulkan.so: error adding symbols: file in wrong format

问题思考：

vulkan sdk官网Linux版本似乎只支持x86_64，在i686上会出问题。或许可以尝试源码编译vulkan？

#### c. x86架构-Windows

> 报错位置：编译连接生成wheel过程
>
> 报错：ncnn.lib(allocator.obj) : error LNK2001: unresolved external symbol *** [D:\a\ncnn-gpu-pre-verification\ncnn-gpu-pre-verification\ncnn-python-gpu\build\temp.win32-3.6\Release\python\pyncnn.vcxproj] 

问题思考：

不清楚报错的原理，没有什么解决思路。

#### d. ARM64架构-Windows

> 报错位置：编译连接生成wheel过程
>
> 报错：ncnn.lib(allocator.obj) : error LNK2001: unresolved external symbol *** [D:\a\ncnn-gpu-pre-verification\ncnn-gpu-pre-verification\ncnn-python-gpu\build\temp.win-arm64-cpython-39\Release\python\pyncnn.vcxproj]

问题思考：

不清楚报错的原理，没有什么解决思路。

#### e. ARM64架构-MacOS

> 报错位置：repair built wheel过程
>
> 报错：Required arch arm64 missing from ncnn/ncnn.cpython-38-darwin.so
>
> [ncnn-vulkan对此架构没有进行repair的过程，故其实生成的wheel可能存在问题]

问题思考：

不清楚报错的原理，没有什么解决思路。

#### f. Universal2架构-MacOS

> 报错位置：repair built wheel过程
>
> 报错：Required arch arm64 missing from ncnn/ncnn.cpython-38-darwin.so
>
> [ncnn-vulkan对此架构没有进行repair的过程，故其实生成的wheel可能存在问题]

问题思考：

不清楚报错的原理，没有什么解决思路。

#### g. 对上述架构暂时保持cpu版本

### 4. Forked ncnn 编译全部wheels验证 √

可见[release test · Hideousmon/ncnn@03a13ba (github.com)](https://github.com/Hideousmon/ncnn/actions/runs/6135704955)。

