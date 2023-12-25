from pathlib import Path

PRETRAINED_MODELS_PATH = {
    # models
    'e4e': '/content/StyleHEAT3D/checkpoints/Encoder_e4e.pth',
    'hfgi': '/content/StyleHEAT3D/checkpoints/hfgi.pth',
    'stylegan2': '/content/StyleHEAT3D/checkpoints/StyleGAN_e4e.pth',
    # editing
    'interfacegan': '/content/StyleHEAT3D/checkpoints/interfacegan_directions/',
    'ganspace': '/content/StyleHEAT3D/checkpoints/ffhq_pca.pt',
    'FFHQ_PCA': '/content/StyleHEAT3D/checkpoints/ffhq_PCA.npz',
    '': '',
    # pretrain
    'discriminator': '/content/StyleHEAT3D/checkpoints/stylegan2_d_256.pth',
    'video_warper': '/content/StyleHEAT3D/checkpoints/video_warper.pth',
    'styleheat': '/content/StyleHEAT3D/checkpoints/StyleHEAT_visual.pt',
    # id_loss
    'irse50': '/content/StyleHEAT3D/checkpoints/model_ir_se50.pth',
    # 3DMM
    'BFM': '/content/StyleHEAT3D/checkpoints/BFM',
    '3DMM': '/content/StyleHEAT3D/checkpoints/Deep3D/epoch_20.pth',
}
