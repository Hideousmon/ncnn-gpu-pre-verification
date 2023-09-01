# ncnn-gpu-pre-verification
### Current ncnn-gpu wheels matrix 

|                       | x86_64 | i686 | x86  | AMD64 | ARM64 | universal2 |
| :-------------------: | :----: | :--: | :--: | :---: | :---: | :--------: |
| ubuntu (cp-manylinux) |   √    |      |  -   |   -   |   -   |     -      |
| ubuntu (cp-musllinux) |        |      |  -   |   -   |   -   |     -      |
|      ubuntu (pp)      |   √    |      |  -   |   -   |   -   |     -      |
|     windows (pp)      |   -    |  -   |  -   |   √   |   -   |     -      |
|     windows (cp)      |   -    |  -   |      |   √   |       |     -      |
|      macos (pp)       |   √    |  -   |  -   |   -   |   -   |     -      |
|      macos (cp)       |   √    |  -   |  -   |   -   |       |            |

### yolov4-tiny inference on windows  (without installing vulkan sdk)

[ncnn_gpu-1.0.20230825-cp38-cp38-win_amd64.whl]

|                  | CPU(3960X) | GPU(AMD RX 580) |
| :--------------: | :--------: | :-------------: |
| time consumption |  51.12ms   |     34.08ms     |

### compare with C++

[ncnn_gpu-1.0.20230825-cp38-cp38-win_amd64.whl]

|        | CPU(6800H) | GPU(3060 Laptop) |
| :----: | :--------: | :--------------: |
|  C++   |  49.24ms   |     13.14ms      |
| Python |  56.62ms   |     14.61ms      |

### TO DO

- [ ] ~~build wheels on i686, x86, arm64, universal2 with vulkan~~.
- [ ] record the issues on i686, x86, arm64, universal2.
- [ ] pytest without libvulkan.
- [ ] pull request to ncnn.