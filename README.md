<div align="center">

# SenseSI: Scaling Spatial Intelligence with Multimodal Foundation Models

</div>

<div align="center">


English | [简体中文](README_CN.md) 

<p align="center">
    <a href="https://huggingface.co/collections/sensenova/sensesi" target="_blank">
        <img alt="SenseSI" src="https://img.shields.io/badge/%F0%9F%A4%97%20_SenseSI-Models-ffc107?color=ffc107&logoColor=white" height="20" />
    </a>
    <a href="https://huggingface.co/spaces/lmms-lab-si/EASI-Leaderboard" target="_blank">
        <img alt="Leaderboard" src="https://img.shields.io/badge/%F0%9F%A4%97%20_EASI-Leaderboard-ffc107?color=ffc107&logoColor=white" height="20" />
    </a>
    <a href="https://github.com/EvolvingLMMs-Lab/EASI" target="_blank">
        <img alt="Code" src="https://img.shields.io/badge/EASI-Code-100000?style=flat-square&logo=github&logoColor=white" height="20" />
    </a>
    <a href="https://github.com/OpenSenseNova/SenseSI/blob/main/LICENSE"><img src="https://img.shields.io/github/license/OpenSenseNova/SenseSI?style=flat"></a>
</p>

</div>


## Overview
Despite remarkable progress, leading multimodal models still exhibit notable deficiencies in spatial intelligence:
the ability to make metric estimations, understand spatial relationships, handle viewpoint changes, and integrate information across complex scenes.
We take a scaling perspective: constructing and curating a large-scale, comprehensive collection of spatial intelligence data, 
and through continued training on powerful multimodal foundations, 
cultivating multi-faceted spatial understanding within the SenseSI family of models.
*In the future, SenseSI will be integrated with larger-scale in-house models.*

## Release Information
Currently, we build SenseSI upon popular open-source foundation models to maximize compatibility with existing research pipelines.
In this release, we present 
[**SenseSI-InternVL3-2B**](https://huggingface.co/sensenova/SenseSI-InternVL3-2B) and 
[**SenseSI-InternVL3-8B**](https://huggingface.co/sensenova/SenseSI-InternVL3-8B), 
which achieve state-of-the-art performance among open-source models of comparable size across four recent spatial intelligence benchmarks: 
**VSI**, **MMSI**, **MindCube**, and **ViewSpatial**.

<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>VSI</th>
      <th>MMSI</th>
      <th>MindCube-Tiny</th>
      <th>ViewSpatial</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#F2F0EF;color:#6b7280;font-weight:700;text-align:center;">
      <td colspan="5"><em>Open-source Models (~2B)</em></td>
    </tr>
    <tr>
      <td>InternVL3-2B</td><td>32.98</td><td>26.50</td><td>37.50</td><td>32.56</td>
    </tr>
    <tr>
      <td>Qwen3-VL-2B-Instruct</td><td>50.36</td><td>28.90</td><td>34.52</td><td>36.97</td>
    </tr>
    <tr>
      <td>MindCube-3B-RawQA-SFT</td><td>17.24</td><td>1.70</td><td>51.73</td><td>24.14</td>
    </tr>
    <tr>
      <td>MindCube-3B-Aug-CGMap-FFR-Out-SFT</td><td>29.60</td><td>29.10</td><td>41.06</td><td>30.90</td>
    </tr>
    <tr>
      <td>MindCube-3B-Plain-CGMap-FFR-Out-SFT</td><td>29.93</td><td>30.40</td><td>39.90</td><td>31.20</td>
    </tr>
    <tr>
      <td>SpatialLadder-3B</td><td>44.86</td><td>27.40</td><td>43.46</td><td>39.85</td>
    </tr>
    <tr>
      <td>SpatialMLLM-4B</td><td>45.98</td><td>26.10</td><td>33.46</td><td>34.66</td>
    </tr>
    <tr>
      <td><strong>SenseSI-InternVL3-2B</strong></td>
      <td><strong>58.47</strong></td>
      <td><strong>35.50</strong></td>
      <td><strong>71.35</strong></td>
      <td><strong>40.62</strong></td>
    </tr>
    <tr style="background:#F2F0EF;color:#6b7280;font-weight:700;text-align:center;">
      <td colspan="5"><em>Open-source Models (~8B)</em></td>
    </tr>
    <tr>
      <td>InternVL3-8B</td><td>42.14</td><td>28.00</td><td>41.54</td><td>38.66</td>
    </tr>
    <tr>
      <td>Qwen3-VL-8B-Instruct</td><td>57.90</td><td>31.10</td><td>29.42</td><td>42.20</td>
    </tr>
    <tr>
      <td>BAGEL-7B</td><td>30.90</td><td>33.10</td><td>34.71</td><td>41.32</td>
    </tr>
    <tr>
      <td>SpaceR-7B</td><td>36.29</td><td>27.40</td><td>37.98</td><td>35.85</td>
    </tr>
    <tr>
      <td>ViLaSR-7B</td><td>44.63</td><td>30.20</td><td>35.10</td><td>35.71</td>
    </tr>
    <tr>
      <td><strong>SenseSI-InternVL3-8B</strong></td>
      <td><strong>62.80</strong></td>
      <td><strong>37.90</strong></td>
      <td><strong>89.33</strong></td>
      <td><strong>53.92</strong></td>
    </tr>
    <tr style="background:#F2F0EF;color:#6b7280;font-weight:600;text-align:center;">
      <td colspan="5"><em>Proprietary Models</em></td>
    </tr>
    <tr style="color:#6b7280;">
      <td>Gemini-2.5-pro-2025-06</td><td>53.57</td><td>38.00</td><td>57.60</td><td>46.06</td>
    </tr>
    <tr style="color:#6b7280;">
      <td>Grok-4-2025-07-09</td><td>47.92</td><td>37.80</td><td>63.56</td><td>43.23</td>
    </tr>
    <tr style="color:#6b7280;">
      <td>GPT-5-2025-08-07</td><td>55.03</td><td>41.80</td><td>56.30</td><td>45.59</td>
    </tr>
  </tbody>
</table>




## 🛠️ QuickStart

### Installation

TBA

### Examples


```python
model_path = "sensenova/SenseSI-InternVL3-8B"
tokenizer = AutoTokenizer.from_pretrained(model_path）
model = AutoModel.from_pretrained(model_path,torch_dtype=torch.bfloat16,low_cpu_mem_usage=True,use_flash_attn=True,trust_remote_code=True).eval().cuda()
```


### Evaluation

To reproduce the results above, please refer to [EASI](https://github.com/EvolvingLMMs-Lab/EASI) to evaluate SenseSI on mainstream spatial intelligence benchmarks.


## What's next?

We will release the accompanying technical report shortly. Please stay tuned!