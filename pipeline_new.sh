python edit_config.py \
--train_dir /home/workspace/data/train/ \
--eval_dir /home/workspace/data/val/ \
--batch_size 2 \
--checkpoint /home/workspace/experiments/pretrained_model/efficientdet_d1_coco17_tpu-32/checkpoint/ckpt-0 --label_map /home/workspace/experiments/label_map.pbtxt \
--pipeline_src /home/workspace/experiments/pretrained_model/efficientdet_d1_coco17_tpu-32/pipeline.config
