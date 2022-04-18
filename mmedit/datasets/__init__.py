# Copyright (c) OpenMMLab. All rights reserved.
from .base_dataset import BaseDataset
from .base_sr_dataset import BaseSRDataset
from .builder import build_dataloader, build_dataset
from .dataset_wrappers import RepeatDataset
from .registry import DATASETS, PIPELINES
from .sr_folder_multiple_gt_dataset import SRFolderMultipleGTDataset
from .sr_reds_multiple_gt_dataset import SRREDSMultipleGTDataset
from .sr_vimeo90k_multiple_gt_dataset import SRVimeo90KMultipleGTDataset

__all__ = [
    'DATASETS', 'PIPELINES', 'build_dataset', 'build_dataloader',
    'BaseDataset', 'BaseMattingDataset', 'ImgInpaintingDataset',
    'AdobeComp1kDataset', 'SRLmdbDataset', 'SRFolderDataset',
    'SRAnnotationDataset', 'BaseSRDataset', 'RepeatDataset', 'SRREDSDataset',
    'SRVimeo90KDataset', 'BaseGenerationDataset', 'GenerationPairedDataset',
    'GenerationUnpairedDataset', 'SRVid4Dataset', 'SRFolderGTDataset',
    'SRREDSMultipleGTDataset', 'SRVimeo90KMultipleGTDataset',
    'SRTestMultipleGTDataset', 'SRFolderRefDataset', 'SRFacialLandmarkDataset',
    'SRFolderMultipleGTDataset', 'SRFolderVideoDataset', 'BaseVFIDataset',
    'VFIVimeo90KDataset'
]
