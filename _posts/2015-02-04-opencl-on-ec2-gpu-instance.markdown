---
author:
  email: suminb@gmail.com
  first_name: Sumin
  last_name: Byeon
categories:
- Programming
- Tutorial
layout: post
meta: null
published: false
redirect_from:
- /post/opencl-on-ec2-gpu-instance
status: publish
tags: []
title: Amazon EC2 GPU 인스턴스에서 OpenCL 사용하기
type: post
---

아마존 EC2 GPU 인스턴스에서 OpenCL 실행 환경을 구축하면서 해결한 문제들을 정리해보았다.

EC2 인스턴스 준비
-----------------

[AWS 콘솔][]에서 머신 이미지(AMI)를 고를 때 다음 이미지를 사용했다.

    ubuntu/images/hvm-ssd/ubuntu-utopic-14.10-amd64-server-20141204

AMI ID는 `ami-02707d03`이다.

가상화 형태는 paravirtualization이 아닌 HVM이어야 GPU 인스턴스를 선택할 수 있도록 되어있는데, 그 이유는 나도 잘 모르겠다.


NVIDIA 드라이버 설치
--------------------

먼저, 시스템에 설치된 그래픽 카드 종류를 알아야 한다.

    $ lspci | grep VGA
    00:02.0 VGA compatible controller: Cirrus Logic GD 5446
    00:03.0 VGA compatible controller: NVIDIA Corporation GK104GL [GRID K520] (rev a1)

그래픽 카드 종류를 알았으니 [NVIDIA 드라이버 다운로드 페이지](http://www.nvidia.com/Download/index.aspx?lang=en-us)에서 적절한 드라이버를 다운로드 한다.

    $ sudo ./NVIDIA-Linux-x86_64-346.35.run

이렇게 설치를 시도하면 다음과 같은 에러 메세지를 볼 수 있다.

    ERROR: Unable to load the kernel module 'nvidia.ko'. This happens most
    frequently when this kernel module was built against the wrong or
    improperly configured kernel sources, with a version of gcc that differs
    from the one used to build the target kernel, or if a driver such as
    rivafb, nvidiafb, or nouveau is present and prevents the NVIDIA kernel
    module from obtaining ownership of the NVIDIA graphics device(s), or no
    NVIDIA GPU installed in this system is supported by this NVIDIA Linux
    graphics driver release.

`dmesg`를 보면 다음과 같은 메세지를 볼 수 있다.

    nvidia: module verification failed: signature and/or  required key missing - tainting kernel

이것 때문에 한참동안 고생하다가 겨우 [실마리가 될만한 글](https://devtalk.nvidia.com/default/topic/547588/linux/error-installing-nvidia-drivers-on-x86_64-amazon-ec2-gpu-cluster-t20-gpu-/post/4321421/#4321421)을 찾았다.

`linux-image-extra-virtual` 패키지를 설치하면 그런 문제가 더이상 나타나지 않는다.

    $ sudo apt-get install linux-image-extra-virtual

이 패키지를 먼저 설치하고 NVIDIA 드라이버를 설치하면 된다.


PyOpenCL 실행 환경 구축
-----------------------

(TODO: Complete this section)


예제 코드 실행시켜보기
----------------------

(TODO: Complete this section)

OpenCL 1.2
----------

(TODO: Complete this section)

그 이외의 정보
--------------

    1 OpenCL Platforms found

     CL_PLATFORM_NAME:      NVIDIA CUDA
     CL_PLATFORM_VERSION:   OpenCL 1.1 CUDA 7.0.19
    OpenCL Device Info:

     1 devices found supporting OpenCL on: NVIDIA CUDA

     ----------------------------------
     Device GRID K520
     ---------------------------------
      CL_DEVICE_NAME:                       GRID K520
      CL_DEVICE_VENDOR:                     NVIDIA Corporation
      CL_DRIVER_VERSION:                    346.35
      CL_DEVICE_TYPE:                       CL_DEVICE_TYPE_GPU
      CL_DEVICE_MAX_COMPUTE_UNITS:          8
      CL_DEVICE_MAX_WORK_ITEM_DIMENSIONS:   3
      CL_DEVICE_MAX_WORK_ITEM_SIZES:        1024 / 1024 / 64
      CL_DEVICE_MAX_WORK_GROUP_SIZE:        1024
      CL_DEVICE_MAX_CLOCK_FREQUENCY:        797 MHz
      CL_DEVICE_ADDRESS_BITS:               32
      CL_DEVICE_MAX_MEM_ALLOC_SIZE:         1023 MByte
      CL_DEVICE_GLOBAL_MEM_SIZE:            4095 MByte
      CL_DEVICE_ERROR_CORRECTION_SUPPORT:   no
      CL_DEVICE_LOCAL_MEM_TYPE:             local
      CL_DEVICE_LOCAL_MEM_SIZE:             47 KByte
      CL_DEVICE_MAX_CONSTANT_BUFFER_SIZE:   64 KByte
      CL_DEVICE_QUEUE_PROPERTIES:           CL_QUEUE_OUT_OF_ORDER_EXEC_MODE_ENABLE
      CL_DEVICE_QUEUE_PROPERTIES:           CL_QUEUE_PROFILING_ENABLE
      CL_DEVICE_IMAGE_SUPPORT:              1
      CL_DEVICE_MAX_READ_IMAGE_ARGS:        256
      CL_DEVICE_MAX_WRITE_IMAGE_ARGS:       16

      CL_DEVICE_IMAGE <dim>                 2D_MAX_WIDTH     32768
                                            2D_MAX_HEIGHT    32768
                                            3D_MAX_WIDTH     4096
                                            3D_MAX_HEIGHT    4096
                                            3D_MAX_DEPTH     4096
      CL_DEVICE_PREFERRED_VECTOR_WIDTH_<t>  CHAR 1, SHORT 1, INT 1, FLOAT 1, DOUBLE 1


    clDeviceQuery, Platform Name = NVIDIA CUDA, Platform Version = OpenCL 1.1 CUDA 7.0.19, NumDevs = 1, Device = GRID K520

    System Info:

     Local Time/Date =  10:31:20, 02/04/2015
     CPU Name: Intel(R) Xeon(R) CPU E5-2670 0 @ 2.60GHz
     # of CPU processors: 8
     Linux version 3.16.0-30-generic (buildd@komainu) (gcc version 4.9.1 (Ubuntu 4.9.1-16ubuntu6) ) #40-Ubuntu SMP Mon Jan 12 22:06:37 UTC 2015



[AWS 콘솔]: http://console.aws.amazon.com
[버그 리포트]: https://bugs.launchpad.net/ubuntu/+source/ubuntu-drivers-common/+bug/1310489