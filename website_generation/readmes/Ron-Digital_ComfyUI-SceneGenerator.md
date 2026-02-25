# ComfyUI-SceneGenerator

ComfyUI-SceneGenerator, JSON dosyalarından sahne önizleme fotoğrafları oluşturmak için kullanılan bir ComfyUI eklentisidir. Bu eklenti, verilen JSON yapılandırmasına göre sahneleri oluşturur ve iki farklı görüntü çıktısı üretir: biri yalnızca ürünleri içerir, diğeri ise hem ürünleri hem de "props"ları içerir.

![ComfyUI-SceneGenerator](demo.png)

## Kurulum

### Adımlar

1. Bu repoyu klonlayın:
    ```sh

    git clone https://github.com/username/ComfyUI-SceneGenerator.git

    cd ComfyUI-SceneGenerator

    ```

2. Gerekli Python paketlerini yükleyin:
    ```sh
    pip install -r requirements.txt
    ```

3. `ComfyUI` kurulumunuzu güncelleyin ve bu eklentiyi tanıyacak şekilde yapılandırın. 

## Kullanım

ComfyUI-SceneGenerator, JSON yapılandırmasını kullanarak sahne önizlemeleri oluşturur. 

### Örnek JSON

Aşağıda örnek bir JSON yapılandırması bulunmaktadır:

```json
{
    "json_img": {
        "stage": {
            "width": 1024,
            "height": 1024
        },
        "json": [
            {
                "config": {
                    "width": 832,
                    "height": 844,
                    "x": -1221.8473873472615,
                    "y": 65.87637986788866,
                    "z": 0,
                    "flip": "[1,1]",
                    "rotation": 0,
                    "src": "https://example.com/image1.png",
                    "name": "fire",
                    "scale": {
                        "x": 0.7592784445653415,
                        "y": 0.7592784445653414
                    },
                    "p_type": "prop"
                }
            },
            {
                "config": {
                    "width": 169,
                    "height": 600,
                    "x": 458.3287536766208,
                    "y": 196.23299366788603,
                    "z": 3,
                    "flip": "[1,1]",
                    "rotation": 29,
                    "src": "https://example.com/image5.png",
                    "name": "tube of cream",
                    "scale": {
                        "x": 1.1271834266188345,
                        "y": 1.1271834266188288
                    },
                    "p_type": "product"
                }
            }
        ]
    }
}
