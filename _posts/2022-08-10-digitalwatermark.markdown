---
layout: post
title:  "数字水印应用"
categories: skill
tags: technology
author: qhmorn
description: 介绍数字水印技术应用
---

数字水印技术
============

<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;数字水印可分为浮现式和隐藏式两种，浮现式：包含的信息，在观看图片或视频时同时被看到；隐藏式：信息以数字的方式加入音频、图片或视频中，无法被看见，阻止数字媒体未经授权的拷贝。
<br>

数字水印程序包含，嵌入器和检测器两个部分。


嵌入时，需要准备：将嵌入水印的载体作品、原始的水印信息。

<br>
检测器有两个操作：
: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;水印检测，它用于判断水印的存在与否
: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;水印提取，它用于从含水印的载体中提取水印信息


<br>
空间域嵌入方案
: 

<br>
变换域嵌入方案
: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;离散傅立叶变换
: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;离散余弦变换
: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;小波变换：时频局部化特征为分析图像的局部特征提供了很好的定位，容易于人类视觉系统相适应

<br>
混沌模型对图像进行变换，得到的图像于原始图像存在视差，从而实现图像加密
: 

<br>
基于量子计算理论的图像水印
: 

_________________

**Steghide**：将文件隐藏到图片或音频中的工具

<br>
*信息写入图片：*
<br>
`steghide embed -cf *.jpg -ef *.txt -p 666888`

*检测信息：*
<br>
`steghide info *.jpg`

*取出信息：*
<br>
`steghide extract -sf *.jpg -p 666888`

***注意：请将 * 替换成实际的文件名***

_________________

<br>

**Steghide软件，下载地址：**

<a href="https://pan.baidu.com/s/1xVsRrlZmBOp-ciC5ixIqEQ?pwd=kyvd" target="_blank" title="百度网盘">百度网盘</a>
