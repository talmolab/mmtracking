USE_MMDET = True
_base_ = ['./faster-rcnn_r50_fpn_4e_mot17-half.py']
model = dict(
    detector=dict(
        backbone=dict(
            depth=101,
            init_cfg=None),
        init_cfg=None))
