---
navigation:
  parent: turbine/turbine-index.md
  title: 涡轮机资源端口
  icon: turbine_resource_port
  position: 35
item_ids:
  - colossal_reactors:turbine_resource_port
categories:
  - ports
---

# 涡轮机资源端口

<BlockImage id="turbine_resource_port" scale="4" />

将**涡轮机资源端口**安装到外壳上, 以在管道/储罐与涡轮机之间输送**蒸汽**, **水**及其他整合包允许的流体.

典型布局: 与[涡轮机控制器](turbine_controller.md)同一面上有**两个资源端口 + 一个能量端口**, 见[入门](getting_started.md). 悬停下方场景中的菱形标记.

<GameScene zoom="6" interactive={true} background="transparent">
  <ImportStructure src="/assets/assemblies/minimal_turbine.snbt" />
  <IsometricCamera yaw="200" pitch="28" />
  <BlockAnnotation x="1" y="2" z="0" color="#55ffff">
**示例: 蒸汽输入**: **Insert** 模式, 启用 **Liquid**. 提示: *将蒸汽(及其他允许的流体)抽入涡轮机.*
  </BlockAnnotation>
  <BlockAnnotation x="5" y="2" z="0" color="#5599ff">
**示例: 水输出**: **Extract** 模式, 启用 **Liquid**. 提示: *将水或排出流体输送至管道.*
  </BlockAnnotation>
</GameScene>

将来自[裂变反应堆](../multiblock/getting_started.md)(或任意蒸汽源)的蒸汽接入 **INSERT** 端口. 将**水/排出物**从 **EXTRACT** 端口输出. 涡轮机能使用多少取决于你的叶片, 见[蒸汽, RF 与线圈](turbine_generation_and_coils.md).

## GUI: 按钮与提示

涡轮机端口使用与反应堆端口相同的界面布局, 但**没有 Solid 行**, 也**没有燃料/冷却剂过滤器**. 在游戏内悬停每个控件, 下方文字与默认提示一致.

### 模式(顶部按钮, 点击循环)

| 标签 | 提示 |
|-------|---------|
| **Insert** | 将蒸汽(及其他允许的流体)抽入涡轮机. |
| **Extract** | 将水或排出流体输送至管道. |
| **Eject** | 将端口储罐内的流体排到外部. |

### 介质开关(点击启用, 激活时带下划线)

| 按钮 | 提示 |
|--------|---------|
| **Liquid** | 点击以允许或阻止流体通过此端口. |
| **Gas** | 点击以允许或阻止 Mekanism 气体通过此端口. |

### 储罐与清空

| 控件 | 提示 |
|---------|---------|
| **液体储罐**(悬停条) | 液体: 数量/容量 mB, 以及流体名称 |
| **气体储罐**(悬停条, Mekanism) | 气体: 数量/容量 mB, 以及气体名称 |
| 液体储罐下方的 **D** | 清空: 清空内部流体储罐(流体会被丢弃) |
| 气体储罐下方的 **D** | 清空: 清空气体储罐(气体会被丢弃) |

管道和储罐连接在**外部**; **内侧**面必须朝向涡轮机内部.

更改模式后, **重启**[涡轮机控制器](turbine_controller.md).

## 自动容量缩放

当涡轮机**重新验证**时, 端口的流体储罐会根据估算的**蒸汽 mB/t × 10** 调整大小, 下限为 **16,000 mB**, 且**没有固定上限**. 需求增加时容量会立即增长, 只有在储存的蒸汽仍能放入较小容量时才会缩小.
