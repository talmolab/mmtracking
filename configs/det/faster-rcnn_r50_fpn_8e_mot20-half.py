USE_MMDET = True
_base_ = ['./faster-rcnn_r50_fpn_4e_mot17-half.py']
model = dict(
    detector=dict(
        rpn_head=dict(bbox_coder=dict(clip_border=True)),
        roi_head=dict(
            bbox_head=dict(bbox_coder=dict(clip_border=True), num_classes=1))))
# data
data_root = 'talmodata-smb/aadi/tracking_transformers/tracking_transformers/baselines/data/flies_13_coco/det/'
data = dict(
    train=dict(
        ann_file=data_root + 'annotations/flies_13_train_cocov2.json',
        img_prefix=data_root + 'train'),
    val=dict(
        ann_file=data_root + 'annotations/flies_13_val_coco_v2.json',
        img_prefix=data_root + 'val'),
    test=dict(
        ann_file=data_root + 'annotations/flies_13_test_cocov2.json',
        img_prefix=data_root + 'test'))
# learning policy
lr_config=None
# lr_config = dict(
#     policy='step',
#     warmup='linear',
#     warmup_iters=100,
#     warmup_ratio=1.0 / 100,
#     step=[6])
# runtime settings
total_epochs = 8
