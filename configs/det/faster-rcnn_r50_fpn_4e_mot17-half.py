USE_MMDET = True
_base_ = [
    '../_base_/models/faster_rcnn_r50_fpn.py',
    '../_base_/datasets/mot_challenge_det.py', '../_base_/default_runtime.py'
]
model = dict(
    detector=dict(
        rpn_head=dict(bbox_coder=dict(clip_border=False)),
        roi_head=dict(
            bbox_head=dict(bbox_coder=dict(clip_border=False), num_classes=1)),
        init_cfg=None))
# learning policy
lr_config=None
# lr_config = dict(
#     policy='step',
#     warmup='linear',
#     warmup_iters=100,
#     warmup_ratio=1.0 / 100,
#     step=[3])
# runtime settings
total_epochs = 4
