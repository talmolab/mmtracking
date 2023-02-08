
# optimizer
optimizer = dict(type='SGD', lr=3e-5, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)
checkpoint_config = dict(interval=1)
#run_num = 21
# yapf:disable
log_config = dict(
    interval=1,
    hooks=[
        dict(type='TextLoggerHook'),
        # dict(type='WandbLoggerHook', 
        #      by_epoch=False,
        #      with_step=True,
        #      init_kwargs={'entity': "aaprasad",  # The entity used to log on Wandb
        #                   'project': "MOTBaselines",  # Project name in WandB
        #                   'name': f'DeepSort_flies13_det_{run_num}',
        #                   'group': 'DeepSort',
        #                   'config': cfg._cfg_dict.to_dict()}
        #     )
    ])
# yapf:enable
dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = None
resume_from = None
workflow = [('train', 1)]

# disable opencv multithreading to avoid system being overloaded
opencv_num_threads = 0
# set multi-process start method as `fork` to speed up the training
mp_start_method = 'fork'
device='cuda'
