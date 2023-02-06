# BasicVSR_PlusPlus (CVPR 2022)
\[[Paper](https://arxiv.org/abs/2104.13371)\] \[[Project Page](https://ckkelvinchan.github.io/projects/BasicVSR++/)\] \[[Code](https://github.com/open-mmlab/mmediting)\]

This is the official repository for BasicVSR++. Please feel free to raise issue related to BasicVSR++! If you are also interested in [RealBasicVSR](https://github.com/ckkelvinchan/RealBasicVSR), which is also accepted to CVPR 2022, please don't hesitate to star!

**Authors**: [Kelvin C.K. Chan](https://ckkelvinchan.github.io/), [Shangchen Zhou](https://shangchenzhou.com/), [Xiangyu Xu](https://sites.google.com/view/xiangyuxu), [Chen Change Loy](https://www.mmlab-ntu.com/person/ccloy/), *Nanyang Technological University*

**Acknowedgement**: Our work is built upon [MMEditing](https://github.com/open-mmlab/mmediting). Please follow and star this repository and MMEditing!

## News
- 2 Dec 2021: Colab demo released <a href="https://colab.research.google.com/drive/1I0kZMM0DQyb4ueHZw5si8fMnRCJ_eUX3?usp=sharing"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="google colab logo"></a>
- 18 Apr 2022: Code released. Also merged into [MMEditing](https://github.com/open-mmlab/mmediting)
- 5 Feb 2023: The checkpoints for **BasicVSR_2x** is released. 

## TODO
- [ ] Add BasicVSR_2x architecture
- [x] ~~Add BasicVSR_2x checkpoints~~
- [ ] Add data processing scripts
- [x] ~~Add checkpoints for deblur and denoise~~
- [x] ~~Add configs for deblur and denoise~~
- [x] ~~Add Colab demo~~

## Pre-trained Weights
You can find the pre-trained weights for **deblurring** and **denoising** in this [link](https://www.dropbox.com/sh/gopo637rbutlxde/AACGnXDlvQMjwfCey3m2g34za?dl=0). For **super-resolution** and **compressed video enhancement**, please refer to [MMEditing](https://github.com/open-mmlab/mmediting/tree/master/configs/restorers/basicvsr_plusplus).

## Installation
1. Install [PyTorch](https://pytorch.org)
2. `pip install openmim`
3. `mim install mmcv-full`
4. `git clone https://github.com/ckkelvinchan/BasicVSR_PlusPlus.git`
5. `cd BasicVSR_PlusPlus`
6. `pip install -v -e .`

## Inference a Video
1. Download pre-trained weights
2. `python demo/restoration_video_demo.py ${CONFIG} ${CHKPT} ${IN_PATH} ${OUT_PATH}`

For example, you can download the VSR checkpoint [here](https://download.openmmlab.com/mmediting/restorers/basicvsr_plusplus/basicvsr_plusplus_c64n7_8x1_600k_reds4_20210217-db622b2f.pth) to `chkpts/basicvsr_plusplus_reds4.pth`, then run
```
python demo/restoration_video_demo.py configs/basicvsr_plusplus_reds4.py chkpts/basicvsr_plusplus_reds4.pth data/demo_000 results/demo_000
```
You can also replace `${IN_PATH} ${OUT_PATH}` by your video path (e.g., `xxx/yyy.mp4`) to input/output videos.

## Training Models
1. Put the dataset in the designated locations specified in the configuration file.
2. `sh tools/dist_train.sh ${CONFIG} ${NGPUS}`

## Data Preprocessing
To be added...

## Related Work
**Our BasicVSR series:**
1. [BasicVSR: The Search for Essential Components in Video Super-Resolution and Beyond](https://ckkelvinchan.github.io/projects/BasicVSR), CVPR 2021
2. [Investigating Tradeoffs in Real-World Video Super-Resolution](https://github.com/ckkelvinchan/RealBasicVSR), CVPR 2022

**More about deformable alignment:**
- [Understanding Deformable Alignment in Video Super-Resolution](https://ckkelvinchan.github.io/projects/DCN), AAAI 2021


## Citations
```
@inproceedings{chan2022basicvsrpp,
  author = {Chan, Kelvin C.K. and Zhou, Shangchen and Xu, Xiangyu and Loy, Chen Change},
  title = {{BasicVSR++}: Improving video super-resolution with enhanced propagation and alignment},
  booktitle = {IEEE Conference on Computer Vision and Pattern Recognition},
  year = {2022}
}
```
```
@article{chan2022generalization,
  title={On the Generalization of {BasicVSR++} to Video Deblurring and Denoising},
  author={Chan, Kelvin CK and Zhou, Shangchen and Xu, Xiangyu and Loy, Chen Change},
  journal={arXiv preprint arXiv:2204.05308},
  year={2022}
}
```
