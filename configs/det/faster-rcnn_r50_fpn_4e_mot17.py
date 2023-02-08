USE_MMDET = True
_base_ = ['./faster-rcnn_r50_fpn_4e_mot17-half.py']
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
