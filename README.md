

# ncnn-gpu-pre-verification

### Current ncnn wheels matrix 

|                       | x86_64 | i686 | x86  | AMD64 | ARM64 | universal2 | aarch64 | ppc64le | s390x |
| :-------------------: | :----: | :--: | :--: | :---: | :---: | :--------: | :-------: | :-------: | :----: |
| ubuntu (cp-manylinux) |   √    |  √   |  -   |   -   |   -   |     -      | √ | √ | √ |
| ubuntu (cp-musllinux) |   √    |  √   |  -   |   -   |   -   |     -      | √ | √ | √ |
|      ubuntu (pp)      |   √    |  √   |  -   |   -   |   -   |     -      | √ | - | - |
|     windows (pp)      |   -    |  -   |  -   |   √   |   -   |     -      | - | - | - |
|     windows (cp)      |   -    |  -   | cpu  |   √   |  cpu  |     -      | - | - | - |
|      macos (pp)       |   √    |  -   |  -   |   -   |   -   |     -      | - | - | - |
|      macos (cp)       |   √    |  -   |  -   |   -   |  cpu  |    cpu     | - | - | - |

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

### TO DO

- [ ] ~~build wheels on i686, x86, arm64, universal2 with vulkan~~.
- [x] record the issues on x86, arm64, universal2.
- [x] pytest without libvulkan.
- [x] build wheels for i686, aarch64, ppc64le, s390x and musllinux.
- [x] pull request to ncnn.
