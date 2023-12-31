

# ncnn-gpu-pre-verification

### Current ncnn wheels matrix 

|                       | x86_64 | i686 | x86  | AMD64 | ARM64 | universal2 | aarch64 | ppc64le | s390x |
| :-------------------: | :----: | :--: | :--: | :---: | :---: | :--------: | :-------: | :-------: | :----: |
| ubuntu (cp-manylinux) |   √    |  √   |  -   |   -   |   -   |     -      | √ | √ | √ |
| ubuntu (cp-musllinux) |   √    |  √   |  -   |   -   |   -   |     -      | √ | √ | √ |
|      ubuntu (pp)      |   √    |  √   |  -   |   -   |   -   |     -      | √ | - | - |
|     windows (pp)      |   -    |  -   |  -   |   √   |   -   |     -      | - | - | - |
|     windows (cp)      |   -    |  -   | √ |   √   |  √  |     -      | - | - | - |
|      macos (pp)       |   √    |  -   |  -   |   -   |   -   |     -      | - | - | - |
|      macos (cp)       |   √    |  -   |  -   |   -   |  √  |    √    | - | - | - |

wheels can be found at [built-wheels](https://github.com/Hideousmon/ncnn-gpu-pre-verification/tree/main/built-wheels) for temporary use.

### trouble shooting

can be found [here](https://github.com/Hideousmon/ncnn-gpu-pre-verification/blob/main/troubleshooting.md). [in Chinese]

### yolov4-tiny inference on windows  (without installing vulkan sdk)

|                  | CPU(3960X) | GPU(AMD RX 580) |
| :--------------: | :--------: | :-------------: |
| time consumption |  51.12ms   |     34.08ms     |

### compare with C++

|        | CPU(6800H) | GPU(3060 Laptop) |
| :----: | :--------: | :--------------: |
|  C++   |  49.24ms   |     13.14ms      |
| Python |  56.62ms   |     14.61ms      |
