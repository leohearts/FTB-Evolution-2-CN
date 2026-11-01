---
navigation:
  title: 激光合成矩阵
  icon: nautec:laser_crafting_matrix
  position: 2
  parent: getting_started/getting_started-index.md
item_ids:
  - nautec:laser_crafting_matrix
---

# <Color id="light_purple">激光合成矩阵</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="laser_crafting_matrix" scale="2"/>
  在机器内进行激光转化, 从而可以自动化.
</Column>

所有[物品转化](item_transformation.md)也可以在矩阵中进行, 一次合成一个, 物品和流体通过管道进出, 而不是丢在地面上.

## <Color id="gold">搭建</Color>

矩阵只从**顶部**接收激光. 将中继器或催化器朝下对准它. 从侧面或底部到达的光束会被忽略.

每个配方需要至少达到其 AP 和至少达到其纯度的光束. 两者中任一不足时, 矩阵会等待并保留进度. 比配方所需更强的光束会让它运行得更快, 与其他机器相同(参见[更强的光束](stronger_beams.md)).

用空手右键点击可打开它.

* 箭头左侧有三个输入槽, 右侧有三个输出槽.
* 最左侧有两个输入储罐, 最右侧有两个输出储罐, 每个容量为 16,000 mB(可配置).
* 每个输入槽只能放不同的物品, 每个输入储罐只能装不同的流体, 因此管道不会把同一种物品摊到每个槽位.
* 手持装满的桶右键点击可为输入储罐加注, 手持空桶右键点击可取出流体, 优先从输出储罐取出.
* 漏斗和管道可插入输入槽并从输出槽抽出. [侧面配置](utilities.md)可分别为物品和流体设置每个面.

面板会显示当前配方所需的 AP 和纯度, 光束满足时显示为绿色, 不满足时显示为红色. 将鼠标悬停在箭头上可查看确切数值. Jade 会显示相同的信息, 以及配方的产物和矩阵等待的原因.

工作时, 中间的环带会旋转, 透镜会脉动.

***

## <Color id="gold">配方</Color>

JEI 会在激光合成分类下列出所有配方.

| 输入 | 产出 | AP | 纯度 | 时间 |
|---|---|---|---|---|
| 海蓝钢混合物 | 海蓝钢锭 | 10 | 任意 | 1 秒 |
| 海蓝钢混合物 | 2 个海蓝钢锭 | 20 | 2.0 | 1 秒 |
| <ItemLink id="burnt_coil"/> | 激光引导线圈 | 20 | 1.5 | 5 秒 |
| 海晶水晶 | 2 个<ItemLink id="prismarine_crystal_shard"/> | 20 | 2.0 | 2 秒 |
| <ItemLink id="cast_iron_block"/> | 4 个<ItemLink id="gear"/> | 40 | 2.5 | 4 秒 |

当有多个配方匹配时, 矩阵会使用光束所满足的纯度最高的那一个.

整合包和数据包可以添加自己的 `nautec:laser_crafting` 配方, 最多三个物品输入, 两个流体输入, 三个物品输出和两个流体输出.

<RecipeFor id="laser_crafting_matrix"/>
