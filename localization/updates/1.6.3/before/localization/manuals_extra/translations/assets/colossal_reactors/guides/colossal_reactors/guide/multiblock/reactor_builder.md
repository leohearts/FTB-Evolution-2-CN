---
navigation:
  parent: multiblock/multiblock-index.md
  title: 反应堆建造器
  icon: reactor_builder
  position: 30
item_ids:
  - colossal_reactors:reactor_builder
categories:
  - multiblock
---

# 反应堆建造器

<BlockImage id="reactor_builder" scale="4" />

**反应堆建造器**会使用其缓冲物品栏与储罐中的材料放置**反应堆内部结构与外壳**. 它**不会**放置**反应堆控制器**, **能量端口**或**资源端口**; 参见[入门](getting_started.md).

## 建造会放置的内容(按顺序)

1. **外壳**结构(可选**顶部开放**, 便于之后修改)
2. 每根燃料棒柱上方顶层的**燃料棒控制器**
3. 按内部图案放置的**反应堆燃料棒**
4. 配置后放置的**流体**散热介质(每个格子 1000 mB)
5. 在剩余内部格子放置的**固体**散热介质方块

## 典型流程

1. 将建造器**放置**在预期占地位置(朝向很重要).
2. **打开** GUI: 设置**尺寸**, **燃料棒图案**, **图案模式**, 散热介质类型, 以及需要时的**顶部开放**.
3. **预览**: 紫色边框, 黄色燃料棒位置, 红色 = 无效/多余方块.
4. **标记输入**: 将缓冲槽位分配给特定物品(见按钮提示).
5. 当缓冲物品栏/储罐中有足够材料时**建造**; 若出现红色区域或需要修改则**停止**.
6. **拆除或忽略**建造器方块, 它不属于多方块结构.
7. 建造完成后**手动**添加[控制器, 能量端口和资源端口](getting_started.md): 控制器位于某面墙的**外侧**; 端口位于**同一面**, 替代**玻璃**格子.

建造器中的**模拟**会估算性能与材料数量; 它**不会**启动真正的反应堆.

<GameScene zoom="4" background="transparent">
  <ImportStructure src="/assets/assemblies/minimal_reactor_automation.snbt" />
  <IsometricCamera yaw="210" pitch="25" />
</GameScene>

示例**成品**布局(建造器外壳 + 手动放置的控制器与端口). 标签说明见[入门](getting_started.md).
