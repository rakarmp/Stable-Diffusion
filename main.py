#@markdown #<font color="#7FFF00">***ALTERNATIFE STABLE DIFFUSION***</font>
#Import modul
from datetime        import datetime
from IPython.display import clear_output
import base64

#Cek HDD
print('Cek HDD ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print('\n')
!df -h

#Cek CPU
print('\n')
print('Cek CPU ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print('\n')
!cat /proc/cpuinfo

#Cek RAM
print('\n')
print('Cek RAM ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print('\n')
!cat /proc/meminfo

#Cek GPU
print('\n')
print('Cek GPU ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print('\n')

#Nvidia
!nvidia-smi

#Decode Base64 untuk menyamarkan agar tidak terdeteksi warning
masbro = base64.b64decode(("d2VidWk=").encode('ascii')).decode('ascii')
bromas = base64.b64decode(("V2ViVUk=").encode('ascii')).decode('ascii')


#@markdown ##***SET UP STABLE DIFFUSION WEBUI***

%cd /content

%env TF_CPP_MIN_LOG_LEVEL=1

#install-ubuntu
!apt -y update -qq
!wget http://launchpadlibrarian.net/367274644/libgoogle-perftools-dev_2.5-2.2ubuntu3_amd64.deb
!wget https://launchpad.net/ubuntu/+source/google-perftools/2.5-2.2ubuntu3/+build/14795286/+files/google-perftools_2.5-2.2ubuntu3_all.deb
!wget https://launchpad.net/ubuntu/+source/google-perftools/2.5-2.2ubuntu3/+build/14795286/+files/libtcmalloc-minimal4_2.5-2.2ubuntu3_amd64.deb
!wget https://launchpad.net/ubuntu/+source/google-perftools/2.5-2.2ubuntu3/+build/14795286/+files/libgoogle-perftools4_2.5-2.2ubuntu3_amd64.deb
!apt install -qq libunwind8-dev
!dpkg -i *.deb
%env LD_PRELOAD=libtcmalloc.so
!rm *.deb

!apt -y install -qq aria2 libcairo2-dev pkg-config python3-dev
!pip install -q torch==1.13.1+cu116 torchvision==0.14.1+cu116 torchaudio==0.13.1 torchtext==0.14.1 torchdata==0.5.1 --extra-index-url https://download.pytorch.org/whl/cu116 -U
!pip install -q xformers==0.0.16 triton==2.0.0 -U

#install-extensions, stable diffusion webui, controlnet, openpose, dan tag/prompt auto complete
!git clone -b v2.1 https://github.com/camenduru/stable-diffusion-$masbro
!git clone https://github.com/vorstcavry/embeddings /content/stable-diffusion-$masbro/embeddings/negative
!git clone https://github.com/vorstcavry/lora /content/stable-diffusion-$masbro/models/Lora/Lora-set
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/embed/upscale/resolve/main/4x-UltraSharp.pth -d /content/stable-diffusion-$masbro/models/ESRGAN -o 4x-UltraSharp.pth
!wget https://raw.githubusercontent.com/camenduru/stable-diffusion-$masbro-scripts/main/run_n_times.py -O /content/stable-diffusion-$masbro/scripts/run_n_times.py
!git clone https://github.com/deforum-art/deforum-for-automatic1111-$masbro /content/stable-diffusion-$masbro/extensions/deforum-for-automatic1111-$masbro
!git -C /content/stable-diffusion-$masbro/extensions/deforum-for-automatic1111-$masbro fetch
!git -C /content/stable-diffusion-$masbro/extensions/deforum-for-automatic1111-$masbro checkout 0056c493e0dd44d2524175564f8fb91e40c94c59
!git clone https://github.com/Klace/stable-diffusion-$masbro-images-browser /content/stable-diffusion-$masbro/extensions/stable-diffusion-$masbro-images-browser
!git clone https://github.com/Iyashinouta/sd-model-downloader /content/stable-diffusion-$masbro/extensions/sd-model-downloader
!git clone https://github.com/camenduru/stable-diffusion-$masbro-huggingface /content/stable-diffusion-$masbro/extensions/stable-diffusion-$masbro-huggingface
!git clone https://github.com/camenduru/sd-civitai-browser /content/stable-diffusion-$masbro/extensions/sd-civitai-browser
!git clone https://github.com/camenduru/sd-$masbro-additional-networks /content/stable-diffusion-$masbro/extensions/sd-$masbro-additional-networks
!git clone https://github.com/Mikubill/sd-$masbro-controlnet /content/stable-diffusion-$masbro/extensions/sd-$masbro-controlnet
!git clone https://github.com/fkunn1326/openpose-editor /content/stable-diffusion-$masbro/extensions/openpose-editor
!git clone https://github.com/jexom/sd-$masbro-depth-lib /content/stable-diffusion-$masbro/extensions/sd-$masbro-depth-lib
!git clone https://github.com/hnmr293/posex /content/stable-diffusion-$masbro/extensions/posex
!git clone https://github.com/DominikDoom/a1111-sd-$masbro-tagcomplete /content/stable-diffusion-$masbro/extensions/tag-autocomplete
!git clone https://github.com/camenduru/sd-$masbro-tunnels /content/stable-diffusion-$masbro/extensions/sd-$masbro-tunnels
!git clone https://github.com/etherealxx/batchlinks-$masbro /content/stable-diffusion-$masbro/extensions/batchlinks-$masbro
!git clone https://github.com/camenduru/stable-diffusion-$masbro-catppuccin /content/stable-diffusion-$masbro/extensions/stable-diffusion-$masbro-catppuccin
!git clone https://github.com/KohakuBlueleaf/a1111-sd-$masbro-locon /content/stable-diffusion-$masbro/extensions/a1111-sd-$masbro-locon/scripts/main.py
!git clone https://github.com/AUTOMATIC1111/stable-diffusion-$masbro-rembg /content/stable-diffusion-$masbro/extensions/stable-diffusion-$masbro-rembg
!git clone https://github.com/camenduru/sd_$masbro_stealth_pnginfo /content/stable-diffusion-$masbro/extensions/sd_$masbro_stealth_pnginfo
!git clone https://github.com/thomasasfk/sd-$masbro-aspect-ratio-helper /content/stable-diffusion-$masbro/extensions/sd-$masbro-aspect-ratio-helper
!git clone https://github.com/tjm35/asymmetric-tiling-sd-$masbro /content/stable-diffusion-$masbro/extensions/asymmetric-tiling-sd-$masbrno
%cd /content/stable-diffusion-$masbro
!git reset --hard
!git -C /content/stable-diffusion-$masbro/repositories/stable-diffusion-stability-ai reset --hard

#install-controlnet
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet/resolve/main/control_canny-fp16.safetensors -d /content/stable-diffusion-$masbro/extensions/sd-$masbro-controlnet/models -o control_canny-fp16.safetensors
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet/resolve/main/control_depth-fp16.safetensors -d /content/stable-diffusion-$masbro/extensions/sd-$masbro-controlnet/models -o control_depth-fp16.safetensors
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet/resolve/main/control_hed-fp16.safetensors -d /content/stable-diffusion-$masbro/extensions/sd-$masbro-controlnet/models -o control_hed-fp16.safetensors
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet/resolve/main/control_mlsd-fp16.safetensors -d /content/stable-diffusion-$masbro/extensions/sd-$masbro-controlnet/models -o control_mlsd-fp16.safetensors
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet/resolve/main/control_normal-fp16.safetensors -d /content/stable-diffusion-$masbro/extensions/sd-$masbro-controlnet/models -o control_normal-fp16.safetensors
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet/resolve/main/control_openpose-fp16.safetensors -d /content/stable-diffusion-$masbro/extensions/sd-$masbro-controlnet/models -o control_openpose-fp16.safetensors
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet/resolve/main/control_scribble-fp16.safetensors -d /content/stable-diffusion-$masbro/extensions/sd-$masbro-controlnet/models -o control_scribble-fp16.safetensors
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet/resolve/main/control_seg-fp16.safetensors -d /content/stable-diffusion-$masbro/extensions/sd-$masbro-controlnet/models -o control_seg-fp16.safetensors
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet/resolve/main/hand_pose_model.pth -d /content/stable-diffusion-$masbro/extensions/sd-$masbro-controlnet/modelse -o hand_pose_model.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet/resolve/main/body_pose_model.pth -d /content/stable-diffusion-$masbro/extensions/sd-$masbro-controlnet/models -o body_pose_model.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet/resolve/main/dpt_hybrid-midas-501f0c75.pt -d /content/stable-diffusion-$masbro/extensions/sd-$masbro-controlnet/models -o dpt_hybrid-midas-501f0c75.pt
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet/resolve/main/mlsd_large_512_fp32.pth -d /content/stable-diffusion-$masbro/extensions/sd-$masbro-controlnet/models -o mlsd_large_512_fp32.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet/resolve/main/mlsd_tiny_512_fp32.pth -d /content/stable-diffusion-$masbro/extensions/sd-$masbro-controlnet/models -o mlsd_tiny_512_fp32.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet/resolve/main/network-bsds500.pth -d /content/stable-diffusion-$masbro/extensions/sd-$masbro-controlnet/models -o network-bsds500.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet/resolve/main/upernet_global_small.pth -d /content/stable-diffusion-$masbro/extensions/sd-$masbro-controlnet/models -o upernet_global_small.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet/resolve/main/t2iadapter_style_sd14v1.pth -d /content/stable-diffusion-$masbro/extensions/sd-$masbro-controlnet/models -o t2iadapter_style_sd14v1.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet/resolve/main/t2iadapter_sketch_sd14v1.pth -d /content/stable-diffusion-$masbro/extensions/sd-$masbro-controlnet/models -o t2iadapter_sketch_sd14v1.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet/resolve/main/t2iadapter_seg_sd14v1.pth -d /content/stable-diffusion-$masbro/extensions/sd-$masbro-controlnet/models -o t2iadapter_seg_sd14v1.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet/resolve/main/t2iadapter_openpose_sd14v1.pth -d /content/stable-diffusion-$masbro/extensions/sd-$masbro-controlnet/models -o t2iadapter_openpose_sd14v1.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet/resolve/main/t2iadapter_keypose_sd14v1.pth -d /content/stable-diffusion-$masbro/extensions/sd-$masbro-controlnet/models -o t2iadapter_keypose_sd14v1.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet/resolve/main/t2iadapter_depth_sd14v1.pth -d /content/stable-diffusion-$masbro/extensions/sd-$masbro-controlnet/models -o t2iadapter_depth_sd14v1.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet/resolve/main/t2iadapter_color_sd14v1.pth -d /content/stable-diffusion-$masbro/extensions/sd-$masbro-controlnet/models -o t2iadapter_color_sd14v1.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet/resolve/main/t2iadapter_canny_sd14v1.pth -d /content/stable-diffusion-$masbro/extensions/sd-$masbro-controlnet/models -o t2iadapter_canny_sd14v1.pth

#membuat folder yang belum tersedia
!mkdir /content/stable-diffusion-$masbro/models/Lora
!mkdir /content/stable-diffusion-$masbro/models/hypernetworks

#install-vae-untuk-model-checkpoint-yang-akan-dipakai
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.ckpt -d /content/stable-diffusion-$masbro/models/VAE -o vae-ft-mse-840000-ema-pruned.ckpt
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/vorstcavry/vaecollection/resolve/main/clearvae_main.safetensors -d /content/stable-diffusion-$masbro/models/VAE -o clearvae_main.safetensors

#install-lora
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/vorstcavry/lora/resolve/main/cuteGirlMix.safetensors -d /content/stable-diffusion-$masbro/models/Lora -o cuteGirlMix.safetensors
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/vorstcavry/lora/resolve/main/chilloutmixlora.safetensors -d /content/stable-diffusion-$masbro/models/Lora -o chilloutmixlora.safetensors
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/vorstcavry/loraasia/resolve/main/japaneseDollLikeness_v15.safetensors -d /content/stable-diffusion-$masbro/models/Lora -o japaneseDollLikeness_v15.safetensors
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/vorstcavry/loraasia/resolve/main/koreanDollLikeness_v20.safetensors -d /content/stable-diffusion-$masbro/models/Lora -o koreanDollLikeness_v20.safetensors
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/vorstcavry/loraasia/resolve/main/taiwanDollLikeness_v15.safetensors -d /content/stable-diffusion-$masbro/models/Lora -o taiwanDollLikeness_v15.safetensors

#intsall-lora-di-additional-networks
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/vorstcavry/lora/resolve/main/cuteGirlMix.safetensors -d /content/stable-diffusion-$masbro/extensions/sd-$masbro-additional-networks/models/lora -o cuteGirlMix.safetensors
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/vorstcavry/lora/resolve/main/chilloutmixlora.safetensors -d /content/stable-diffusion-$masbro/extensions/sd-$masbro-additional-networks/models/lora -o chilloutmixlora.safetensors
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/vorstcavry/loraasia/resolve/main/japaneseDollLikeness_v15.safetensors -d /content/stable-diffusion-$masbro/extensions/sd-$masbro-additional-networks/models/lora -o japaneseDollLikeness_v15.safetensors
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/vorstcavry/loraasia/resolve/main/koreanDollLikeness_v20.safetensors -d /content/stable-diffusion-$masbro/extensions/sd-$masbro-additional-networks/models/lora -o koreanDollLikeness_v20.safetensors
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/vorstcavry/loraasia/resolve/main/taiwanDollLikeness_v15.safetensors -d /content/stable-diffusion-$masbro/extensions/sd-$masbro-additional-networks/models/lora -o taiwanDollLikeness_v15.safetensors

#intsall-Checkpoint

#@markdown ### <font color="#00CED1">**PILIH MODEL**</font>

#@markdown <font color="#CC3E3E">**JANGAN CENTANG SEMUA!!!**</font>
ChillOutMix = True #@param {type:"boolean"}
MeinaPastel = False #@param {type:"boolean"}
PerfectWorld = False #@param {type:"boolean"}
Figure = False #@param {type:"boolean"}
DosMix = False #@param {type:"boolean"}
RevAnimated = False #@param {type:"boolean"}
MeinaMix = False #@param {type:"boolean"}
CyberReal  = False #@param {type:"boolean"}

with open("models.txt", "w") as f:
     if ChillOutMix:
        f.write("https://huggingface.co/AnonPerson/ChilloutMix/resolve/main/ChilloutMix-ni-fp16.safetensors\n"
                " out=ChilloutMix-ni.safetensors\n")
     else:
          pass
     if MeinaPastel:
        f.write("https://huggingface.co/Meina/MeinaPastel/resolve/main/MeinaPastelV4%20-%20Without%20VAE.safetensors\n"
                " out=MeinaPastelV4.safetensors\n")
     else:
          pass
     if PerfectWorld:
        f.write("https://huggingface.co/ckpt/perfect_world/resolve/main/perfectWorld_v2Baked.safetensors\n"
                " out=perfectWorld_v2Baked.safetensors\n")
     else:
          pass
     if Figure :
        f.write("https://huggingface.co/vorstcavry/figurestyle/resolve/main/figure.safetensors\n"
                " out=figure.safetensors\n")
     else:
          pass
     if DosMix :
       f.write("https://huggingface.co/vorstcavry/dosmix/resolve/main/ddosmix_V2.safetensors\n"
                " out=ddosmix_V2.safetensors\n")
     else:
          pass
     if RevAnimated :
       f.write("https://huggingface.co/ckpt/rev-animated/resolve/main/revAnimated_v11.safetensors\n"
                " out=revAnimated_v11.safetensors\n")
     else:
          pass
     if MeinaMix :
       f.write("https://huggingface.co/ckpt/MeinaMix/resolve/main/Meina_V8_baked_VAE.safetensors\n"
                " out=Meina_V8_baked_VAE.safetensors\n")
     else:
          pass
     if CyberReal :
       f.write("https://huggingface.co/ckpt/CyberRealistic/resolve/main/cyberrealistic_v13.safetensors\n"
                " out=cyberrealistic_v13.safetensors\n")
     else:
          pass
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --input-file models.txt -d /content/stable-diffusion-$masbro/models/Stable-diffusion
!rm -rf /content/models.txt


#@markdown (hapus centang model yang tidak dipakai)
#@markdown **CONTOH STYLE GAMBAR ADA DI BAWAH**

#mempersiapkan data
!sed -i -e '''/    prepare_environment()/a\    os.system\(f\"""sed -i -e ''\"s/dict()))/dict())).cuda()/g\"'' /content/stable-diffusion-$masbro/repositories/stable-diffusion-stability-ai/ldm/util.py""")''' /content/stable-diffusion-$masbro/launch.py
!sed -i -e 's/\"sd_model_checkpoint\"\,/\"sd_model_checkpoint\,sd_vae\,CLIP_stop_at_last_layers\"\,/g' /content/stable-diffusion-$masbro/modules/shared.py

!mkdir /content/stable-diffusion-$masbro/extensions/deforum-for-automatic1111-$masbro/models
!sed -i -e 's/\"sd_model_checkpoint\"\,/\"sd_model_checkpoint\,sd_vae\,CLIP_stop_at_last_layers\"\,/g' /content/stable-diffusion-$masbro/modules/shared.py

!python launch.py --listen --xformers --enable-insecure-extension-access --theme dark --gradio-queue --multiple