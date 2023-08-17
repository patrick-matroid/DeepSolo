





# Pretrain ic15 

python tools/train_net.py --config-file configs/R_50/IC15/pretrain_150k_tt_mlt_13_15_textocr_generic.yaml --eval-only MODEL.WEIGHTS ckpts/res50_pretrain_synth-tt-mlt-13-15-textocr.pth

python tools/train_net.py --config-file configs/R_50/IC15/pretrain_150k_tt_mlt_13_15_textocr_weak.yaml --eval-only MODEL.WEIGHTS ckpts/res50_pretrain_synth-tt-mlt-13-15-textocr.pth

python tools/train_net.py --config-file configs/R_50/IC15/pretrain_150k_tt_mlt_13_15_textocr_strong.yaml --eval-only MODEL.WEIGHTS ckpts/res50_pretrain_synth-tt-mlt-13-15-textocr.pth



python tools/train_net.py --config-file configs/ViTAEv2_S/IC15/pretrain_150k_tt_mlt_13_15_textocr_generic.yaml --eval-only MODEL.WEIGHTS ckpts/vitaev2-s_pretrain_synth-tt-mlt-13-15-textocr.pth

python tools/train_net.py --config-file configs/ViTAEv2_S/IC15/pretrain_150k_tt_mlt_13_15_textocr_weak.yaml --eval-only MODEL.WEIGHTS ckpts/vitaev2-s_pretrain_synth-tt-mlt-13-15-textocr.pth

python tools/train_net.py --config-file configs/ViTAEv2_S/IC15/pretrain_150k_tt_mlt_13_15_textocr_strong.yaml --eval-only MODEL.WEIGHTS ckpts/vitaev2-s_pretrain_synth-tt-mlt-13-15-textocr.pth


# Pretrain total-text

python tools/train_net.py --config-file configs/R_50/TotalText/pretrain_150k_tt_mlt_13_15_textocr.yaml --eval-only MODEL.WEIGHTS ckpts/res50_pretrain_synth-tt-mlt-13-15-textocr.pth

python tools/train_net.py --config-file configs/ViTAEv2_S/TotalText/pretrain_150k_tt_mlt_13_15_textocr.yaml --eval-only MODEL.WEIGHTS ckpts/vitaev2-s_pretrain_synth-tt-mlt-13-15-textocr.pth





# Finetune for ic15 

## Res 50 

### from ic15
python tools/train_net.py --config-file configs/R_50/IC15/finetune_150k_tt_mlt_13_15_textocr_generic.yaml --eval-only MODEL.WEIGHTS ckpts/ic15_res50_finetune_synth-tt-mlt-13-15-textocr.pth

python tools/train_net.py --config-file configs/R_50/IC15/finetune_150k_tt_mlt_13_15_textocr_strong.yaml --eval-only MODEL.WEIGHTS ckpts/ic15_res50_finetune_synth-tt-mlt-13-15-textocr.pth

python tools/train_net.py --config-file configs/R_50/IC15/finetune_150k_tt_mlt_13_15_textocr_weak.yaml --eval-only MODEL.WEIGHTS ckpts/ic15_res50_finetune_synth-tt-mlt-13-15-textocr.pth

### from tt
python tools/train_net.py --config-file configs/R_50/IC15/finetune_from_tt_150k_tt_mlt_13_15_textocr_generic.yaml --eval-only MODEL.WEIGHTS ckpts/tt_res50_finetune_synth-tt-mlt-13-15-textocr.pth

python tools/train_net.py --config-file configs/R_50/IC15/finetune_from_tt_150k_tt_mlt_13_15_textocr_strong.yaml --eval-only MODEL.WEIGHTS ckpts/tt_res50_finetune_synth-tt-mlt-13-15-textocr.pth

python tools/train_net.py --config-file configs/R_50/IC15/finetune_from_tt_150k_tt_mlt_13_15_textocr_weak.yaml --eval-only MODEL.WEIGHTS ckpts/tt_res50_finetune_synth-tt-mlt-13-15-textocr.pth

## VIT

### from ic15
python tools/train_net.py --config-file configs/ViTAEv2_S/IC15/finetune_150k_tt_mlt_13_15_textocr_strong.yaml --eval-only MODEL.WEIGHTS ckpts/ic15_vitaev2-s_finetune_synth-tt-mlt-13-15-textocr.pth

python tools/train_net.py --config-file configs/ViTAEv2_S/IC15/finetune_150k_tt_mlt_13_15_textocr_weak.yaml --eval-only MODEL.WEIGHTS ckpts/ic15_vitaev2-s_finetune_synth-tt-mlt-13-15-textocr.pth

python tools/train_net.py --config-file configs/ViTAEv2_S/IC15/finetune_150k_tt_mlt_13_15_textocr_generic.yaml --eval-only MODEL.WEIGHTS ckpts/ic15_vitaev2-s_finetune_synth-tt-mlt-13-15-textocr.pth

### from tt
python tools/train_net.py --config-file configs/ViTAEv2_S/IC15/finetune_from_tt_150k_tt_mlt_13_15_textocr_strong.yaml --eval-only MODEL.WEIGHTS ckpts/tt_vitaev2-s_finetune_synth-tt-mlt-13-15-textocr.pth

python tools/train_net.py --config-file configs/ViTAEv2_S/IC15/finetune_from_tt_150k_tt_mlt_13_15_textocr_weak.yaml --eval-only MODEL.WEIGHTS ckpts/tt_vitaev2-s_finetune_synth-tt-mlt-13-15-textocr.pth

python tools/train_net.py --config-file configs/ViTAEv2_S/IC15/finetune_from_tt_150k_tt_mlt_13_15_textocr_generic.yaml --eval-only MODEL.WEIGHTS ckpts/tt_vitaev2-s_finetune_synth-tt-mlt-13-15-textocr.pth




# Finetune for tt

## Res 50

### from tt
python tools/train_net.py --config-file configs/R_50/TotalText/finetune_150k_tt_mlt_13_15_textocr.yaml --eval-only MODEL.WEIGHTS ckpts/tt_res50_finetune_synth-tt-mlt-13-15-textocr.pth
### from ic15
python tools/train_net.py --config-file configs/R_50/TotalText/finetune_from_ic15_150k_tt_mlt_13_15_textocr.yaml --eval-only MODEL.WEIGHTS ckpts/ic15_res50_finetune_synth-tt-mlt-13-15-textocr.pth
## VIT

### from tt
python tools/train_net.py --config-file configs/ViTAEv2_S/TotalText/finetune_150k_tt_mlt_13_15_textocr.yaml --eval-only MODEL.WEIGHTS ckpts/tt_vitaev2-s_finetune_synth-tt-mlt-13-15-textocr.pth
### from ic15

python tools/train_net.py --config-file configs/ViTAEv2_S/TotalText/finetune_from_ic15_150k_tt_mlt_13_15_textocr.yaml --eval-only MODEL.WEIGHTS ckpts/ic15_vitaev2-s_finetune_synth-tt-mlt-13-15-textocr.pth