python edit_config.py \
--train_dir /home/workspace/data/train/ \
--eval_dir /home/workspace/data/val/ \
--batch_size 2 \
--checkpoint /home/workspace/experiments/pretrained_model/faster_rcnn_resnet101_v1_640x640_coco17_tpu-8/checkpoint/ckpt-0 --label_map /home/workspace/experiments/label_map.pbtxt \
--pipeline_src /home/workspace/experiments/pretrained_model/faster_rcnn_resnet101_v1_640x640_coco17_tpu-8/pipeline.config
