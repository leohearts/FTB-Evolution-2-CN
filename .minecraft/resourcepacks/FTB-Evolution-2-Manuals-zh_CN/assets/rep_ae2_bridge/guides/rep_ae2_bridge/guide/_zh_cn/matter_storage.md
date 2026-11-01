---
navigation:
    parent: index.md
    title: 物质存储
    icon: rep_ae2_bridge:matter_storage_cell_1k
    position: 30
categories:
- rep_bridge_components
item_ids:
- rep_ae2_bridge:matter_cell_housing
- rep_ae2_bridge:matter_storage_cell_1k
- rep_ae2_bridge:matter_storage_cell_4k
- rep_ae2_bridge:matter_storage_cell_16k
- rep_ae2_bridge:matter_storage_cell_64k
- rep_ae2_bridge:matter_storage_cell_256k
- rep_ae2_bridge:matter_storage_cell_creative
---

# 物质存储

<Row gap="20">
<ItemImage id="rep_ae2_bridge:matter_storage_cell_1k" scale="4"></ItemImage>
<ItemImage id="rep_ae2_bridge:matter_storage_cell_4k" scale="4"></ItemImage>
<ItemImage id="rep_ae2_bridge:matter_storage_cell_16k" scale="4"></ItemImage>
</Row>

物质存储元件可将 Replication 物质保存在你的 **ME 系统**中, 与普通元件存储物品的方式类似. 连接桥接器后, 这些元件中的物质也可供物质网络使用.

## 元件与外壳

- 使用 **物质元件外壳** 和对应的 AE2 元件组件 (1k / 4k / 16k / 64k / 256k) 建造元件
- 容量与所用组件一致, 组件越大, 可容纳的物质越多
- 也可按外壳的合成样板, 在中间放入组件, 一步合成元件
- **创造物质存储元件** 提供无限量的所有物质类型 (创造/测试用)

像其他存储元件一样, 将元件放入 ME驱动器或箱子即可. 终端可将物质类型与物品, 流体分开筛选.

## 输入, 输出与存储总线

加载本附属后, AE2 的 **ME输入总线**, **ME输出总线** 和 **ME存储总线** 可与相邻的 Replication **物质储罐** 及 **分解器** 之间传输物质. 像设置流体一样, 在总线上启用物质键类型即可.

装在物质储罐上的 **ME存储总线** 既会在 ME 系统中 **列出** 储罐内容, 也能插入或提取物质 (双向). 输入总线将物质从储罐拉入 ME; 输出总线将物质从 ME 推入储罐.

## 分解样板 (物品 → 物质)

在 **ME样板编码终端** 上, 使用额外的 **物质** 标签页 (蓝图图标):

- 在输入栏放入物品 (提高数量可按比例增加产出)
- 面板会预览物质数量 (不可选择)
- 编码后生成一个普通的 AE2 **处理样板**

将该样板放入朝向 **分解器** 的 **ME样板供应器**. 在分解器上用 **ME输入总线** (或存储总线) 抽取产出的物质. 桥接器还会将 Replication 网络中的物质作为库存映射到 ME 中.

## JEI 物质物品

本附属的虚拟物质物品是 JEI 辅助物品. 将其拖入 AE2 过滤器或监控器时, 会自动配置为真正的 **物质** 键.

## 存储监控器

手持 Replication **物质储罐** 或虚拟物质物品, 右键未锁定的 **存储监控器**:

- 已装填的储罐/物质物品 → 设为该物质类型
- 对空监控器使用空罐 → AE2 将设为储罐物品本身
- 已有设置时使用空罐 → 先设为第一种物质类型, 之后循环切换

## 自动合成与物质可见性

有桥接器时, AE2 合成任务会预留物质, 但不会将其从 ME 中取出. 库存仍保留在元件/储罐/总线中, 因此 Replication 依然可以看到; 实际消耗发生在样板运行时. 取消任务会清除虚拟预留, 不会复制物质.

## 提示

- 对于使用桥接器的 Replication 机器, 通过桥接器显示的物质与元件中存储的物质属于同一物质池
- 产出物质的自动合成任务需要在分解器上安装输入/存储总线; 仅靠桥接器映射只能显示库存, 无法完成样板供应器的产物回收
- 若要通过 AE2 转移大量物质, 请确保元件空间充足
