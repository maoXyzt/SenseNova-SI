<div align="center">

# SenseSI: 探索空间智能在多模态基础模型上尺度效应

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


## 概览
尽管多模态学习取得了显著进展，当前主流模型在空间智能方面仍存在明显不足，
包括对尺度关系的估计、空间结构的理解、视角变化的处理，以及复杂场景中信息的整合等能力。
我们从尺度效应（Scaling）视角出发，构建并整理了一个大规模且多样化的空间智能数据集，
并在强大的多模态基础模型上持续训练，从而在 SenseSI 模型家族中观察到复合的空间智能。
*后续 SenseSI 将与更大规模的内部模型进行集成。*

## 发布信息
目前，我们基于流行的开源基础模型构建 SenseSI，以最大化与现有研究流程的兼容性。
在本次发布中，我们推出
[**SenseSI-InternVL3-2B**](https://huggingface.co/sensenova/SenseSI-InternVL3-2B) 与 
[**SenseSI-InternVL3-8B**](https://huggingface.co/sensenova/SenseSI-InternVL3-8B), 
在四个近期发布的空间智能基准测试（**VSI**、**MMSI**、**MindCube**、**ViewSpatial**）上，
在同等模型规模下均取得了开源模型的最新最优性能（state-of-the-art）。

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




## 🛠️ 快速上手

### 安装

TBA

### 示例

#### 单图多选题

该例题源自[SITE-Bench](https://wenqi-wang20.github.io/SITE-Bench.github.io/)的`MultiV`子集:

```bash
python example.py \
  --image_paths examples/Q1_1.png \
  --question "<image>\nWhich figure is a top-down view of the given shape?\nOptions:\nA: A\nB: B\nC: C\nD: D" \
  --model_path sensenova/SenseSI-InternVL3-8B 
# --model_path OpenGVLab/InternVL3-8B 
```

题目:
<!-- Example 1 -->
<div style="border:1px solid #e5e7eb; border-radius:12px; padding:16px; margin:16px 0;">
  <div style="font-weight:600; font-size:16px; margin-bottom:8px;">
    Example 1 · Single Image
  </div>

  <div style="margin:8px 0 12px;">
    <strong>Q:</strong> Which figure is a top-down view of the given shape?\nOptions:\nA: A\nB: B\nC: C\nD: D
  </div>

  <div align="center" style="margin:8px 0;">
    <img src="./examples/Q1_1.png" alt="Example 1 image" style="max-width:100%; height:auto;">
  </div>
</div>

#### 多图多选题

该例题源自[MindCube](https://mind-cube.github.io/)的`Rotation`子集:

```bash
python example.py \
  --image_paths examples/Q2_1.png examples/Q2_2.png \
  --question "<image><image>\nBased on these two views showing the same scene: in which direction did I move from the first view to the second view?\nDirectly left B. Directly right C. Diagonally forward and right D. Diagonally forward and left" \
  --model_path sensenova/SenseSI-InternVL3-8B 
# --model_path OpenGVLab/InternVL3-8B
```

题目:
<!-- Example 2 -->
<div style="border:1px solid #e5e7eb; border-radius:12px; padding:16px; margin:16px 0;">

  <div style="margin:8px 0 12px;">
    <strong>Q:</strong> Based on these two views showing the same scene: in which direction did I move from the first view to the second view?\nDirectly left B. Directly right C. Diagonally forward and right D. Diagonally forward and left
  </div>
  <table>
    <tr>
      <td align="center" width="50%" style="padding:4px;">
        <img src="./examples/Q2_1.png" alt="Image A" width="100%">
      </td>
      <td align="center" width="50%" style="padding:4px;">
        <img src="./examples/Q2_2.png" alt="Image B" width="100%">
      </td>
    </tr>
  </table>
</div>

#### 批量测试

构建类似于[examples/examples.jsonl](examples/examples.jsonl)的文件，每一行代表一个问题。
模型只加载一次，按逐行的顺序逐个回答问题，问题之间互不干扰。
> `jsonl`更详细的格式可以参考[单图数据](https://internvl.readthedocs.io/en/latest/get_started/chat_data_format.html#single-image-data)和[多图数据](https://internvl.readthedocs.io/en/latest/get_started/chat_data_format.html#multi-image-data)

```bash
python example.py \
  --jsonl_path examples/examples.jsonl \
  --model_path sensenova/SenseSI-InternVL3-8B 
# --model_path OpenGVLab/InternVL3-8B 
```

### 评测

如需复现上述结果，请参考 [EASI](https://github.com/EvolvingLMMs-Lab/EASI) 在主流空间智能基准上评估 SenseSI 的表现。


## 后续计划

我们将于近期发布配套的技术报告，敬请期待。