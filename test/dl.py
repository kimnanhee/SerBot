#%%
'''
import urllib.request

url = "https://github.com/pytorch/hub/tree/master/images/dog.jpg"
fname = "dog.jpg"

try:
    urllib.request.urlretrieve(url, fname)
except Exception as e:
    print(e)
'''
# %%
import torch
import torchvision.models as models
# %%
model = models.segmentation.deeplabv3_resnet101(pretrained=True)
model.eval()
# %%
from PIL import Image
from torchvision import transforms

input_image = Image.open("dog.jpg")
preprocess = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

input_tensor = preprocess(input_image)
input_batch = input_tensor.unsqueeze(0)

if torch.cuda.is_available():
    input_batch = input_batch.to('cuda')
    model.to('cuda')
with torch.no_grad():
    output = model(input_batch)['out'][0] # 0번은 결과, 1번은 파라미터

output_predictions = output.argmax(0)
palette = torch.tensor([2 ** 25 -1, 2 ** 15 -1, 2 ** 21 -1])
colors = torch.as_tensor([i for i in range(21)])[:, None] * palette
colors = (colors % 255).numpy().astype("uint8")

r = Image.fromarray(output_predictions.byte().cpu().numpy()).resize(input_image.size)
r.putpalette(colors)

import matplotlib.pyplot as plt
plt.imshow(r)
plt.show()
# %%
