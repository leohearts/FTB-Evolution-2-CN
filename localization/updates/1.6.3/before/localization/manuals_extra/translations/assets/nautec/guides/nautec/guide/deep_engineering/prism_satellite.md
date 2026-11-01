---
navigation:
  title: 棱镜卫星
  icon: nautec:prism_satellite
  position: 10
  parent: deep_engineering/deep_engineering-index.md
item_ids:
  - nautec:prism_satellite
  - nautec:uplink_array
---

# <Color id="aqua">棱镜卫星</Color>

<Column alignItems="center" fullWidth={true}>
  <Row>
    <ItemImage id="uplink_array" scale="2"/>
    <ItemImage id="prism_satellite" scale="2"/>
  </Row>
  无需中继链, 即可将激光能量(AP)和 FE 传输到网络中的任何位置.
</Column>

<ItemLink id="uplink_array"/>从你的激光中获取 AP, 从你的线缆中获取 FE, 并将它们向上发射到其上方轨道中的卫星. 卫星再将它们向下发送到同一网络中的每个输出[共鸣节点](resonance_node.md)和共鸣护符, 无论距离多远.

***

## <Color id="gold">设置</Color>

1. 放置一个<ItemLink id="uplink_array"/>. 它有两格高.
2. 空手右键点击它, 选择或创建一个网络, 方式与<ItemLink id="resonance_node"/>相同. 阵列和节点共享网络及其受信任玩家.
3. 手持<ItemLink id="prism_satellite"/>右键点击上行链路以发射. 卫星会升入轨道并留在那里, 直到上行链路被破坏, 此时它会掉落回来.
4. 将激光射入上行链路的侧面或底面, 并从任意面输入 FE.
5. 在需要能量的地方放置<ItemLink id="resonance_node"/>, 将其加入同一网络并设为**输出**.

***

## <Color id="gold">规则</Color>

* **天空:** 上行链路的碟形天线上方需要开阔天空. 只有固体方块会阻挡. 水, 玻璃和树叶都算开阔, 因此位于海床上或玻璃屋顶下的上行链路也能工作. 共鸣节点不需要天空.
* **维度:** 每台已发射卫星的上行链路都会为整个网络贡献同一个能量池, 无论处于哪个维度. 位于没有自身上行链路的维度中的输出节点仍会获得能量, 但其 AP 到达时纯度会降低 5%(`satelliteCrossDimensionPurityLoss`). 在该维度建造一台上行链路即可避免此损失.
* **共享:** 优先级最高的输出节点和护符会先被填充, 同优先级的则平均分配. 途中会损失 10%. 在拥有上行链路的维度内, 纯度会原样传递.
* **多台上行链路:** 网络中的每台上行链路都会加入同一个能量池, 无论其处于哪个维度. 它们的光束会合并, 因此能量池的纯度会接近最纯的上行链路.
* **已加载区块:** 上行链路只在其区块加载时工作. 在其界面中开启**加载**, 它就会保持自身区块加载, 除非服务器已关闭该功能(`resonanceChunkLoading`).

界面会显示上行链路是否在线, 若不在线则显示它正在等待什么, 以及它持有的 AP 和 FE 数量.

***

## <Color id="gold">缓冲</Color>

每台上行链路最多可储存 5,000,000 AP 和 5,000,000 FE(`satelliteApBuffer` 和 `satelliteFeBuffer`). 它会储存射入的 AP 及其纯度, 以及推入的 FE, 并保留两者, 直到网络中的输出节点或护符需要它们, 因此上行链路可以在输出建成之前就填满.

优先级和每 tick 上限在各输出节点上设置; 见[共鸣节点](resonance_node.md).
