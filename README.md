# pairwise-skybox-cubemap-seam

## 领域

游戏、图形与多媒体

## 主题

天空盒接缝

## 说明

cubemap 面间连续、mip 接缝与曝光统一。

初始状态下 `render/skybox_cubemap_seam.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
