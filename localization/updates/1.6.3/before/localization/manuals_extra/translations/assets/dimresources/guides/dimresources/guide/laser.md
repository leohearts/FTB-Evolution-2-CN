---
navigation:
    title: 激光器
    icon: 'dimresources:laser'
    parent: index.md
    position: 5
item_ids:
    - 'dimresources:laser'
---

# 激光器

## 激光器搭建

跨维度激光器用于从其他行星开采方块.激光器必须放置在由维度石和维度石砖构成的结构上.示例如下

<GameScene zoom="1" interactive={true}>
  <ImportStructure src="assets/structures/laser.nbt" />
</GameScene>

激光器需要在 GUI 中放入行星定位器, 才能知道从哪颗行星开采

某些行星需要更高等级的激光器多方块结构.行星等级范围为 1 到 12.每提升一级, 多方块结构就需要高出一格

<GameScene zoom="1" interactive={true}>
  <ImportStructure src="assets/structures/lasermax.nbt" />
</GameScene>
