# ncnn-gpu-pre-verification
### Current ncnn-gpu wheels matrix 

|                       | x86_64 | i686 | x86  | AMD64 | ARM64 | universal2 |
| :-------------------: | :----: | :--: | :--: | :---: | :---: | :--------: |
| ubuntu (cp-manylinux) |   √    |  √   |  -   |   -   |   -   |     -      |
| ubuntu (cp-musllinux) |   √    |  √   |  -   |   -   |   -   |     -      |
|      ubuntu (pp)      |   √    |  √   |  -   |   -   |   -   |     -      |
|     windows (pp)      |   -    |  -   |  -   |   √   |   -   |     -      |
|     windows (cp)      |   -    |  -   | cpu  |   √   |  cpu  |     -      |
|      macos (pp)       |   √    |  -   |  -   |   -   |   -   |     -      |
|      macos (cp)       |   √    |  -   |  -   |   -   |  cpu  |    cpu     |

### yolov4-tiny inference on windows  (without installing vulkan sdk)

|                  | CPU(3960X) | GPU(AMD RX 580) |
| :--------------: | :--------: | :-------------: |
| time consumption |  51.12ms   |     34.08ms     |

### compare with C++

|        | CPU(6800H) | GPU(3060 Laptop) |
| :----: | :--------: | :--------------: |
|  C++   |  49.24ms   |     13.14ms      |
| Python |  56.62ms   |     14.61ms      |

### trouble shooting

can be found [here](https://github.com/Hideousmon/ncnn-gpu-pre-verification/blob/main/troubleshooting.md). [in Chinese]

### TO DO

- [ ] ~~build wheels on i686, x86, arm64, universal2 with vulkan~~.
- [x] record the issues on i686, x86, arm64, universal2.
- [x] pytest without libvulkan.
- [x] pull request to ncnn.
